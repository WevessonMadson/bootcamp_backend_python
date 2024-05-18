## Classes:

Define as características e métodos, porém não é possível usá-las diretamente, mas sim construir objetos a partir delas para usá-los diretamente.

A classe é uma classificação de objetos do mundo real abstraidos para uma classificação computacional.

Uma classe Cachorro é um exemplo que podemos definir as características genéricas que um cachorro possui e ações (métodos que ele tem), como latir, correr, etc.

[Exemplo da classe Cachorro](./exemplo_classe_cachorro.py)

[Exercício da bicicletaria do João](./exercicios/bicicletaria.py)

#### Contrutores e Destrutores:

- O método construtor sempre é executado quando uma nova instância da classe é criada: ```__init__```
```
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
```

- O método destrutor é executado sempre que uma instância é destruída. 
- Destrutores em Python não são muito utilizados, pois o Python tem um coletor de lixo que lida com o gerenciamento de memória automaticamente. 
- Para declarar o método destrutor da classe, criamos um método com o nome ```__del__```

