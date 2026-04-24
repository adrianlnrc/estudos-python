import requests 

resposta = requests.get('https://github.com/adrianlnrc')

print("Status da conexão",resposta.status_code) # verificar a conexão

print("Codigo HTML da página:",resposta.text) #.text retorna o código HTML 


