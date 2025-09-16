import requests

#realizar uma requisição get
print("--------------Requisição GET--------------")
resposta = requests.get('https://jsonplaceholder.typicode.com/todos/1')
if resposta.status_code == 200:
    dados = resposta.json()
    print(dados)
else:
    print(f"Erro ao acessar a API: {resposta.status_code}")

#realizar uma requisição post
print("--------------Requisição POST--------------")
url = 'https://jsonplaceholder.typicode.com/posts'
dados = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
resposta = requests.post(url, json=dados)
if resposta.status_code == 201:
    print("Postagem criada com sucesso!")
else:
    print(f"Erro ao criar postagem: {resposta.status_code}")

#web scraping
print("--------------Web Scraping--------------")
url = 'https://example.com'
resposta = requests.get(url)
if resposta.status_code == 200:
    conteudo = resposta.text
    print(conteudo)
else:
    print(f"Erro ao acessar a página: {resposta.status_code}")