### Manipulação de arquivos em Python

```
Objetivo geral:

Aprender a importância dos arquivos, como abrir, ler, escrever, e gerenciá-los com o Python.
```

- trabalharemos com os formatos .txt e .csv

###### Abertura e fechamento

- Para manipular arquivos em python, primeiro precisamos abrir: ``` open() ```

- Depois de manipular, precisamos fechar o arquivo: ``` close() ```

```
file = open("example.txt", "r") # r é para modo leitura, w gravação e a anexar

# fazemos algo com o arquivo ...

file.close()
```

###### Leitura do arquivo

- Para ler um arquivo existem várias maneiras: ``` read(), readline() e readliines() ```

```
file = open('example.txt', 'r')

print(file.read())

file.close()
```

- O ``` read() ``` retorna uma string que representa o conteúdo do arquivo;

- O ``` readline() ``` lê uma linha por vez, enquanto o ``` readlines() ``` retorna uma lista onde cada elemento é uma linha do arquivo;


###### Escrita de arquivos

- Para escrever em um arquivo, precisamos usar abrir o arquivo em modo escrita ou append: "w" or "a";

- Podemos usar a função ``` write() ``` ou ``` writelines() ```;

```
file = open("arquivo.extensao", "w")

file.write("Teste de escrita")

file.close()
```


###### Boas práticas

- É uma boa prática usar o bloco with, pois ele fecha o arquivo ao final do bloco;

- Também é uma boa prática verificar se o arquivo foi aberto corretamente antes de fazer operações, fazendo isso com o except de IOError;

- Abaixo a sintaxe do bloco with, com verificação de abertura:

```
try:
    with open("arquivo.extensao", "r") as arquivo:
        print(arquivo.read())
    
    # aqui, após o bloco, já não é mais possível fazer operações, pois o arquivo já foi fechado.

except IOError as exc:
    print(f"Não foi possível abrir o arquivo: {exc}")

```

- Também podemos informar o encoding = "utf-8" na função de abertura, para escrevermos e lermos informações com acentuação, por exemplo:

```
try:
    with open("arquivo.extensao", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Não foi possível abrir o arquivo: {exc}")
```


## Manipulação de arquivos CSV

- Python fornece um módulo chamado 'csv' para trabalhar com arquivos .csv;

```
import csv

try:
    with open('example.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except IOError as exc:
    print(f'Não foi possível abrir o arquivo: {exc}')            

try:
    with open('example.csv', 'w', encoding='utf-8', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["nome", "idade"])
        writer.writerow(["Ana", 30])
        writer.writerow(["João", 25])
except IOError as exc:
    print(f'Não foi possível abrir o arquivo: {exc}')            
```    

