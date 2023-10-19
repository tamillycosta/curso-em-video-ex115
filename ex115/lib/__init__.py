def leiaFloat(mesagem):
    while True:
        try:
            num = float(input(mesagem))
            return num
        except KeyboardInterrupt:
            print('o usuario preferiu interromper o programa')
            num = 0
            return num
        except:
            print(f'ERRO, informe um codigo valido')