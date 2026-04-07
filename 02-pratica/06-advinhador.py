
def binary_Search(arr, item):
    baixo = 0
    alto = len(arr) - 1
    tentativas = 0
 
    while baixo <= alto: 
        meio = (baixo + alto) // 2
        chute = arr[meio]
        usuario = input(f" O numero: {chute} é (Maior),(Menor) ou acertei? (Acertou): ").lower()
        if usuario == "menor":
            baixo = meio + 1
            tentativas += 1
        elif usuario == "maior":
            alto = meio - 1
            tentativas += 1
        elif usuario == "acertou":
            tentativas += 1
            return (f"Em {tentativas} tentativas, Resultado: {chute}")
        else:
            print("Digite apenas: maior, menor ou acertou")

while True:
    arr = list(range(1,101))

    try:
        num = int(input("digite um numero de 1 a 100: "))
        if num < 1 or num > 100:
            print("digite apenas numeros entre 1 a 100")
        else:
            print(f"numero digitado: {num}")
            resultado = binary_Search(arr,num)
            print(resultado)
            break
    except ValueError:
        print("ERRO, digite apenas numeros")

