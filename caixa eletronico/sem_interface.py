
def depositar(saldo):
    valor = float(input("\ndigite o valor a ser depositado: "))
    saldo += valor
    print("\n\n Deposito realizado")
    return saldo


def ver_saldo(saldo):
    print(f"\n\n Seu saldo é {saldo}")

def sacar(saldo):
    valor = float(input("\ndigite o valor a ser sacado: "))
    if valor <= saldo:
        saldo-=valor
        print("\n\n saque realizado")
    else:
        print("\nSaldo insufficiente")

    return saldo

def caixa_eletronico():
    saldo = 0.0
    opcao = ""

    while opcao != "sair":
        print("\n=== Caixa Eletrônico ===")
        print("Opções: [d] Deposito")
        print("Opções: [s] Sacar")
        print("Opções: [v] Ver Saldo")
        print("Opções: [sair] Encerrar")
        
        opcao = input("\nEscolha uma opção: ").lower()

        if opcao == "d":
            saldo = depositar(saldo)
        
        elif opcao == "s":
            saldo = sacar(saldo)

        elif opcao == "v":
            ver_saldo(saldo)

        elif opcao == "sair":
            print("\noperacao encerrada")
            break
        else:
            print("\nopcao invalida")

caixa_eletronico()