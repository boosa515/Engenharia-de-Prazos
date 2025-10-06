# < Engenharia de Prazos: Task Manager Inteligente > ⚙️

![Status do Projeto](https://img.shields.io/badge/Status-FINALIZADO-success?style=for-the-badge)
![Tecnologia Backend](https://img.shields.io/badge/Backend-Python%20%7C%20Flask-blue?style=for-the-badge&logo=python)
![Tecnologia Frontend](https://img.shields.io/badge/Frontend-HTML%20%7C%20Tailwind%20%7C%20JS-blueviolet?style=for-the-badge&logo=tailwindcss)
![Banco de Dados](https://img.shields.io/badge/DB-SQLite-lightgrey?style=for-the-badge&logo=sqlite)

## 💡 Sobre o Projeto

O **Engenharia de Prazos** é um Gerenciador de Tarefas Full-Stack desenvolvido para estudantes e profissionais que lidam com múltiplos prazos de alta complexidade (relatórios, projetos, provas).

Este sistema, construído do zero com **Python + Flask**, utiliza um motor de **Priorização de Urgência Automática** (baseado na data de vencimento) e oferece uma interface limpa, moderna e totalmente adaptável através dos modos **Claro e Escuro**, garantindo que as atividades mais críticas estejam sempre em foco.

### Estrutura do Projeto

engenharia-de-prazos/
├── app.py                  # Backend (API REST, Flask e lógica do servidor)
├── requirements.txt        # Dependências do Python
├── tasks.db                # Banco de dados SQLite (gerado e ignorado pelo Git)
├── .gitignore              # Ignora arquivos de cache e o BD local
└── templates/
└── index.html          # Frontend (HTML, CSS customizado e JavaScript)

### Tecnologias Utilizadas

| Categoria | Tecnologia | Justificativa |
| :--- | :--- | :--- |
| **Backend** | Python 3.x, Flask | Framework simples e didático, perfeito para APIs REST rápidas. |
| **Banco de Dados** | SQLite3 | Persistência de dados leve e nativa do Python, ideal para projetos single-user. |
| **Design/UX** | Tailwind CSS | Estilização rápida, responsiva e moderna com classes utilitárias. |
| **Lógica** | JavaScript (Vanilla) | Controle de navegação em tela única e toda a lógica de priorização e filtros. |

---

## ⚙️ Funcionalidades Avançadas

1.  **Priorização Automática de Urgência:** Classifica e reordena tarefas sem intervenção manual, baseada na proximidade da data de entrega.
2.  **Organização por Disciplina (Tags):** Permite categorizar tarefas por matérias (Cálculo, Programação, Física, etc.) e filtrar a lista.
3.  **Controle de Visão (Views):** Navegação fluida em tela única entre a **Lista Principal** (Filtros + Tarefas) e a **Tela de Adição** (`+ Adicionar Tarefa`).
4.  **Design Adaptável:** Suporte a **Modo Escuro / Modo Claro** com um toque de design profissional (gradiente azul-roxo no tema claro).

### 📅 Detalhe da Priorização Automática

| Urgência | Condição | Efeito Visual |
| :--- | :--- | :--- |
| **URGENTE** | Vencimento em $\le 2$ dias. | Destaque e animação de alerta. |
| **ALTA** | Vencimento entre **3 e 5 dias**. | Destaque laranja. |
| **MÉDIA** | Vencimento em $> 5$ dias. | Destaque azul (cor principal). |
| **EXPIRADA** | Vencimento **já ultrapassado**. | Destaque vermelho escuro e filtro dedicado. |

---

## 🛠️ Instalação e Execução (VS Code Ready)

Para rodar este projeto em um ambiente de desenvolvimento limpo e profissional, siga os passos abaixo, idealmente dentro do Visual Studio Code.

### Pré-requisitos

* **Python 3.x**
* **Git** (Instalado e configurado no PATH)

### 1. Clonar e Configurar o Ambiente Virtual

Abra o terminal na pasta onde deseja clonar o projeto:

```bash
# 1. Clona o repositório
git clone [https://github.com/boosa515/Engenharia-de-Prazos.git](https://github.com/boosa515/Engenharia-de-Prazos.git)
cd Engenharia-de-Prazos

# 2. Cria o ambiente virtual
python -m venv venv

# 3. Ativa o ambiente virtual (Windows)
.\venv\Scripts\activate
# (Para macOS/Linux use: source venv/bin/activate)

2. Instalar Dependências
Com o ambiente virtual ativado ((venv) deve aparecer no seu terminal), instale o Flask:

pip install -r requirements.txt

Aqui está o arquivo README.md final. Ele está totalmente configurado para o seu projeto, destacando todas as funcionalidades avançadas que desenvolvemos, incluindo as Tags de Matéria e a configuração profissional para o Visual Studio Code.

Basta criar um arquivo chamado README.md na raiz do seu projeto e colar o código abaixo.

Code snippet

# < Engenharia de Prazos: Task Manager Inteligente > ⚙️

![Status do Projeto](https://img.shields.io/badge/Status-FINALIZADO-success?style=for-the-badge)
![Tecnologia Backend](https://img.shields.io/badge/Backend-Python%20%7C%20Flask-blue?style=for-the-badge&logo=python)
![Tecnologia Frontend](https://img.shields.io/badge/Frontend-HTML%20%7C%20Tailwind%20%7C%20JS-blueviolet?style=for-the-badge&logo=tailwindcss)
![Banco de Dados](https://img.shields.io/badge/DB-SQLite-lightgrey?style=for-the-badge&logo=sqlite)

## 💡 Sobre o Projeto

O **Engenharia de Prazos** é um Gerenciador de Tarefas Full-Stack desenvolvido para estudantes e profissionais que lidam com múltiplos prazos de alta complexidade (relatórios, projetos, provas).

Este sistema, construído do zero com **Python + Flask**, utiliza um motor de **Priorização de Urgência Automática** (baseado na data de vencimento) e oferece uma interface limpa, moderna e totalmente adaptável através dos modos **Claro e Escuro**, garantindo que as atividades mais críticas estejam sempre em foco.

### Estrutura do Projeto

engenharia-de-prazos/
├── app.py                  # Backend (API REST, Flask e lógica do servidor)
├── requirements.txt        # Dependências do Python
├── tasks.db                # Banco de dados SQLite (gerado e ignorado pelo Git)
├── .gitignore              # Ignora arquivos de cache e o BD local
└── templates/
└── index.html          # Frontend (HTML, CSS customizado e JavaScript)


### Tecnologias Utilizadas

| Categoria | Tecnologia | Justificativa |
| :--- | :--- | :--- |
| **Backend** | Python 3.x, Flask | Framework simples e didático, perfeito para APIs REST rápidas. |
| **Banco de Dados** | SQLite3 | Persistência de dados leve e nativa do Python, ideal para projetos single-user. |
| **Design/UX** | Tailwind CSS | Estilização rápida, responsiva e moderna com classes utilitárias. |
| **Lógica** | JavaScript (Vanilla) | Controle de navegação em tela única e toda a lógica de priorização e filtros. |

---

## ⚙️ Funcionalidades Avançadas

1.  **Priorização Automática de Urgência:** Classifica e reordena tarefas sem intervenção manual, baseada na proximidade da data de entrega.
2.  **Organização por Disciplina (Tags):** Permite categorizar tarefas por matérias (Cálculo, Programação, Física, etc.) e filtrar a lista.
3.  **Controle de Visão (Views):** Navegação fluida em tela única entre a **Lista Principal** (Filtros + Tarefas) e a **Tela de Adição** (`+ Adicionar Tarefa`).
4.  **Design Adaptável:** Suporte a **Modo Escuro / Modo Claro** com um toque de design profissional (gradiente azul-roxo no tema claro).

### 📅 Detalhe da Priorização Automática

| Urgência | Condição | Efeito Visual |
| :--- | :--- | :--- |
| **URGENTE** | Vencimento em $\le 2$ dias. | Destaque e animação de alerta. |
| **ALTA** | Vencimento entre **3 e 5 dias**. | Destaque laranja. |
| **MÉDIA** | Vencimento em $> 5$ dias. | Destaque azul (cor principal). |
| **EXPIRADA** | Vencimento **já ultrapassado**. | Destaque vermelho escuro e filtro dedicado. |

---

## 🛠️ Instalação e Execução (VS Code Ready)

Para rodar este projeto em um ambiente de desenvolvimento limpo e profissional, siga os passos abaixo, idealmente dentro do Visual Studio Code.

### Pré-requisitos

* **Python 3.x**
* **Git** (Instalado e configurado no PATH)

### 1. Clonar e Configurar o Ambiente Virtual

Abra o terminal na pasta onde deseja clonar o projeto:

```bash
# 1. Clona o repositório
git clone [https://github.com/boosa515/Engenharia-de-Prazos.git](https://github.com/boosa515/Engenharia-de-Prazos.git)
cd Engenharia-de-Prazos

# 2. Cria o ambiente virtual
python -m venv venv

# 3. Ativa o ambiente virtual (Windows)
.\venv\Scripts\activate
# (Para macOS/Linux use: source venv/bin/activate)

2. Instalar Dependências
Com o ambiente virtual ativado ((venv) deve aparecer no seu terminal), instale o Flask:

pip install -r requirements.txt

3. Executar a Aplicação

Inicie o servidor de desenvolvimento Flask. O banco de dados tasks.db será criado automaticamente na primeira execução.

# 1. Define o arquivo principal do Flask
export FLASK_APP=app.py 

# 2. Inicia o servidor
flask run

4. Acesso
Abra seu navegador e acesse:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)
