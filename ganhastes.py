def ver_vitoria(linha1, linha2, linha3):
    finalizar: int
    finalizar = 0
    pontox = 0
    pontoo = 0
    if ('X' in linha1) or ('X' in linha2) or ('X' in linha3):
        if 'X' in linha1[0] and 'X' in linha2[1] and 'X' in linha3[2]:
            pontox += 1
        if 'X' in linha1[0] and 'X' in linha2[0] and 'X' in linha3[0]:
            pontox += 1
        if 'X' in linha1[1] and 'X' in linha2[1] and 'X' in linha3[1]:
            pontox += 1
        if 'X' in linha1[2] and 'X' in linha2[2] and 'X' in linha3[2]:
            pontox += 1
        if 'X' in linha1[2] and 'X' in linha2[1] and 'X' in linha3[0]:
            pontox += 1
        if 'X' in linha1[0] and 'X' in linha1[1] and 'X' in linha1[2]:
            pontox += 1
        if 'X' in linha2[0] and 'X' in linha2[1] and 'X' in linha2[2]:
            pontox += 1
        if 'X' in linha3[0] and 'X' in linha3[1] and 'X' in linha3[2]:
            pontox += 1
    if ('O' in linha1) or ('O' in linha2) or ('O' in linha3):
        if 'O' in linha1[0] and 'O' in linha2[1] and 'O' in linha3[2]:
            pontoo += 1
        if 'O' in linha1[0] and 'O' in linha2[0] and 'O' in linha3[0]:
            pontoo += 1
        if 'O' in linha1[1] and 'O' in linha2[1] and 'O' in linha3[1]:
            pontoo += 1
        if 'O' in linha1[2] and 'O' in linha2[2] and 'O' in linha3[2]:
            pontoo += 1
        if 'O' in linha1[2] and 'O' in linha2[1] and 'O' in linha3[0]:
            pontoo += 1
        if 'O' in linha1[0] and 'O' in linha1[1] and 'O' in linha1[2]:
            pontox += 1
        if 'O' in linha2[0] and 'O' in linha2[1] and 'O' in linha2[2]:
            pontox += 1
        if 'O' in linha3[0] and 'O' in linha3[1] and 'O' in linha3[2]:
            pontox += 1
    if pontox == 1:
        finalizar = 1
    elif pontoo == 1:
        finalizar = 1
    return finalizar, pontox, pontoo
