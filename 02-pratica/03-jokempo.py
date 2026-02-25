# random Library
import random

Jokempo = ['pedra','papel','tesoura']

iniciar = 1

while iniciar == 1:
    print('------Jokempo--------')
    print(Jokempo)
    tentativa = input('escolha um dos três: ').lower()
    print('------------------------------')
    computador = random.choice(Jokempo)

    print(f'JOGADOR: {tentativa} x COMPUTADOR: {computador}')
    # possibilidades onde o jogador ganha
    if tentativa == 'pedra' and computador == 'tesoura':
        print(f'Parabéns, você ganhou')
    elif tentativa == 'papel' and computador == 'pedra':
        print('Parabéns, Você ganhou')
    elif tentativa == 'tesoura' and computador == 'papel':
        print('Parabéns, você ganhou')
    # possibilidades que o computador ganha
    if tentativa == 'tesoura' and computador == 'pedra':
        print(f'Perdeu')
    elif tentativa == 'pedra' and computador == 'papel':
        print('Perdeu')
    elif tentativa == 'papel' and computador == 'tesoura':
        print('Perdeu')
    # Empate
    elif tentativa == computador:
        print('empate')
    
    iniciar = int(input('\n jogar novamente (1) ou jogar novamente (0)'))