import sqlite3
import json
from flask import Flask, jsonify, request, g, send_file
from datetime import datetime
import os

# Configuração do Flask
app = Flask(__name__)
# Nome do arquivo do banco de dados SQLite
DATABASE = 'tasks.db'

# --- Funções de Conexão com o Banco de Dados ---

def get_db():
    """Obtém a conexão com o banco de dados."""
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        # Configura a conexão para retornar linhas como dicionários (útil para JSON)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    """Fecha a conexão com o banco de dados ao final de cada requisição."""
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    """Cria a tabela de tarefas se ela não existir e garante que colunas existam."""
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        
        # Cria a tabela principal se não existir (Mantendo 'priority' para evitar erros de schema)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                due_date TEXT,
                status INTEGER NOT NULL DEFAULT 0,
                priority INTEGER NOT NULL DEFAULT 1 -- Coluna mantida, mas não usada pelo frontend
            );
        ''')
        db.commit()
        print("Banco de dados inicializado/atualizado em tasks.db")

# Inicializa o banco de dados quando o script é executado
with app.app_context():
    init_db()

# --- Rotas da API (CRUD) ---

@app.route('/')
def index():
    """Serve o arquivo HTML principal."""
    try:
        return send_file('index.html')
    except FileNotFoundError:
        return "Erro: Arquivo index.html não encontrado.", 404

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Retorna todas as tarefas salvas, ordenadas apenas por Status e Data (a ordenação de urgência é feita no frontend)."""
    db = get_db()
    cursor = db.cursor()
    # Ordem: status (0=pendente primeiro), due_date (mais próxima primeiro)
    cursor.execute("SELECT id, title, description, due_date, status, priority FROM tasks ORDER BY status ASC, due_date ASC")
    tasks = cursor.fetchall()

    tasks_list = [dict(task) for task in tasks]

    # Converte o status (INTEGER) para BOOLEAN para o frontend
    for task in tasks_list:
        task['is_completed'] = bool(task['status'])
        del task['status']

    return jsonify(tasks_list)

@app.route('/tasks', methods=['POST'])
def add_task():
    """Adiciona uma nova tarefa."""
    data = request.get_json()
    title = data.get('title')
    description = data.get('description', '')
    due_date = data.get('due_date', None) # Data pode ser nula
    
    if not title:
        return jsonify({'error': 'O título é obrigatório.'}), 400

    db = get_db()
    cursor = db.cursor()
    try:
        # A coluna 'priority' será salva com o valor padrão 1 (Baixa), mas ignorada pelo frontend
        cursor.execute(
            "INSERT INTO tasks (title, description, due_date, status, priority) VALUES (?, ?, ?, ?, ?)",
            (title, description, due_date, 0, 1) 
        )
        db.commit()
        new_task_id = cursor.lastrowid
        return jsonify({'id': new_task_id, 'message': 'Tarefa adicionada com sucesso!'}), 201
    except Exception as e:
        return jsonify({'error': f'Erro ao adicionar tarefa: {str(e)}'}), 500

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Atualiza uma tarefa existente (título, descrição, data ou status)."""
    data = request.get_json()
    db = get_db()
    cursor = db.cursor()

    if 'is_completed' in data:
        data['status'] = 1 if data['is_completed'] else 0
        del data['is_completed']

    set_clauses = []
    values = []
    for key, value in data.items():
        # Remove 'priority' dos campos que podem ser atualizados
        if key in ['title', 'description', 'due_date', 'status']: 
            set_clauses.append(f"{key} = ?")
            values.append(value)

    if not set_clauses:
        return jsonify({'error': 'Nenhum campo válido para atualização fornecido.'}), 400

    values.append(task_id)
    query = f"UPDATE tasks SET {', '.join(set_clauses)} WHERE id = ?"

    try:
        cursor.execute(query, values)
        db.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Tarefa não encontrada.'}), 404
        return jsonify({'message': 'Tarefa atualizada com sucesso!'}), 200
    except Exception as e:
        return jsonify({'error': f'Erro ao atualizar tarefa: {str(e)}'}), 500

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Exclui uma tarefa pelo ID."""
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        db.commit()
        if cursor.rowcount == 0:
            return jsonify({'error': 'Tarefa não encontrada.'}), 404
        return jsonify({'message': 'Tarefa excluída com sucesso!'}), 200
    except Exception as e:
        return jsonify({'error': f'Erro ao excluir tarefa: {str(e)}'}), 500

if __name__ == '__main__':
    print("Servidor Flask configurado. Use 'py -m flask run' para iniciar.")
