def menu():
    menu = """ 

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair

    """

    return input(menu)

def deposito_cliente(deposito, saldo, extrato):
            
    if deposito >= 0:
        saldo += deposito
        extrato += f'valor depositado R${deposito:.2f}\n'
        
    elif deposito < 0:
        print("O número informado deve ser diferente de zero")
        
    else:
        print("informe um número positivo para depósito")
        
    return saldo, extrato
                
def extrato_cliente(saldo, /, *, extrato):
    print(f"{extrato}\nSaldo R${saldo}")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Já existe usuário com este CPF")
        return
    nome = input("informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dia-mes-ano): ")
    endereco = input("Informe o endereco (logradouro, n° - bairro - cidade/UF): ")
    
    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf" == cpf]]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def sacar(*,saldo, valor, extrato, limite, numero_saque, limite_saque):
    if valor > saldo:
        print("saldo insuficiente para saque")
                
    elif valor > limite:
        print(f'Limite máximo de saque excedido a {limite}')
    
    elif valor < 0:
        print("Numero informado delve ser diferente de zero")
        
    elif limite_saque > numero_saque:
        for index in range(limite_saque):
            saldo -= valor
            limite_saque -= 1
            extrato += f'valor sacado R${valor:.2f}\n'
            break
        
    else:
        print( "Limite de saque diário excedido ")
    
    return saldo, extrato

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado, fluxo de criação de conta encerrado")

def listar_contas(contas):
    for conta in contas:
        print(f'''\
            Agência: {conta['agencia']}
            C/C:     {conta['numero_conta']}
            Titulas: {conta['usuario']['nome']}
        ''')

def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0
    usuarios = []
    contas = []
    while True:
        
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("Digite o valor a ser depositado: "))
            saldo, extrato = deposito_cliente(valor, saldo, extrato)
            
        elif opcao == "s":
            
            valor = float(input("valor numero_saque a realizar: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato, 
                limite=limite,
                numero_saque=numero_saque, 
                limite_saque=LIMITE_SAQUE,
            )
            
        elif opcao == "e":
            extrato_cliente(saldo, extrato=extrato)
        
        elif opcao == 'nu':
            criar_usuario(usuarios)
        
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if opcao == "nc":
                contas.append(conta)
        elif opcao == 'lc':
            listar_contas(contas)
            
        elif opcao == "q":
            break
        
        else:
            print("Opçao inválida")

main()      
