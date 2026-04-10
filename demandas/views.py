from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Demanda
import json

def lista_demandas(request):
    if request.method == "POST":
        tipo = request.POST.get("tipo")
        voltar_assinado = True if tipo == "Voltar assinado" else False

        Demanda.objects.create(
            titulo=request.POST.get("titulo"),
            descricao=request.POST.get("descricao"),
            tipo=tipo,
            voltar_assinado=voltar_assinado
        )
        return redirect("lista_demandas")

    colunas = {
        "Projetos": Demanda.objects.filter(tipo="Projeto").order_by("-data_criacao"),
        "Vistorias": Demanda.objects.filter(tipo="Vistoria").order_by("-data_criacao"),
        "Postar": Demanda.objects.filter(tipo="Postar").order_by("-data_criacao"),
        "Voltar assinado": Demanda.objects.filter(tipo="Voltar assinado").order_by("-data_criacao"),
    }

    for demandas in colunas.values():
        for demanda in demandas:
            demanda.cor = demanda.cor_status

    return render(request, "demandas/lista.html", {"colunas": colunas})


def excluir_demanda(request, id):
    try:
        demanda = Demanda.objects.get(id=id)
        demanda.delete()
    except Demanda.DoesNotExist:
        pass
    return redirect("lista_demandas")


def mover_demanda(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            demanda_id = data.get("id")
            nova_coluna = data.get("nova_coluna")

            mapa = {
                "Projetos": "Projeto",
                "Vistorias": "Vistoria",
                "Postar": "Postar",
                "Voltar assinado": "Voltar assinado"
            }

            tipo_correto = mapa.get(nova_coluna, nova_coluna)

            demanda = Demanda.objects.get(id=demanda_id)
            demanda.tipo = tipo_correto
            demanda.voltar_assinado = True if tipo_correto == "Voltar assinado" else False
            demanda.save()

            return JsonResponse({"status": "ok"})

        except Exception as e:
            return JsonResponse({"status": "erro", "mensagem": str(e)})

    return JsonResponse({"status": "erro"})