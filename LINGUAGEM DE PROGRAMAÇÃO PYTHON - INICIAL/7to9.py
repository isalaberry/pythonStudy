#importando módulos
from math import sqrt
print(sqrt(25))

#criando um módulo e importando ele
import meumodulo_7
meumodulo_7.saudacao("Isabel")

#strings---------------------------------------------------------------------
texto1='parede'
texto2="amarela"

'''
print(texto1[0])
print(texto1[1])
'''
print('.........................')
print(texto1)
print(texto2)
print('.........................')
print(texto1[0:4])
print(texto1[4:6])
print(texto2[0:4])
print(texto2[4:7])
print('.........................')
print(texto1[0:4].upper())
print(texto1[4:6].upper())
print(texto2[0:4].upper())
print(texto2[4:7].upper())
print('.........................')

#formatação de strings
nome='Isabel'
idade=21
fraseformat='Meu nome é {} e tenho {} anos.'.format(nome, idade)
print(fraseformat)

nome='Isabel'
idade=21
frasefstrings=f'Meu nome é {nome} e tenho {idade} anos.'
print(frasefstrings)


#manipulação de arquivos
arquivo=open('arquivo.txt','r')
conteudo=arquivo.read()
print(conteudo)
arquivo.close()

arquivo=open('arquivo.txt','w')
arquivo.write('Escrevendo nesse arquivo aqui.')
arquivo.close()

#anexar 'a'
arquivo=open('arquivo.txt','a')
arquivo.write('Anexando esse texto ao arquivo.')
arquivo.close()

arquivo=open('arquivo.txt','r')
conteudo=arquivo.read()
print(conteudo)
arquivo.close()