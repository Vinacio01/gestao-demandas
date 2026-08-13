## Gestão de Demandas

-RegistEste é um sistema de gestão de fluxos de trabalho desenvolvido com Django, projetado para organizar, categorizar e acompanhar o ciclo de vida de solicitações internas. Este sistema foi desenvolvido para resolver uma necessidade real de organização de processos, focando em usabilidade e visibilidade de prazos.
---

## Funcionalidades

- Criação e Categorização: Registro de demandas classificadas por tipos (Projeto, Vistoria, Postar, Voltar Assinado).
- Indicadores Visuais de Prazo (SLA): Sistema inteligente de cores baseado na data de criação para indicar a urgência de cada demanda:
  - Verde: Criada há menos de 1 dia
  - Amarelo: Entre 1 e 3 dias de criação.
  - Vermelho: Mais de 3 dias (atraso/atenção necessária).
- Gestão de Fluxo: Controle de documentos que precisam "Voltar Assinados", garantindo que nenhuma etapa burocrática seja esquecida.
- Interface Administrativa: Painel customizado para gestão rápida de dados.


---

## Tecnologias utilizadas

 **Linguagem:** Python 3.x Python 3.x  
 **Framework Web:** Django
 **Banco de Dados:** SQLite (Desenvolvimento) / Suporte a PostgreSQL (Produção)
 **Frontend:** Django Templates & CSS Customizado

---
O projeto segue o padrão MVT (Model-View-Template) do Django, com foco em uma modelagem de dados enxuta e eficiente:
- **Lógica de Negócio no Model:** Utilização de @property no modelo Demanda para calcular dinamicamente o status de urgência (cor_status) e o tempo de vida da demanda (dias_de_criacao). Isso garante que a regra de negócio esteja centralizada e seja fácil de manter.
- **Escalabilidade:** Estrutura preparada para migração para bancos de dados mais robustos (como PostgreSQL) e expansão para uma API REST utilizando Django REST Framework.


##  Estrutura do projeto

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


