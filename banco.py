menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

=> """
saldo = 0
limite = 500
extrato = ""
numeroSaques = 0
LIMITES_SAQUES = 3 

while True:
    opcao = input(menu)
    if opcao == "d":
        print("-"*40)
        print("\t Depósito")
        deposito = int(input("Entre com o valor para depositar: "))
        if deposito >= 0:
            saldo += deposito
            print(f"Você depositou R${deposito:.2f}.")
            print(f"Seu saldo é de: R${saldo:.2f}")
            extrato += f" + R${deposito:.2f}\n"
        else:
            print("Não é possível depositar valores negativos.")
        print("-"*40)

    elif opcao == "s":
        print("-"*40)
        if numeroSaques < LIMITES_SAQUES:
            print("\t Sacar")
            saque = int(input("Entre com o valor para sacar: "))
            if saque > saldo:
                print(f"Seu saldo não permite um saque superior à R${saldo:.2f}.")
            elif saque > limite:
                print(f"Não foi possível realizar o saque, pois o valor excede o limite de R${limite:.2f}")
            else:
                saldo -= saque
                numeroSaques += 1
                print(f"Você realizou um saque de: R${saque:.2f}.")
                print(f"Seu saldo é de: R${saldo:.2f}")
                extrato += f" - R${saque:.2f}\n"
        else:
            print("Não é possível realizar mais saques hoje.")
        print("-"*40)

    elif opcao == "e":
        print("-"*40)
        print("\t Extrato")
        print(extrato)
        print("-"*40)

    elif opcao == "q":
        break

    else:
        print("Opção Inválida! Entre novamente com a opção correta.")