
def binary_Search(arr):
    baixo = 0
    alto = len(arr) - 1
    tentativas = 0
 
    while baixo <= alto: 
        meio = (baixo + alto) // 2
        chute = arr[meio]
        tentativas += 1
        num_usuario = input(f"O meu chute foi {chute}. O seu número é (Menor), (Maior) ou (Acertou)? ").lower()
        if num_usuario == "maior":
            baixo = meio + 1
        elif num_usuario == "menor":
            alto = meio - 1
        elif num_usuario == "acertou":
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
            resultado = binary_Search(arr)
            print(resultado)
            break
    except ValueError:
        print(f"ERRO , digite apenas numeros")

