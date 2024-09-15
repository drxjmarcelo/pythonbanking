menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":

        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo+= valor
            extrato +- f"Deposito: RS$ {valor:.2f}\n"

        else:
            print("ERRO! O valor digitado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("ERRO! Saldo insuficiente")

        elif valor > limite:
            print(f"ERRO! Você só pode efetuar saques até: R$ {limite:.2f}")
        
        elif numero_saques >= LIMITE_SAQUES:
            print("ERRO! Limite de saque excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            numero_saques += 1

    elif opcao == "e":
        print("\n############### Extrato ###############")
        print("Não foi realizada nenhuma movimentação." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("#######################################")
    
    elif opcao == "q":
        break

    else:
        print("Operacao invalida, por favor selecione novamente a operação desejada.")