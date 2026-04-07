

def binary_Search(arr, item):
    baixo = 0
    alto = len(arr) - 1
 
    while baixo <= alto: 
        meio = (baixo + alto) // 2
        chute = arr[meio]
        usuario = input(f"numero:{chute} (Maior) (Menor) (Acertou)".lower())
        if usuario == "maior":
            baixo = meio + 1
        elif usuario == "menor":
            alto = meio -1
        else:
            return (f" Acertei, seu numero: {num},  meu chute {chute}")
        ...


while True:
    arr = list(range(1,101))

    try:
        num = int(input("digite um numero de 1 a 100: "))
        if num < 1 or num > 100:
            print("digite apenas numeros entre 1 a 100")
        else:
            print(num)
            
        resultado = binary_Search(arr,num)
        print(resultado)
        break


    

    
    except ValueError:
        print("ERRO, digite apenas numeros")

