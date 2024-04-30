import time

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = """
      EXTRATO
-------------------
"""
numero_saques =  0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    match opcao:
        case "d":
            deposito = float(input("Quanto você vai depositar? R$ "))
            
            if deposito > 0:
                print("Depositando, aguarde...")
                saldo += deposito
                extrato += f"|      + R$ {deposito:.2f}   |\n"
                time.sleep(3)
                print("Depósito realizado com sucesso.")
            else: 
                print("Valor inválido para depósito, tente novamente.")
                
        case "s":
            if numero_saques == LIMITE_SAQUES:
                print(f"Não é possível realizar um novo saque, pois já foram utilizados os {LIMITE_SAQUES} saques diários.")
                print("Tente novamente amanhã.")
            else:
                saque = int(input("Quando você quer sacar? R$ "))

                if saque > limite:
                    print(f"O valor que deseja sacar é maior que o valor limite de R$ {limite}.")
                    print("Tente novamente com um valor menor.")
                elif saque > saldo:
                    print("Saldo insuficiente...")
                elif saque > 0:
                    print("Sacando, aguarde...")
                    saldo -= saque
                    numero_saques += 1
                    extrato += f"|      - R$ {saque:.2f}   |\n"
                    time.sleep(3)
                    print("Saque realizado com sucesso.")
                else:
                    print("O valor que deseja sacar é inválido, tente novamente.")                

        case "e":
            print(extrato)
            print(f"| Saldo: R$ {saldo:.2f}  |")
            print("-------------------")
        case "q":
            print("Volte sempre...")
            break
        case _:
            print("Operação inválida, por favor selecione novamente a operação desejada.")