def depositar(saldo, extrato):
    print('Deposito')
    valor = (float(input('Digite o valor que deseja depositar: R$')))
    if (valor > 0):
        saldo += valor
        extrato += (f'Depósito: R${valor:.2f}\n')
        print(f'O valor de R${valor} foi depositado na sua conta')
    else:
        print('Valor inválido')
    return saldo, extrato

def sacar(saldo, extrato, numero_saques):
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
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print(extrato if extrato else 'Nenhuma movimentação realizada.')
    print(f'Saldo atual: R${saldo:.2f}')

def criar_usuario(usuarios):
    cpf = (int(input('Digite o CPF: ')))
    if cpf in usuarios:
        print('Usuário já cadastrado')
        return usuarios

    nome = (str(input('Digite o nome: '))).strip()
    data_nascimento = (str(input('Digite a data de nascimento (dd/mm/aaaa): '))).strip()
    endereco = (str(input('Digite o endereço: '))).strip()

    usuarios[cpf] = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    }

    print('Usuário Cadastrado com Sucesso')
    return usuarios

def listar_usuarios(usuarios):
    if not usuarios:
        print('Não há usuários cadastrados')
        return
    for cpf, dados in usuarios.items():
        print(f"{cpf}: {dados}")

menu =  """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar Usuário
[l] Listar Usuários
[q] Sair
=> """

usuarios = {}
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == 's':
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques)
 
    elif opcao == 'e':
        exibir_extrato(saldo, extrato)
    
    elif opcao =='c':
        usuarios = criar_usuario(usuarios)

    elif opcao =='l':
        listar_usuarios(usuarios)

    elif opcao == 'q':
        print('Sair')
        break

    else:
        print('Operação Inválida')