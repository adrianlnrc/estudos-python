import time 
import random
pontuacoes = [random.randint(1, 5_000_001) for _ in range(5_000_001)]


def busca_maior(arr):
    maior_numero = 0
    for elemento in arr:
        if elemento > maior_numero:
            maior_numero = elemento

    return maior_numero

inicio = time.time()

resultado = busca_maior(pontuacoes)

final = time.time()
print(resultado)

print(f"o tempo de execucao foi de {final - inicio:.6f}")