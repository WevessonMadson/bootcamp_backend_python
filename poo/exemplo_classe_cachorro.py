class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        if self.acordado:
            print("Auau")
    
    def dormir(self):
        self.acordado = False
        print("Zzzzzz...")



# Instanciando objetos de exemplo:

cao_1 = Cachorro("chappie", "amarelo", False)
cao_2 = Cachorro("Aladim", "Branco e preto")

cao_1.latir() # não late porque o cachorro está dormindo

print(cao_2.acordado)

cao_2.dormir()

print(cao_2.acordado)