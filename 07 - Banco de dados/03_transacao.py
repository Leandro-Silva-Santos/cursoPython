import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "clientes.sqlite")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute("DELETE FROM clientes WHERE id = 8;")
    conexao.commit()
    
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?)', ("Teste 2", 'teste@gmail.com'))
    cursor.execute('INSERT INTO clientes (id, nome, email)VALUES (?, ?, ?)', (5, 'Teste 3', 'teste3@hotmail.com'))
    conexao.commit()
except Exception as e:
    print(f"Ops! um erro ocorreu! {exc}")
    conexao.rollback()