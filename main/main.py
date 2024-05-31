saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

print("Bem Vindo ao Banco Virtual DIO")
menu = """
\n
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Opção Selecionada
"""

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor_depositado = float(input("Insira o valor que deseja depositar: "))

        if valor_depositado > 0:
            saldo += valor_depositado
            extrato += f"Depósito: R$ {valor_depositado:.2f}\n"
            print("Depósito realizado com sucesso!\n")
        else:
            print("Não foi possível efetuar o depósito. O valor inserido é inválido")

    elif opcao == 's':
        if numero_saques < LIMITE_SAQUES:
            print(f"Saldo Disponível: R$ {saldo:.2f}\n")
            valor_sacado = float(input("Insira o valor que deseja sacar: "))
            if (valor_sacado > 0 and valor_sacado <= limite) and (saldo >= valor_sacado and saldo >= 0):
                saldo -= valor_sacado
                extrato += f"Saque: R$ {valor_sacado:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso!\n")
            elif saldo < valor_sacado:
                print("Não foi possível efetuar o saque. Saldo Insuficiente")

            else:
                print("Não foi possível efetuar o saque. O valor inserido é inválido!")
        else:
            print("Você atingiu o limite de quantidades de saques diários!")

    elif opcao == 'e':
        print("================ EXTRATO ================")
        if extrato == "":
            print("Você ainda não realizou nenhuma operação no momento!")
        else:
            print(f"Saldo Disponível: R$ {saldo:.2f}\n")
            print(extrato)
        print("=========================================")

    elif opcao == 'q':
        print("Obrigado por utilizar nossos serviços!\nAté a próxima")
        break
    else:
        print("Opção inválida. Tente Novamente")
