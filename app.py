import sqlite3
import json
import os
from flask import Flask, jsonify, request, g, render_template

# Configuração
app = Flask(__name__, template_folder='templates')
DATABASE = 'tasks.db'

# --- Funções de Conexão e Utilitários do Banco de Dados ---

def get_db():
    """Obtém ou cria a conexão com o banco de dados."""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        # Retorna linhas como dicionários para fácil conversão para JSON
        db.row_factory = sqlite3.Row
    return db

def query_db(query, args=(), one=False):
    """Função utilitária para executar queries no banco de dados."""
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute(query, args)
        db.commit()
        # Se for um SELECT, retorna os resultados
        if query.strip().upper().startswith("SELECT"):
            rv = cursor.fetchall()
            return (rv[0] if rv else None) if one else rv
        # Se for um INSERT, retorna o ID inserido
        elif query.strip().upper().startswith("INSERT"):
            return cursor.lastrowid
        # Para UPDATE/DELETE, retorna a contagem de linhas afetadas
        return cursor.rowcount
    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")
        # Lança o erro novamente para ser capturado pela rota Flask
        raise e
    finally:
        cursor.close()

@app.teardown_appcontext
def close_connection(exception):
    """Fecha a conexão com o banco de dados ao final de cada requisição."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    """Cria a tabela de tarefas se ela não existir."""
    with app.app_context():
        # Usa um cursor separado para garantir que a conexão seja aberta
        # e a tabela criada de forma segura.
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                due_date TEXT,
                status INTEGER NOT NULL DEFAULT 0,
                priority INTEGER NOT NULL DEFAULT 1 
            );
        ''')
        db.commit()
        print("Banco de dados inicializado/atualizado em tasks.db")

# Inicializa o banco de dados
init_db()

# --- Rotas da Aplicação ---

@app.route('/')
def index():
    """Serve o arquivo HTML principal da aplicação (index.html)."""
    # Usa render_template, que busca o arquivo na pasta 'templates'
    try:
        return render_template('index.html')
    except Exception as e:
        # Erro mais específico se o template não for encontrado
        return f"Erro: Arquivo index.html não encontrado na pasta 'templates'. Detalhe: {e}", 404

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Retorna todas as tarefas salvas."""
    try:
        # A ordenação por status e data é mantida no backend
        tasks = query_db("SELECT id, title, description, due_date, status, priority FROM tasks ORDER BY status ASC, due_date ASC")
        
        # Converte a lista de objetos Row para dicionários e o status para boolean
        tasks_list = []
        for task in tasks:
            task_dict = dict(task)
            task_dict['is_completed'] = bool(task_dict.pop('status'))
            tasks_list.append(task_dict)

        return jsonify(tasks_list)
    except Exception as e:
        return jsonify({'error': f'Erro ao buscar tarefas: {str(e)}'}), 500


@app.route('/tasks', methods=['POST'])
def add_task():
    """Adiciona uma nova tarefa."""
    data = request.get_json()
    title = data.get('title')
    description = data.get('description', '')
    # O valor None é mantido se a data não for fornecida
    due_date = data.get('due_date') or None 
    
    if not title:
        return jsonify({'error': 'O título é obrigatório.'}), 400

    try:
        new_id = query_db(
            "INSERT INTO tasks (title, description, due_date, status, priority) VALUES (?, ?, ?, ?, ?)",
            (title, description, due_date, 0, 1) 
        )
        return jsonify({'id': new_id, 'message': 'Tarefa adicionada com sucesso!'}), 201
    except Exception as e:
        return jsonify({'error': f'Erro ao adicionar tarefa: {str(e)}'}), 500

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Atualiza uma tarefa existente (título, descrição, data ou status)."""
    data = request.get_json()

    # Prepara o status (0 ou 1) se is_completed for fornecido
    if 'is_completed' in data:
        data['status'] = 1 if data.pop('is_completed') else 0
    
    set_clauses = []
    values = []
    
    # Montagem dinâmica e segura da query de atualização
    allowed_fields = ['title', 'description', 'due_date', 'status']
    for key, value in data.items():
        if key in allowed_fields: 
            set_clauses.append(f"{key} = ?")
            # Converte data vazia para None para SQLite
            values.append(value if value != '' else None) 

    if not set_clauses:
        return jsonify({'error': 'Nenhum campo válido para atualização fornecido.'}), 400

    values.append(task_id)
    query = f"UPDATE tasks SET {', '.join(set_clauses)} WHERE id = ?"

    try:
        row_count = query_db(query, values)
        if row_count == 0:
            return jsonify({'error': 'Tarefa não encontrada.'}), 404
        return jsonify({'message': 'Tarefa atualizada com sucesso!'}), 200
    except Exception as e:
        return jsonify({'error': f'Erro ao atualizar tarefa: {str(e)}'}), 500

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Exclui uma tarefa pelo ID."""
    try:
        row_count = query_db("DELETE FROM tasks WHERE id = ?", (task_id,))
        if row_count == 0:
            return jsonify({'error': 'Tarefa não encontrada.'}), 404
        return jsonify({'message': 'Tarefa excluída com sucesso!'}), 200
    except Exception as e:
        return jsonify({'error': f'Erro ao excluir tarefa: {str(e)}'}), 500

# O bloco if __name__ é mantido para clareza
if __name__ == '__main__':
    print("Servidor Flask configurado. Use 'py -m flask run' para iniciar.")