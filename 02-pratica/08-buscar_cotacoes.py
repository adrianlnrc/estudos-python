import requests 

# Requisitando dados através da biblioteca requests, sendo utilizada com os métodos get, put, delete, head, options

url = "https://assessorialpha.com/"

mascara = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

dados = requests.get(url,headers=mascara)

if dados.status_code == 200:
    print(f'Sucesso na entrada do Site {url}')
    print(f"Quantidade de dados recebida em caracteres: {len(dados.text)}")

    print(f"primeiros duzentos caracteres da pagina:")
    print(dados.text[:200])
else:
    print(f"O site barrou, status code: {dados.status_code}")







