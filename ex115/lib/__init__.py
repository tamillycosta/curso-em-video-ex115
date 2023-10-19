from ex115.interface import *

def Cria_arquivo():
    nome_arquivo = "curso-em-video"
    with open('curso-em-video','w') as arquivo:
        print(f'o arquivo {nome_arquivo} foi criado')
        return arquivo

def mostra_arquivo():
    arquivo = open('curso-em-video', 'r')
    lista = arquivo.readlines()
    for linha in lista:
        partes = linha.strip().split()
        if len(partes) == 2:
            nome, idade = partes
            print(f'Nome: {nome.ljust(20)}',end='')
            print(f'IDADE: {idade}')


def input_arquivo():
    lista = []
    while True:
        nome = input('nome: ')
        idade = input('idade: ')
        if idade.isdigit():
            with open("curso-em-video", "a") as arquivo:
                arquivo.write(f"{nome} {idade}\n")
            print(f'{nome} com idade {idade} foi adicionado ao arquivo.')
            break
        else:
            print('Erro, informe uma idade válida.')













