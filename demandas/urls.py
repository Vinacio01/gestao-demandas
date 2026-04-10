from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_demandas, name='lista_demandas'),
    path('excluir/<int:id>/', views.excluir_demanda, name='excluir_demanda'),
    path('mover/', views.mover_demanda, name='mover_demanda'),
]