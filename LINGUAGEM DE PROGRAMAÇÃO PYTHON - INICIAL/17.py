import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
resposta = requests.get(url)
soup = BeautifulSoup(resposta.text, 'html.parser')

titulos = soup.find_all('h1')
for titulo in titulos:
    print(titulo.get_text())

#manipular os dados em um dataframe
import pandas as pd
dados = {
    'Nome': ['Isabel', 'João', 'Maria'],
    'Idade': [28, 34, 22],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}
df = pd.DataFrame(dados)
print(df)

#filtrando dados
print("--------------Filtrando dados--------------")
df_sp = df[df['Cidade'] == 'São Paulo']
print(df_sp)