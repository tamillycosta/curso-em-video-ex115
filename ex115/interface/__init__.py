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

def pintar_menu():
    linha('Menu Principal',tudo=True)
    print('1- Ver pessoas cadastradas')
    print('2- Cadastrar uma nova pessoa')
    print('3- Sair')
    linha(tudo=False)



def LeiaINT(mensagem):
    while True:
        try:
            num = int(input(mensagem))
            if num == 1:
                time.sleep(0.5)
                linha('OPÇÃO 1', tudo=True)
                pintar_menu()

            if num == 2:
                time.sleep(0.5)
                linha('OPÇÃO 2', tudo=True)
                pintar_menu()

            else:
                if num == 3:
                    linha('SAINDO DO SISTEMA ... ATÉ LOGO')
                    return num

        except  (TypeError,ValueError):
            print('ERRO, informe um codigo valido')
        except KeyboardInterrupt:
            print('o usuario encerreou bruscamente o programa')



def cadastros(dado):
    pass









