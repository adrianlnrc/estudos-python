import random

def batalha_dragao():
    ataques_dragao = {
        "Sopro de Fogo": 20,
        "Patada": 10,
        "Mordida": 15
    }
    
    vida_dragao = 100
    vida_player = 60
    
    print("--- UM DRAGÃO DE OURO POUSOU NA SUA FRENTE! ---")

    while vida_player > 0 and vida_dragao > 0:
        
        try:
            ataque_player = int(input('\nEscolha o selo numeral de 1 a 3: '))
        except ValueError:
            print("Por favor, digite um número válido!")
            continue

        ataque_fera = random.randint(1, 3)

        print(f'O Dragão escolheu o selo numeral: {ataque_fera}')
        print(f'O Jogador escolheu o selo numeral: {ataque_player}')

        nome_ataque = random.choice(list(ataques_dragao.keys()))

        if ataque_player == ataque_fera:
            print('--- VOCÊ ACERTOU! ---')
            print('Você pula para o ataque e tira 30 de vida do dragão!')
            vida_dragao -= 30
        else:
            print('--- VOCÊ ERROU! ---')

            dano = ataques_dragao[nome_ataque]
            vida_player -= dano
            print(f'O Dragão usou {nome_ataque} e te causou {dano} de dano!')

        print(f'HP Player: {max(0, vida_player)} | HP Dragão: {max(0, vida_dragao)}')

    if vida_dragao <= 0:
        print('\n VITÓRIA! O Dragão de Ouro foi derrotado!')
    else:
        print('\n DERROTA... Você foi dilacerado pelo Dragão.')

batalha_dragao()