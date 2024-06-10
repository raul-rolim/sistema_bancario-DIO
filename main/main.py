# #EXTRATO
# 	-Positional (saldo) and Keyword (extrato)
#
# #CRIAR USUÁRIO (CLIENTE)
# 	-Armazenar em uma lista (nome,nascimento,cpf e endereço 	(logradouro, numero - bairro - cidade/sigla estado)
# 	-Apenas um cadastro por CPF
#
# #CRIAR CONTA CORRENTE
# 	-Lista: agência, número da conta e usuário
# 	-Número da conta é sequencial, iniciando em 1
# 	-Agência é fixo: 0001
# 	-O usuário pode ter mais de uma conta, mas deve pertencer a apenas 	um usuário cada conta.



def menu():
    menu = """
    \n
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [nu] Novo Usuário
    [q] Sair

    Opção Selecionada
    """
    opcao = input(menu)
    return opcao

def main():
    global numero_conta
    global usuario
    global conta_corrente
    numero_conta = 1
    usuarios = []
    contas = []


    while True:
        usuario_logado = usuario["cpf"] is not None
        opcao = menu()
        if opcao == 'd' and usuario_logado:
            valor_a_depositar = float(input("Insira o valor que deseja depositar: "))
            depositar(valor_a_depositar, conta_corrente["saldo"], conta_corrente["extrato"])

        elif opcao == 's' and usuario_logado:
            valor_a_sacar = float(input("Insira o valor que deseja sacar: "))
            saque(valor_sacado=valor_a_sacar, saldo=conta_corrente["saldo"], extrato=conta_corrente["extrato"], conta_corrente=conta_corrente)

        elif opcao == 'e' and usuario_logado:
            extrato(conta_corrente["saldo"], conta_corrente["nome"], extrato=conta_corrente["extrato"])

        elif opcao == 'nc':
            criar_conta(usuarios)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'q':
            print("Obrigado por utilizar nossos serviços!\nAté a próxima")
            exit()

        else:
            print("Opção inválida. Tente Novamente")

def depositar(valor_depositado, saldo, extrato, /):
    if valor_depositado > 0:
        saldo += valor_depositado
        extrato += f"Depósito: R$ {valor_depositado:.2f}\n"
        print("Depósito realizado com sucesso!\n")
    else:
        print("Não foi possível efetuar o depósito. O valor inserido é inválido")

def saque(*, valor_sacado, saldo, extrato, conta_corrente):

    saque_valido = 0 < valor_sacado <= conta_corrente["limite_por_saque"]
    saldo_suficiente = saldo >= valor_sacado and saldo >= 0
    limite_saques = conta_corrente["numero_saques"] >= conta_corrente["LIMITE_SAQUES"]

    if saque_valido and saldo_suficiente:
        saldo -= valor_sacado
        extrato += f"Saque: R$ {valor_sacado:.2f}\n"
        conta_corrente["numero_saques"] += 1
        print("Saque realizado com sucesso!\n")

    elif saldo < valor_sacado:
        print("Não foi possível efetuar o saque. Saldo Insuficiente")

    elif limite_saques:
        print("Você atingiu o limite de quantidades de saques diários!")

    else:
        print("Não foi possível efetuar o saque. O valor inserido é inválido!")

def extrato(saldo, /, nome, *, extrato):
    print("================ EXTRATO ================")
    if extrato == "":
        print(f"{nome}\nVocê ainda não realizou nenhuma operação no momento!")
    else:
        print(f"Saldo Disponível: R$ {saldo:.2f}\n")
        print(extrato)
    print("=========================================")

def criar_usuario(usuarios):
    nome = input("Insira seu nome: ")
    cpf = input("Insira seu cpf: ")
    if verificar_usuario(usuarios, cpf):
        print("Erro!\nO CPF inserido já foi cadastrado anteriormente!")

    else:
        data_nascimento = input("Insira sua data de nascimento: ")
        endereco = input("Insira seu endereço (logradouro, número da residência, bairro - estado/sigla cidade): ")
        global usuario
        usuario = {'nome': nome,
                   'cpf': cpf,
                   'data_nascimento': data_nascimento,
                   'endereço': endereco
                   }

        usuarios.append(usuario)

        print(f"Usuário criado com sucesso\nBem Vindo {nome}")

        print(usuario)

def verificar_usuario(usuarios, cpf):
    for usuario in usuarios:

        if cpf == usuario['cpf']:
            return True

    return False

def criar_conta(usuario):
    global numero_conta
    global conta_corrente
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite_por_saque = 500
    extrato = ""
    numero_saques = 0
    if usuario['cpf'] is None:
        print("Você ainda não se cadastrou!")
    else:
        conta_corrente = {'usuario':usuario,
                          'saldo':saldo,
                          'extrato':extrato,
                          'limite_por_saque':limite_por_saque,
                          'LIMITE_SAQUES':LIMITE_SAQUES,
                          'numero_saques':numero_saques,
                          'numero_conta':numero_conta,
                          'agencia':AGENCIA}
        numero_conta += 1

main()