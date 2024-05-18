## Passagem por parâmentro:

def mensagem(nome):
    print("Executando nome.")
    return f'Oi {nome}'

def mensagem_longa(nome):
    print('Executando mensagem longa.')
    return f'Olá, tudo bem com você, {nome}?'

def executar(funcao, nome):
    print('executando executar')
    return funcao(nome)


print(executar(mensagem_longa, "Wevesson"))



## Função interna:

def principal():
    print("Executando a função principal")

    def interna_1():
        print("Exetunado a função interna #1")

    def interna_2():
        print("Excetando a função interna #2")

    interna_1()
    interna_2()

principal()


# Retornando função:

def calculadora(operacao):
    def soma(num1, num2):
        return num1 + num2
    
    def subtrai(num1, num2):
        return num1 - num2
    
    def multiplica(num1, num2):
        return num1 * num2
    
    def dividi(num1, num2):
        return num1 / num2
    
    match operacao:
        case "+":
            return soma
        
        case "-":
            return subtrai
        
        case "*":
            return multiplica
        
        case "/":
            return dividi
        
        case _: return "Operação é inválida."


# A função pode ser externalizada e salva numa variárel que consegue executar a função:
somarrr = calculadora("+")
subitrairrr = calculadora("-")
multiplicarrr = calculadora("*")
dividirrr = calculadora("/")

print(somarrr(2, 4))
print(subitrairrr(2, 4))
print(multiplicarrr(2, 4))
print(dividirrr(2, 4))


# Decorador é uma função:

def meu_decorador(funcao): # recebe  uma funcao
    def envelope(): # inner function
        print("Faz algo antes de executar a função.")
        
        funcao() # executa  a função que foi passada como argumento
        
        print("Faz algo depois de executar a função.")

    return envelope # retorna a função interna (inner function)


def ola_mundo_1():
    print("Olá, mundo #1!")


ola_mundo_1 = meu_decorador(ola_mundo_1)  # Decorou a função olá mundo

ola_mundo_1()


# Dar para usar o decorador de uma forma mais simples com o símbolo @

@meu_decorador  # dá no mesmo de fazer o exemplo antes
def ola_mundo():
    print("Olá, mundo #2!")

ola_mundo()


# E, se a função esperar argumentos? teremos que fazer uso de parametros na função interna, recebendo *args e **kwargs

def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return envelope


@duplicar 
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}!")

# aprender("Python")

# aprender("Inglês")


# E se quiser retornar o valor de retorno do decorador? Basta retorna a função decorada dentro da função interna

def duplicar_retorno(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return envelope


@duplicar_retorno
def tudo_maiusculo_duplo(tecnologia):
    print(f"Estou aprendendo {tecnologia}!")
    return tecnologia.upper()

tudo_maiusculo_duplo("Python")

print(tudo_maiusculo_duplo("Inglês"))


# Agora, para não perder os nomes das funções, podemos usar a biblioteca functools

import functools

def recupera(func):
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        func(*args, **kwargs)

    return envelope


@recupera
def recuperando_nome(tecnologia):
    print(f"Estou aprendendo {tecnologia}!")


print(ola_mundo.__name__) ## aqui se perde

print(recuperando_nome.__name__)  ## aqui retorna o nome correto