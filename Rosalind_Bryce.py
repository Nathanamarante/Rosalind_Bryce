## Rosalind problem solving arquive ##

import os

## Python Village ##
#INI3
string1 = 'DvcPJY2pkEtPantheraFxfCfZSHhbaHPHKf5ACwUHWK2X0Nx9aWFtWaU7XqM7q5jSGs5J0J39BfNvQKPKqIKiMnyP4fr4qE6JZUrKspaldingiOIcaawyJvdP0ZpW4jd8PdMQRIxGnH6fyqyfjZVcDiOWJEbc6lr5.'
print (string1[11:18+1])
print (string1[101:109+1])

## INI4 
a= 4556
b= 9403
c= (a < b < 10000)
soma=0

resultado = sum(i for i in range(a, b + 1) if i % 2 != 0)
print(resultado)

## INI5
base_diretorio = os.path.dirname(os.path.abspath(__file__))
arquivo = os.path.join(base_diretorio, 'rosalind_ini5.txt')

with open(arquivo, 'r', encoding='utf-8') as f:
    linhas = f.readlines()
    for numero, linha in enumerate(linhas, start=1):
        if numero % 2 == 0:
            print(linha.rstrip('\r\n'))

## INI6
print(f"\nINI6: ")
from collections import Counter #Buscado em documentação

def contar_palavras(s: str) -> dict[str, int]: #Função criada para contagem de palavras, é esperado uma string e a contagem de ocorrências
    palavras = s.split()
    return dict(Counter(palavras))

ini_6 =  "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
ini_6_resultado = contar_palavras(ini_6)

for palavra, quantidade in ini_6_resultado.items():
    print(palavra, quantidade)
