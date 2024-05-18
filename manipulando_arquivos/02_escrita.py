file = open("./teste.txt", "a")

file.write("Teste de escrita")


file.close()

# usando append e usando as boas práticas com o bloco with, como também o encoding e verificação de abertura com try except:

try:
    with open("./teste.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write("\nteste de escrita 2, acrescentando ao arquivo já escrito.")
except IOError as exc:
    print(f"Não foi possível abrir o arquivo: {exc}")
    