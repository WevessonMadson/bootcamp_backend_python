import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")

cursor = conexao.cursor()


# criando uma tabela:
def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(100))"
    )


# inserindo dados:
def inserir_registro(conexao, cursor, nome, email):
    data = ("Wevesson Madson", "teste.teste@gmail.com")
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", data)

    data = [
        ("Silva", "email@teste.com"),
        ("Cabral", "outro_email@tes.com"),
        ("Obrian", "outro_ainda@teste.com"),
    ]
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES(?, ?)", data)

    conexao.commit()


# atualizando dados na base:
def atualizar_registros(conexao, cursor, nome, email, id):
    data = ("Wevesson Silva", 1)
    cursor.execute("UPDATE clientes SET nome = ? WHERE id = ?", data)

    conexao.commit()


# deletando dados da tabela:
def deletar_registro(conexao, cursor, id):
    data = id
    cursor.execute("DELETE FROM clientes WHERE id = ?", data)

    conexao.commit()


# consultando os registros:
# fetchone
def consulta_um_registro(cursor, id):
    cursor.row_factory = sqlite3.Row
    data = id
    cursor.execute("SELECT * FROM clientes WHERE id = ?", data)
    result = cursor.fetchone()
    print(dict(result))


# fetchall
def consulta_varios_registros(cursor):
    cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM clientes")
    results = cursor.fetchall()

    for registo in results:
        print(dict(registo))


consulta_um_registro(cursor, "2")
consulta_varios_registros(cursor)
