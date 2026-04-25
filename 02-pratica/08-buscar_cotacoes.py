import requests 

resposta = requests.get('https://github.com/adrianlnrc') # transformando resposta em um objeto Response

# Pegando todo tipo de retirada de informação do objeto 

print("Codigo HTML da página:",resposta.text) #.text retorna o código HTML 

print("Status da conexão",resposta.status_code) # verificar a conexão




