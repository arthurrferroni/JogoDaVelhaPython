def escrever(linha1, linha2, linha3, simbolo):
    escolhe = int(input("Escolha uma posição: "))
    if escolhe < 4:
        if escolhe > 1:
            if escolhe == 3:
                if 'X' not in linha1[2] and 'O' not in linha1[2]:
                    linha1.pop(2)
                    linha1.insert(2, simbolo)
                    erro = 0
                else:
                    erro = 1
                    print('Posição já usada. Por favor escolha outra')
            elif escolhe == 2:
                if 'X' not in linha1[1] and 'O' not in linha1[1]:
                    linha1.pop(1)
                    linha1.insert(1, simbolo)
                    erro = 0
                else:
                    erro = 1
                    print('Posição já usada. Por favor escolha outra')
        elif escolhe == 1:
            if 'X' not in linha1[0] and 'O' not in linha1[0]:
                linha1.pop(0)
                linha1.insert(0, simbolo)
                erro = 0
            else:
                erro = 1
                print('Posição já usada. Por favor escolha outra')
    if escolhe < 7:
        if escolhe > 4:
            if escolhe == 6:
                if 'X' not in linha2[2] and 'O' not in linha2[2]:
                    linha2.pop(2)
                    linha2.insert(2, simbolo)
                    erro = 0
                else:
                    erro = 1
                    print('Posição já usada. Por favor escolha outra')
            elif escolhe == 5:
                if 'X' not in linha2[1] and 'O' not in linha2[1]:
                    linha2.pop(1)
                    linha2.insert(1, simbolo)
                    erro = 0
                else:
                    erro = 1
                    print('Posição já usada. Por favor escolha outra')
        elif escolhe == 4:
            if 'X' not in linha2[0] and 'O' not in linha2[0]:
                linha2.pop(0)
                linha2.insert(0, simbolo)
                erro = 0
            else:
                erro = 1
                print('Posição já usada. Por favor escolha outra')
    if escolhe < 10:
        if escolhe > 7:
            if escolhe == 9:
                if 'X' not in linha3[2] and 'O' not in linha3[2]:
                    linha3.pop(2)
                    linha3.insert(2, simbolo)
                    erro = 0
                else:
                    erro = 1
                    print('Posição já usada. Por favor escolha outra')
            elif escolhe == 8:
                if 'X' not in linha3[1] and 'O' not in linha3[1]:
                    linha3.pop(1)
                    linha3.insert(1, simbolo)
                    erro = 0
                else:
                    erro = 1
                    print('Posição já usada. Por favor escolha outra')
        elif escolhe == 7:
            if 'X' not in linha3[0] and 'O' not in linha3[0]:
                linha3.pop(0)
                linha3.insert(0, simbolo)
                erro = 0
            else:
                erro = 1
                print('Posição já usada. Por favor escolha outra')
    return erro
