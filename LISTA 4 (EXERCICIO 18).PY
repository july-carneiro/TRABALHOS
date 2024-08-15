#JOGO PEDRA, PAPEL E TESOURA

import random
def jogar():
    opcoes=['pedra','papel','tesoura']

    jogada=input("Escolha pedra,papel ou tesoura:").lower()

    if jogada not in opcoes:
        print("Escolha inválida, tente novamente.")
        return
    jogadamaquina= random.choice(opcoes)
    print (f'Você escolheu:{jogada}')
    print(f'A Máquina escolheu{jogadamaquina}')
    if jogada==jogadamaquina:
        print('Empate!')
    elif (jogada =='pedra' and jogadamaquina =='tesoura') or (jogada== 'papel'and jogadamaquina =='pedra') or (jogada=='tesoura'and jogadamaquina=='papel'):
        print('Você venceu!')
    else:
        print('Você perdeu!')

        