# < Engenharia de Prazos: Task Manager Inteligente > ⚙️

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask Badge"/>
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite Badge"/>
  <img src="https://img.shields.io/badge/Full_Stack-FFC72C?style=for-the-badge" alt="Full Stack Badge"/>
</p>

## 💡 Sobre o Projeto

Gerenciador de tarefas Full-Stack desenvolvido com **Python (Flask)** e **SQLite**, focado em gerenciamento de prazos complexos.

O principal diferencial é o **motor de Priorização de Urgência Automática** (baseado na data de vencimento) e uma interface moderna com suporte a **Modo Escuro / Modo Claro**.

### ⚙️ Principais Funcionalidades

* **Priorização Automática:** Classificação e reordenação de tarefas baseada na proximidade do prazo (**Urgente**, **Alta**, **Média**, **Expirada**).
* **Controle de Status:** CRUD completo (Adicionar, Editar, Excluir, Marcar como Concluída) de tarefas.
* **Design Adaptável:** Interface fluida em tela única com suporte a temas.

---

## 🛠️ Instalação e Execução

### Pré-requisitos

* Python 3.x

### 1. Configurar o Ambiente

Assumindo que você já clonou o repositório e está no diretório do projeto:

```bash
# Cria e ativa o ambiente virtual
python -m venv venv

# Windows:
.\venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate

# Instala as dependências (Flask)
pip install -r requirements.txt

2. Rodar a Aplicação
Com o ambiente virtual ativado, execute o servidor Flask. O banco de dados tasks.db será criado automaticamente.

# 1. Define o arquivo principal do Flask
export FLASK_APP=app.py 

# 2. Inicia o servidor
flask run

3. Acesso
Abra seu navegador e acesse: http://127.0.0.1:5000/
