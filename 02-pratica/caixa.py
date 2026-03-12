
contas = {
    "admin": 100.0,
    "teste": 500.0,
}


def consultar_saldo(usuario):
    saldo = contas["admin"]

print(consultar_saldo("admin"))
    
def depositar(usuario):
    ...

usuario_atual = "admin"
while True:
    print(f"Bradesco: Bem vindo usuario: {usuario_atual} ")
    print("(1)consultar saldo (2) depositar")

    try:
        opcao = int(input("Opção:"))

        if opcao == 1:
            consultar_saldo(usuario_atual)
        
        elif opcao == 2:
            valor = int(input("Digite o valor a ser depositado"))
            depositar(usuario_atual,valor)



    except ValueError:
        print("Erro")
        
