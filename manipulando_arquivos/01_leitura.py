file = open('./loren.txt', 'r')

todo_conteudo = file.read()
print(todo_conteudo)

lista_de_conteudo_linhas = file.readlines()
print(lista_de_conteudo_linhas)

while len(linha := file.readline()): # a cada passagem, retorna uma linha
    print(linha)

file.close()

## Obs.: ao passar pela primeira leitura, as demais não podem ser lidas