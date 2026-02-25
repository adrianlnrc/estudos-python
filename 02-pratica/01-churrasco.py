homens = int(input('digite quantos homens vao ao churrasco'))
mulheres = int(input('digite quantas mulheres'))
criancas = int(input('digite quantas criancas'))

# consumo aproximado em gramas por pessoa
homens *= 400
mulheres *= 300
criancas *= 200

total_de_carne = homens + mulheres + criancas
# converter de gramas para quilogramas
quantidade_comprar = total_de_carne / 1000

# exibir com 2 casas decimais e calcular +10% inline
print(f"Quantidade sem acréscimo: {quantidade_comprar:.2f} kg")
print(f"Quantidade com 10% de margem: {quantidade_comprar * 1.10:.2f} kg")