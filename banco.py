def menu ():
    print("""
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Criar Usuário
    [v] Vincular Conta Corrente à um usuário
    
    [q] Sair

    """)
    return input("=> ")

def depositar(deposito, saldo, extrato, /):
    if deposito >= 0:
        saldo += deposito
        print(f"Você depositou R${deposito:.2f}.")
        print(f"Seu saldo é de: R${saldo:.2f}")
        extrato += f" + R${deposito:.2f}\n"
    else:
        print("Não é possível depositar valores negativos.")
    return saldo, extrato

def sacar(*, saque, limite, saldo, extrato, numeroSaques):
    if saque > saldo:
        print(f"Seu saldo não permite um saque superior à R${saldo:.2f}.")
    elif saque > limite:
        print(f"Não foi possível realizar o saque, pois o valor excede o limite de R${limite:.2f}")
    else:
        saldo -= saque
        print(f"Você realizou um saque de: R${saque:.2f}.")
        print(f"Seu saldo é de: R${saldo:.2f}")
        extrato += f" - R${saque:.2f}\n"
        numeroSaques += 1
    return saldo, extrato, numeroSaques

def extratos(saldo,/, *, extrato):
    print("-"*40)
    print("\t Extrato")
    print(extrato)
    print(f"\nSaldo: R${saldo}")
    print("-"*40)

def criar_usuario(usuarios):
    cpf = input("Entre com o CPF: ")
    user = filtragem(cpf, usuarios)

    if user:
        print("Este CPF já foi cadastrado! Tente novamente.")
        return
    
    nome = input("Entre com o Nome: ")
    endereco = input("Entre com o Endereço (logradouro, num - bairro - cidade/sigla do Estado): ")
    dataNascimento = input("Entre com a Data de Nascimento (dd-mm-aaaa): ")

    usuarios.append({"cpf": cpf, "nome": nome, "endereço": endereco, "data": dataNascimento})

def filtragem(cpf, usuarios):
    usuario_filtrado = []
    for user in usuarios:
        if user["cpf"] == cpf:
            usuario_filtrado.append(user)

    if usuario_filtrado:
        return usuario_filtrado[0]
    else:
        None

def criar_contaCorrente(agencia, num_conta, usuarios):
    cpf = input("Entre com o CPF: ")
    user = filtragem(cpf, usuarios)

    if user:
        print("Conta vinculada com sucesso!")
        return {"agencia":agencia, "num_conta":num_conta, "user": user}  
    print("Usuário não encontrado. Tente novamente!")

def main():
    num_conta = 1
    usuarios = []
    contas = []
    saldo = 0
    limite = 500
    extrato = ""
    numeroSaques = 0
    LIMITES_SAQUES = 3 
    AGENCIA = "0001"

    while True:
        opcao = menu()
        if opcao == "d":
            print("-"*40)
            print("\t Depósito")
            deposito = float(input("Entre com o valor para depositar: "))
            saldo, extrato = depositar(deposito, saldo, extrato)

        elif opcao == "s":
            print("-"*40)
            print("\t Sacar")
            saque = float(input("Entre com o valor para sacar: "))

            if saque <= 0:
                print("Entre com um valor possível!")
                continue

            if numeroSaques < LIMITES_SAQUES:
                saldo, extrato, numeroSaques = sacar(
                    saldo = saldo,
                    extrato = extrato,
                    limite = limite,
                    saque = saque,
                    numeroSaques = numeroSaques
                )
            else:
                print("Não é possível realizar mais saques hoje.")
            print("-"*40)

        elif opcao == "e":
            extratos(saldo, extrato = extrato)

        elif opcao == "c":
            criar_usuario(usuarios)

        elif opcao == "v":
            conta = criar_contaCorrente(AGENCIA, num_conta, usuarios)

            if conta:
                contas.append(conta)
                num_conta += 1

        elif opcao == "q":
            break

        else:
            print("Opção Inválida! Entre novamente com a opção correta.")

main()
