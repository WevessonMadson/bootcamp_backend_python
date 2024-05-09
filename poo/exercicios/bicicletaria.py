class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar():
        print("bibi, bibi")
    
    def parar(self):
        print("Shhhhhh...")
    
    def correr(self):
        print("Zummmmmm, Zummmmm....")

    # extra:
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


bike1 = Bicicleta("preta", "bmx", 2003, 750.32)

print(bike1)