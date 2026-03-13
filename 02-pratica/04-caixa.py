
contas = {
    'admin': 1000.00,
    'visitante': 0.00
}

def consultar_saldo(usuario):
    saldo = contas[usuario]
    print(f"seu saldo atual é {saldo}!")

def depositar(usuario, valor):
    


    
    pass
def sacar(usuario, valor):
   pass


usuario_atual = 'admin'

while True:
    print(f"\n Caixa  Usuário: {usuario_atual}")
    print("(1) Consultar | (2) Depositar | (3) Sacar | (4) Sair")
    
    try:
        opcao = int(input("Opção: "))
        
        if opcao == 1:
            consultar_saldo(usuario_atual)
            
        elif opcao == 2:
            valor = float(input("Valor do depósito: "))
            depositar(usuario_atual, valor)
            
        elif opcao == 3:
            valor = float(input("Valor do saque:  "))
            sacar(usuario_atual, valor)
            
        elif opcao == 4:
            break
            
    except ValueError: 
        print("\nERRO!")