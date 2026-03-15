import operacoes

print("""
        --------------------
            Calculadora
        --------------------
""")

while True: 

    try:
        op = float(input("digite a operacao desejada: (1)soma (2)subtracao (3)multiplicacao (4)divisao (5) sair: "))
    
        if op == 1:
            resultado = operacoes.soma(0,0)
        elif op == 2:
            resultado = operacoes.subtracao(0,0)
        elif op == 3: 
            resultado = operacoes.multiplicacao(0,0)
        elif op == 4:
            resultado = operacoes.divisao(0,0)
        else:
            break

        print(resultado)

    except ValueError:
        print("digite um numero válido")