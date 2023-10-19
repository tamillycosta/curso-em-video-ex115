from ex115.interface import *
from ex115.lib import *
cont = 0

while True:
    cont += 1
    if cont < 1:
        Cria_arquivo()
    opcao = pintar_menu(['Dados De Usuários', 'Cadastrar Novo Usuario', 'Sair'])
    if opcao == 1:
        time.sleep(0.5)
        linha('PESSOAS CADASTRADAS', tudo=True)
        mostra_arquivo()
    elif opcao == 2:
        time.sleep(0.5)
        linha('CADASTRO DE PESSOAS', tudo=True)
        input_arquivo()
    elif  opcao == 3:
        linha('SAINDO DO SISTEMA ... ATÉ LOGO')
        break
    else:
        print('ERRO,informe uma opção valida')




