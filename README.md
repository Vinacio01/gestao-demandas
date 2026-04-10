# Gestão de Demandas

Um sistema web simples para acompanhar demandas/tarefas, com contagem de dias desde a criação e sinalização de urgência.

Esse projeto foi desenvolvido como parte do meu aprendizado em desenvolvimento web com **Python** e **Django**.  
O objetivo é facilitar o acompanhamento de tarefas do dia a dia com prioridade visual por tempo de duração.

---

## Funcionalidades

- Cadastro de demandas
- Contador que mostra há quantos dias a demanda está ativa
- Sinalização de urgência com base no tempo de vida da demanda
- Edição e exclusão de demandas
- Interface web acessível via navegador

---

## Tecnologias utilizadas

 **Python** — Linguagem principal  
 **Django** — Framework web baseado em MTV (*Model-Template-View*) para desenvolvimento rápido de aplicações web, semelhante à arquitetura moderna de backends
 **HTML e CSS** — Interface de usuário

---

## 📁 Estrutura do projeto

```
Gestao-de-Demandas/
├── core/
│   └── demandas/
│       ├── migrations/
│       ├── templates/
│       ├── static/
│       ├── admin.py
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       └── ...
├── manage.py
├── .gitignore
└── README.md
```


Aqui o Django organiza modelos, views e URLs de forma modular para melhor manutenção do código.

---

## Instalação (Local)

> **Pré-requisitos:**  
> • Python instalado (versão 3.8+)  
> • Virtualenv criado e ativado

```bash
# 1. Clone o repositório
git clone https://github.com/Vinacio01/Gestao-de-Demandas.git

# 2. Acesse a pasta do projeto
cd Gestao-de-Demandas

# 3. Crie e ative ambiente virtual (opcional)
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# 4. Instale dependências
pip install django

# 5. Rode as migrações
python manage.py migrate

# 6. Inicie o servidor
python manage.py runserver


