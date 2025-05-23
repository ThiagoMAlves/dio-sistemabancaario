menu =  """

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

    if opcao == 'd':
        print('Deposito')
        d = (float(input('Digite o valor que deseja depositar: R$')))
        if (d > 0):
            saldo += d
            print(f'O valor de R${d} foi depositado na sua conta')
            extrato += (f'Depósito: R${d:.2f}\n')
        else:
            print('Valor inválido')

    elif opcao == 's':
        if (numero_saques == LIMITE_SAQUES):
            print('Limite de saques diário excedido')
        else:
            saque = (float(input('Digite o valor que deseja sacar: R$')))
            if saque <= saldo and saque <= 500 and saque > 0:
                numero_saques += 1
                saldo -= saque
                print(f'O valor de R${saque} foi sacado de sua conta')
                extrato += (f'Saque: R${saque:.2f}\n')
            else:
                print('Valor Inválido')
 
    elif opcao == 'e':
        print(f'Extrato:\n',extrato)
        print(f'Saldo: R${saldo:.2f}')

    elif opcao == 'q':
        print('Sair')
        break

    else:
        print('Operação Inválida')