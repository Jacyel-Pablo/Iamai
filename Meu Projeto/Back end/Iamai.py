from os import startfile
from random import randint
from googlesearch import search

# Inicio do codigo

criado = str('Jacyel Pablo')
Iamai = str('Iamai')

print(f'Todos os direitos resevados a {criado}\nSeja bem vindo ao sistema {Iamai}')

nome = str(input('Porfavor insira seu nome:\n')).lower()

if nome in ['jacyel pablo', 'jacyel', 'jacyel pablo lopes de moura']:
    print('Seja-bem vindo senhor')

else:
    print(f'Meu Deus uma pessoa nova que legal prazer ter conhece {nome}\nVamos ser amigos')
    amigos = str(input('s/n\n')).lower()
    if amigos in ['s', 'sim', 'si', 'sm']:
        print(f'Que legal meu novo amigo {nome}\nSeu nome é muito bonito')
    else:
        print('Que pena quem saber você não muda de ideia')

while True:
    oque_voce_gostaria = str(input('Oque você gostaria de fazer:\n')).lower()

# abrindo bloco de notas

    if oque_voce_gostaria in ['bloco de notas', 'notepad', 'bloco de nota', 'nopad', 'abrir bloco de notas', 'iamai abra o bloco de notas', 'ok iamai abra o bloco de notas']:
        print('Abrindo bloco de notas')
        startfile('notepad')

# Abrindo o Word

    if oque_voce_gostaria in ['word', 'winword', 'abrir word', 'abrir word', 'abrir o word', 'iamai abra o word', 'ok iamai abra o word']:
        print(f'Ok {nome.title()}\nAbrindo o Word')
        startfile('WINWORD.EXE')

# Abrindo Microsoft edge

    if oque_voce_gostaria in ['abrir microsoft edge', 'microsoft edge', 'abra o microsofr edge', 'iamai abra o microsoft edge', 'navegado edge']:
        print('Ok abrindo Microsoft Edge')
        startfile('msedge.exe')

# Gerador de senha

    if oque_voce_gostaria in ['gerador de senha', 'gerar senha', 'senha', 'gerar numeros', 'gerar numeros', 'numeros aleatorios', 'gerado de senhar', 'gerador de senha', 'gerado de numeros']:
        numeroal = randint(1, 20), randint(1, 20), randint(1, 20), randint(1,20), randint(1, 20), randint(1, 20)
        print(f'O numero gerador foi {numeroal}')

# Pesquisa na web

    if oque_voce_gostaria in ['pesquisa', 'web broser', 'pesquisa na web', 'pesquise isso para mim', 'pesquise isso para mim pf', 'fassa uma pesquisa na web', 'web pesquisa']:
        pesquisa = str(input('Ok vamos pesquisa algo na web\nDigite algo para pesquisa:\n'))
        pesquisa1 = list(
            search(
                pesquisa,
                lang = 'pt-br',
                num_results = 5
            )
        )
        print(f'Esse é o resultado do que eu achei na web {pesquisa1}')

    if oque_voce_gostaria in ['sair', 'fecha o progama', 'fecha', 'exit', 'termina', 'quero sair']:
        sair = input(f'Aperter entre para sair\nEspero ter ver de novo {nome.title()}')
        exit()