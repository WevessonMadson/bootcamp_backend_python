import time

FALHA = "[FALHA]:"
SUCESSO = "[SUCESSO]:"
INFO = "[INFO]:"

def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):
    atingiu_limite_saques = numero_saques >= limite_saques

    if atingiu_limite_saques:
        print(f"{FALHA} Não é possível realizar um novo saque, pois já foram utilizados os {limite_saques} saques diários.")
        print(f"{INFO} Tente novamente amanhã.")
        
    else:
        valor_saque = int(input("Quanto você quer sacar? R$ "))

        ultrapassa_valor_limite = valor_saque > limite
        tem_saldo = valor_saque <= saldo
        valor_for_valido = valor_saque > 0

        if ultrapassa_valor_limite:
            print(f"{FALHA} O valor informado é maior que o valor limite: R$ {limite}.")
    
        elif not tem_saldo:
            print(f"{FALHA} Saldo insuficiente...")

        elif valor_for_valido:
            print(f"{INFO} Sacando, aguarde...")
            saldo -= valor_saque
            numero_saques += 1
            extrato += [f"- R$ {valor_saque:7.2f}"]
            time.sleep(3)
            print(f"{SUCESSO} Saque realizado com sucesso.")

        else:
            print(f"{FALHA} O valor que deseja sacar é inválido, tente novamente.")
    
    return saldo, extrato, numero_saques

def depositar(saldo, extrato, /):
    deposito = int(input("Quanto você quer depositar? R$ "))

    valor_for_valido = deposito > 0

    if valor_for_valido:
        print(f"{INFO} Depositando, aguarde...")
        saldo += deposito
        extrato += [f"+ R$ {deposito:7.2f}"]
        time.sleep(3)
        print(f"{SUCESSO} Depósito realizado com sucesso.")
    else: 
        print(f"{FALHA} O valor informado não é válido.")
    
    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    largura_extrato = 30

    linha_saldo = f"Saldo: R$ {saldo:.2f}"

    print(f"{INFO} Gerando o extrato, aguarde...\n")
    time.sleep(3)

    print("EXTRATO".center(largura_extrato))
    print("".center(largura_extrato, "="))

    for linha_transacao in extrato:
        print(f"{''.center(largura_extrato - len(linha_transacao) - 1)} {linha_transacao}")

    print(f"\n{''.center(largura_extrato - len(linha_saldo) - 1)} {linha_saldo}")
    print("".center(largura_extrato, "="))

def buscar_usuario(usuarios, *, cpf):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    nao_tem_usuarios = usuarios_filtrados == []

    print(f"{INFO} Consultando CPF do usuário, aguarde...")
    time.sleep(2)

    if nao_tem_usuarios:
        return False
    
    return usuarios_filtrados[0]   

def cadastrar_usuario(usuarios):
    cpf = input("Informe o cpf (apenas números): ")
    tem_usuario = buscar_usuario(usuarios, cpf=cpf)
    
    if tem_usuario:
        print(f"\n{FALHA} Já existe cadastro para este cpf.")
        print(f"{INFO} Tente listar as contas deste usuário na opção do MENU.")

    else:
        nome = input("\nInforme o primeiro e último nome do cliente: ")
        data_nascimento = input("Informe a data de nascimento (DD-MM-AAA): ")

        logradouro = input("\nInforme o logradouro: ")
        numero_endereco = input("Informe o número da residência: ")
        bairro = input("Informe o bairro: ")
        cidade = input("Informe a cidade: ")
        uf = input("Informe a UF (PE): ")

        endereco = f"{logradouro}, {numero_endereco}, - {bairro} - {cidade}/{uf}"

        usuarios += [{"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}]

        print(f"\n{INFO} Cadastrando usuário, aguarde...")
        time.sleep(2)
        print(f"{SUCESSO} Usuário cadastrado.")


    return usuarios

def criar_conta(usuarios, contas, agencia, ultima_conta):
    cpf = input("Informe o cpf (apenas números): ")
    usuario_existe = buscar_usuario(usuarios, cpf=cpf)

    if usuario_existe:
        ultima_conta += 1
        contas += [{"agencia": agencia, "conta": ultima_conta, "cpf": cpf}]
        print(f"\n{SUCESSO} Conta cadastrada com sucesso.")
        print(f"{INFO} Guarde as informações da conta:")    
        print(f"""
            ==========================
            Ag : {agencia}
            C/C: {ultima_conta}
            ==========================
             """)
    
    else:
        print(f"\n{FALHA} Esse usuário não está cadastrado.")
        print(f"{INFO} Tente cadastrá-lo antes.")

    return contas, ultima_conta   


def listar_contas(contas, cpf):
    contas_filtradas = [conta for conta in contas if conta["cpf"] == cpf]

    print(f"{INFO} Buscando contas, aguarde...")
    time.sleep(2)

    nao_tem_contas = contas_filtradas == []

    if nao_tem_contas:
        print(f"{INFO} Usuário não possui conta.")
    
    else:
        largura_extrato_contas = 40
        print(f"CONTAS DO CPF: {cpf}".center(largura_extrato_contas))
        print("".center(largura_extrato_contas, "="))

        for conta in contas_filtradas:
            print(f"\nAg : {conta['agencia']}")
            print(f"C/C: {conta['conta']}")

        print("".center(largura_extrato_contas, "="))


     

def start():
    menu = """

    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nu] Cadastrar usuário
    [nc] Cadastrar conta
    [sc] Listar contas do usuário
    [q]  Sair

    => """

    saldo = 0
    limite = 500
    extrato = []
    numero_saques =  0
    LIMITE_SAQUES = 3

    usuarios = []
    contas = []
    ultima_conta = 0
    AGENCIA = "0001"

    while True:
        opcao = input(menu)

        match opcao:
            case "d":
                saldo, extrato = depositar(saldo, extrato)
                    
            case "s":
                saldo, extrato, numero_saques = sacar(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)              

            case "e":
                mostrar_extrato(saldo, extrato=extrato)

            case "q":
                print("Volte sempre...")
                break

            case "nu":
                usuarios = cadastrar_usuario(usuarios)

            case "nc":
                contas, ultima_conta = criar_conta(usuarios, contas, AGENCIA, ultima_conta)
            
            case "sc":
                cpf = input("Informe o cpf do cliente: ")

                listar_contas(contas, cpf)
             
            case _:
                print("Operação inválida, por favor selecione novamente a operação desejada.")



start()


