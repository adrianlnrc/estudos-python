supermercado = {
    "limpeza":{"detergente": 2.0,"amaciante": 20,"sabao em po": 16.90},
    "Acouque":{"alcatra:": 45.90, "patinho moido": 42.90,"peito de frango": 20.00},
    "padaria":{"pao": 14.90, "rosca": 5.00, "pizza": 29.90},

}

def ver_secoes():
    print("\nSeções disponíveis")
    for s in supermercado:
        print(s)

def ver_produtos(secao):
    print(supermercado[secao].items())



while True:
    print("=" * 20)
    print("Bem vindo ao supermercado girassol")
    print("=" * 20)

    try:
        op = int(input("digite a opcao: (1) ver secoes (2) ver produtos (3) Sair -- "))
        
        if op == 1:
            ver_secoes()
        
        elif op == 2:
            secao = input("de qual secao deseja ver os produtos? ")
            ver_produtos(secao)
        else:
            print("Obrigado, volte sempre")
            break

            
            



    except ValueError:
        print("Erro, digite apenas numeros na pagina principal")
