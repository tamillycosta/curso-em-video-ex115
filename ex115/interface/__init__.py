import time

from ex115.lib import *
from time import sleep
def linha(mensagem='',tudo=True):
  mensagem = mensagem.center(33)

  if tudo == True:
      print('~' * 40)
      print(F"  {mensagem}")
      print('~' * 40)
  else:
     so_linha = '~' * 40
     print(so_linha)

def pintar_menu(lista):
    cont=0
    linha('Menu Principal',tudo=True)
    for p in lista:
        cont += 1
        print(f'{cont} - {p}')
    linha(tudo=False)
    opcao = LeiaINT('sua opção: ')
    return opcao



def LeiaINT(mensagem=''):
    while True:
        try:
            num = int(input(mensagem))
        except (TypeError,ValueError):
            print('ERRO, informe um codigo valido')
        except KeyboardInterrupt:
            print('o usuario encerreou bruscamente o programa')
        else:
            return num










