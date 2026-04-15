
pontuacoes = [150, 24, 79, 312, 5, 99]


def busca_maior(arr):
    maior = arr[0]
    maior_indice = 0

    for i in range(1, len(arr)):
        if arr[i] > maior:
            maior = arr[i]
            maior_indice = i
    return maior_indice


def SelectionSort(arr):
    nova_lista = []
    for i in range(len(arr)):
        maior = busca_maior(arr)
        nova_lista.append(arr.pop(maior))
    return nova_lista

    
teste_buscaMaior = busca_maior(pontuacoes)
print(teste_buscaMaior)

lista_baguncada = [1,55,22,95,31,59,23,77,58,14,21]
teste_SelectionSort = SelectionSort(lista_baguncada)


