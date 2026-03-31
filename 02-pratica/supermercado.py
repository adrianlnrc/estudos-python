supermercado = {
    "limpeza":{"Detergente": 2.0,"Amaciante": 20,"Sabao em po": 16.90},
    "acougue":{"Alcatra": 45.90, "Patinho moido": 42.90,"Peito de frango": 20.00},
    "padaria":{"Pão": 14.90, "Rosca": 5.00, "Pizza": 29.90},

}


def exibir_secoes():
    for s in supermercado:
        print(s)

def exibir_produtos(secao):
    print(f"os produtos da secao: {secao}")
    for produto, valor in supermercado[secao].items():
        print(f'{produto} Valor R$ {valor}')
    
while True:
    print("=" * 35)
    print("Bem vindo ao supermercado girassol")
    print("=" * 35)
    print("(1) Ver todas as secoes")
    print("(2) Ver produtos de uma seção")
    print("(3) Sair")

    try:
        op = int(input("digite a opcao: "))
        
        if op == 1:
            exibir_secoes()
        
        elif op == 2:
            exibir_secoes()
            secao = input("de qual secao deseja ver os produtos? ".lower())
            exibir_produtos(secao)
            if secao in supermercado:
                exibir_produtos(secao)
            else:
                print("Secão nao encontrada!")
        elif op == 3:
            print("Obrigado, volte sempre!")
            break 
        else:
            print("Opção inválida, Escolha 1,2 ou 3")

    except ValueError:
        print("Erro, digite apenas numeros na pagina principal")
