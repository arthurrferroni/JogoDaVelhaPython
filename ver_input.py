def inicia():
    i: int
    i = 0
    while i != 1:
        simbolo = input("Escolha X ou O: ")
        simbolo = simbolo.upper()
        if simbolo == 'X':
            i += 1
        elif simbolo == 'O':
            i += 1
        else:
            print("Escolha o simbolo certo.")
    return simbolo
