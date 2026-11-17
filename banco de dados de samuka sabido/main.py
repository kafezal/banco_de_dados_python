import sqlite3

conexao = sqlite3.connect("escola.db")

cursor = conexao.cursor()

print("banco conectado!")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    curso TEXT
    )
''')

conexao.close()