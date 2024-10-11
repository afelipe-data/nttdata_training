menu = """

[d] Deposito
[s] Saque
[e] Extrato
[x] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado => "))
        if valor >0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Operação realizada com sucesso!\n")
        else:
            print("Falha na operação!\n Valor inválido.\n Repita a operação.\n")
    
    elif opcao == "s":
        if numero_saques < limite_saques:
            valor = float(input("Digite o valor do saque => "))
            if valor >0:
                if valor > limite:
                    print("Falha na operação!\n Valor de saque individual excedido.\n Repita a operação com um valor menor.\n")
                elif valor > saldo:
                    print("Falha na operação!\n Saldo excedido.\n Repita a operação com um valor menor.\n")

                else:
                    saldo -= valor
                    extrato += f"Saque: R$ -{valor:.2f}\n"
                    print("Operação realizada com sucesso!\n")
                    numero_saques +=1
                
            else:
                print("Falha na operação!\n Valor inválido.\n Repita a operação.\n")
        else:
            print("Falha na operação!\n Excedido o número de saques diários.\n")
    
    elif opcao == "e":
        if len(extrato) == 0:
            print("Não há registro de operações. \n")
        else:
            print("_____________________________________\n")
            print(extrato)
            print("_____________________________________\n")
            print(f"Saldo = {saldo:.2f}")
    
    elif opcao == "x":
        break

    else: 
        print("Operação inválida! \n Digite outra opção.\n")
