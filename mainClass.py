import time

def limparTela():
    print(chr(27) + "[2J")

saldoLista = []
operacaoLista = []

def histExtrato(valor, operacao):
    if valor > 0:
        saldoLista.append(valor)
        operacaoLista.append(operacao)

def MainMenu():
    textoOp = '''
    Selecione o número da opção desejada:
    1 - Extrato
    2 - Deposito
    3 - Saque
    '''

    print("***** Banco Guarani *****\n")
    print(textoOp)

    op = input("Nº Opção: ")

    match op:
        case '1':
            extrato()
        case '2':
            deposito()
        case '3':
            saque()
        case _:
            print("Opção invalida")
            time.sleep(2)
            limparTela()
            MainMenu()

def extrato():
    limparTela()

    textoDesc = '''
    -- Extrato

    Exibindo todas as operações bancarias efetuadas:
    '''

    print(textoDesc)

    for i in range(len(operacaoLista)):
        print(f"Operação: {operacaoLista[i]} = Saldo: R$ {saldoLista[i]:.2f}")

    print("Pressione qualquer tecla para retornar ao menu principal...")
    input("")
    MainMenu()

def deposito():
    limparTela()
    
    textoDesc = '''
    -- Despósito
    Q - Voltar ao menu principal.

    Primeiro digite o valor em Reais a ser depositado em sua conta e logo em seguida os centavos:
    '''

    print(textoDesc)
    
    valorString = input("Valor: ")

    if valorString != 'q' and valorString != 'Q':

        centavosString = input("Centavos: ")

        print(f"O valor a ser depositado é de R${valorString},{centavosString}\nEstá correto?")
        confirma = input("S (Sim), N (Não): ")
    
        if confirma == "s" or confirma == 'S':
            valorFinal = valorString + "." + centavosString
            valor = float (valorFinal)
            histExtrato(valor, "Deposito")
            limparTela()
            print("Deposito efetuado com sucesso!")
            time.sleep(3)
            limparTela()
            MainMenu()

        elif confirma == 'n' or confirma == 'N':
            limparTela()
            deposito()

        else:
            print("Opção invalida")
            time.sleep(2)
            limparTela()
            deposito()

    else:
        limparTela()
        MainMenu()

def saque():
    limparTela()

    textoDesc = '''
    -- Saque
    Q - Voltar ao menu principal.

    Primeiro digite o valor em Reais a ser sacado de sua conta e logo em seguida os centavos:
    '''

    print(textoDesc)

    valorString = input("Valor: ")

    if valorString != 'q' and valorString != 'Q':

        centavosString = input("Centavos: ")

        print(f"O valor a ser sacado é de R${valorString},{centavosString}\nEstá correto?")
        confirma = input("S (Sim), N (Não): ")

        if confirma == "s" or confirma == 'S':
            valorFinal = valorString + "." + centavosString
            valor = float(valorFinal)
            if valor <= 500 and len([i for i in operacaoLista if i == "Saque"]) < 3:
                histExtrato(-valor, "Saque")
                limparTela()
                print("Saque efetuado com sucesso!")
                time.sleep(3)
                limparTela()
                MainMenu()
            else:
                print("Limite de saque excedido.")
                time.sleep(2)
                limparTela()
                MainMenu()

        elif confirma == 'n' or confirma == 'N':
            limparTela()
            saque()

        else:
            print("Opção invalida")
            time.sleep(2)
            limparTela()
            saque()

    else:
        limparTela()
        MainMenu()

#Inicia o programa
MainMenu()
