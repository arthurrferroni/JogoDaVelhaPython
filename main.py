from desenha import Desenhar
from escreve import escrever
from ganhastes import ver_vitoria
from ver_input import inicia
linha1 = [" ", " ", " "]  # Vetor que guarda os dados da Linha 1 do jogo da velha (linha superior)
linha2 = [" ", " ", " "]  # Vetor que guarda os dados da Linha 2 do jogo da velha (linha central)
linha3 = [" ", " ", " "]  # Vetor que guarda os dados da Linha 3 do jogo da velha (linha inferior)
jogada: int
jogada = 1
finaliza = [0, 0, 0]
erro: int
erro = 1
iz: int
iz = 1
while iz != 0:
    try:
        player = int(input("Você quer jogar de [1] Player ou [2] Players? "))
        if player == 2:
            simbolo = inicia()
            Desenhar(linha1, linha2, linha3)
            while not finaliza[0] == 1:
                jogada += 1
                while erro != 0:
                    erro = escrever(linha1, linha2, linha3, simbolo)
                if simbolo == "X":
                    simbolo = "O"
                else:
                    simbolo = "X"
                finaliza = ver_vitoria(linha1, linha2, linha3)
                if jogada == 9:
                    finaliza = 1
                Desenhar(linha1, linha2, linha3)
                erro = 1
                iz = 0
                print(finaliza)
        else:
            if player == 1:
                print("Não ta pronto")
                iz = 0
            else:
                print("Numero invalido")
                iz = 1
    except ValueError:
        print("Valor invalido.")
        iz = 1
if finaliza[1] > finaliza[2]:
    print("O X ganhou.")
elif finaliza[2] > finaliza[1]:
    print("O O ganhou.")
else:
    print("Deu velha.")
