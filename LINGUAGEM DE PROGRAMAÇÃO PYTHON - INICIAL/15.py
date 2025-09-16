
# converter json para python (dict)
print("----------------------------------------------------------------------")
import json
dados = '{"nome": "Isabel", "idade": 21, "cidade": "São Paulo"}'
json_dados = json.loads(dados)
print(json_dados)

# python (dict) para json
print("----------------------------------------------------------------------")
dados = {"nome": "Isabel", "idade": 21, "cidade": "Curitiba"}
json_dados = json.dumps(dados)
print(json_dados)

#lendo um arquivo.csv
print("----------------------------------------------------------------------")
import csv
import os
caminho = os.path.join(os.path.dirname(__file__), 'dados.csv')
with open(caminho, mode='r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        print(linha)

#convertendo json para csv
print("----------------------------------------------------------------------")
json_dados = '[{"nome": "Isabel", "idade": 21, "cidade": "Brasilia"}, {"nome": "João", "idade": 30, "cidade": "Rio de Janeiro"}]'
dados = json.loads(json_dados)

print("Conteúdo do JSON a ser escrito no CSV:")
for dado in dados:
    print(dado)

with open('dados.csv', mode='w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(['Nome', 'Idade', 'Cidade'])
    print("\nEscrevendo no arquivo dados.csv:")
    for dado in dados:
        escritor_csv.writerow([dado['nome'], dado['idade'], dado['cidade']])
print("\nArquivo dados.csv criado/atualizado com sucesso!")
