## Python DB API

- Para conectar ao banco de dados, basta usar o conector correto;

- Exemplo de conexão com o sqlite3:

```
import sqlite3

con = sqlite3.connect('meu_banco.db')
```

- obs.: a conexão com todos os conectores vai sempre seguir o mesmo padrão: ``` nome_conector.connect("informações do banco") ```

#### criando tabela no banco

```
cursor = conexao.cursor()

cursor.execute(
    "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(100))"
)
```

#### inserindo dados na tabela:

```
data = ("Wevesson Madson", "teste.teste@gmail.com")
cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", data)

conexao.commit()

ou

data = [
    ("Silva", "email@teste.com"),
    ("Cabral", "outro_email@tes.com"),
    ("Obrian", "outro_ainda@teste.com"),
]
cur.executemany("INSERT INTO clientes (nome, email) VALUES(?, ?)", data)

conexao.commit()
```

#### atualizando dados:

```
data = ("Wevesson Silva", 1)
cursor.execute("UPDATE clientes SET nome = ? WHERE id = ?", data)

conexao.commit()
```


#### deletando dados:

```
data = id
cursor.execute("DELETE FROM clientes WHERE id = ?", data)

conexao.commit()
```


#### consultando dados:

```
# um registro apenas: fetchone
data = id
cursor.execute("SELECT * FROM clientes WHERE id = ?", data)
result = cursor.fetchone()
print(result)

# vários registros: fetchall
cursor.execute("SELECT * FROM clientes")
results = cursor.fetchall()

    for registo in results:
        print(registo)
```

#### alterando o row_factory

- Até agora, sempre está sendo retornado o registro como tupla;

- Se a tupla não atender as necessidades, podemos trocar para trabalhar com a row_factory do sqlite3.Row;

```
cursor.row_factory = sqlite3.Row
cursor.execute("SELECT * FROM clientes WHERE id = 2")
result = cursor.fetchone()
print(dict(result))
```

- dessa forma teremos um dicionário


### Controle de Transações:

```
try:
    cursor.execute("INSERT INTO clientes VALUES (? ?)", (1, "ABC"))
    conexao.commit()
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    conexao.rollback()
```

-  Fazer o rollback no caso de erro.
