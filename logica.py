menu = """ 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    
    opcao = input(menu)
    


    if opcao == "d":
        
        deposito = float(input("Digite o valor a ser depositado: "))
        
        if deposito >= 0:
            saldo += deposito
            extrato += f'valor depositado R${deposito:.2f}\n'
            
        elif deposito < 0:
            print("O número informado deve ser diferente de zero")
            
        else:
            print("informe um número positivo para depósito")
        
    elif opcao == "s":
        
            numero_saque = float(input("valor numero_saque a realizar: "))
            
            if numero_saque > saldo:
                print("saldo insuficiente para saque")
                
            elif numero_saque > limite:
                print(f'Limite máximo de saque excedido a {limite}')
            
            elif numero_saque < 0:
                print("Numero informado delve ser diferente de zero")
                
            elif LIMITE_SAQUE > 0:
                for index in range(LIMITE_SAQUE):
                    saldo -= numero_saque
                    LIMITE_SAQUE -= 1
                    extrato += f'valor sacado R${numero_saque:.2f}\n'
                    
                    break
            else:
                print( "Limite de saque diário excedido ")
        
    elif opcao == "e":
        print(f'{extrato}\n'+ f'R$Saldo:{saldo:.2f}')
        
    elif opcao == "q":
        break
    
    else:
        print("Opçao inválida")