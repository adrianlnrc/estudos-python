import requests 
from bs4 import BeautifulSoup as bs

# Requisitando dados através da biblioteca requests, sendo utilizada com os métodos get, put, delete, head, options

url = "https://assessorialpha.com/"
mascara = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

dados = requests.get(url,headers=mascara)
statusDaRequisicao = dados.status_code
sopa = bs(dados.text, 'html.parser')
slogan = sopa.find("h2")

if dados.status_code == 200:
    print(f'Sucesso na entrada do Site {url}')
        # print(f"Quantidade de dados recebida em caracteres: {dados.text}")
    print(f"Slogan da página: {slogan.text.strip()}")

    #print(f"primeiros duzentos caracteres da pagina: {dados.text[:200]}")
   
else:
    print(f"O site barrou, status code: {dados.status_code}")

servicos = [] # servicos oferecidos

cabecalhos = sopa.find_all(["h2","h3"])

for item in cabecalhos:
    texto_limpo = item.text.strip()
    if len(texto_limpo) > 5: 
        servicos.append(texto_limpo)

print(f"empresa com slogan: {slogan}")

for i in servicos:
    print(f"serviço {servicos}")
        





