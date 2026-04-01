consumo_agua = {
    "adrian": 0,
    "maria clara": 0,

}

meta_diaria = 2000

def registrar_agua(nome,quantidade):
    consumo_agua[nome] += quantidade 
    total_consumido = consumo_agua[nome]
    print(f" foi adicionado {quantidade} ml,  total {total_consumido}")

def exibir_total():
    print("Status da meta")

    for nome, total_ml in consumo_agua.items():
        if total_ml >= meta_diaria:
            print(f"parabens, a meta {meta_diaria} foi batida: {total_ml}")
        else: 
            faltam = meta_diaria - total_ml
            print(f"ainda falta pouco para bater a meta {meta_diaria}, total ingerido {total_ml} ")
        print(f" {nome}: {total_ml}")
    


while True: 
    print("=" * 40)
    print("Contador de Agua")
    print("=" * 40)
    print("(1) Adicionar Agua ingerida")
    print("(2) Exibir total de Agua ingerida")
    print("(3) sair")

    try:
        op = int(input("Qual opcao:"))

        if op == 1:
            nome = input("De quem voce quer registrar: ".lower())
            quantidade = int(input("quantos ml foram ingeridos? "))
            registrar_agua(nome,quantidade)
        
        elif op == 2: 
            exibir_total()
        
        else: 
            print("valeu!")
            break





    except ValueError:
        print("ERRO, selecione uma das opçoes")






