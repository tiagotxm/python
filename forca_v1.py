# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word

    # Método para adivinhar a letra
    def guess(self, letter):
        if letter in self.word:
            return True
        else:
            return False


    # Método para verificar se o jogo terminou
    def hangman_over(self,palavraFinal,qtd_erro):

        if self.word == palavraFinal:
            return True
        elif self.word != palavraFinal or qtd_erro == 6:
            return False

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        return True

    # Método para não mostrar a letra no board
    def hide_word(self):
        palavraOculta = '-' * len(self.word)
        print("PALAVRA: ",palavraOculta)
        return palavraOculta

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self,posicao):
        print(board[posicao])

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())
    qtd_erro=0
    letras_erradas=[]

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter

    # Verifica o status do jogo
    game.print_game_status(0)

    palavraOculta = list(game.hide_word())

    while(qtd_erro < 6):


        letra = input('Digite uma letra: ')
        existe_letra = game.guess(letra)

        if existe_letra == True:
            game.print_game_status(qtd_erro)

            for indice,valor in enumerate(game.word):
                if letra in valor:
                    #print(indice)
                    palavraOculta[indice]=letra

            palavraFinal ="".join(palavraOculta)
            print(palavraFinal)
            fim = game.hangman_over(palavraFinal,qtd_erro)

            if fim == True:
                # De acordo com o status, imprime mensagem na tela para o usuário
                if game.hangman_won():
                    print('\nParabéns! Você venceu!!')
                    break

        else:
            print(palavraFinal)
            letras_erradas.append(letra)
            print('\nLetras erradas digitadas:')
            for i in letras_erradas:
                print(i)

            qtd_erro += 1
            game.print_game_status(qtd_erro)

            if qtd_erro == 6:
                print('\nGame over! Você perdeu.')
                print('A palavra era ' + game.word)
                print('\nFoi bom jogar com você! Agora vá estudar!\n')







# Executa o programa
if __name__ == "__main__":
    main()
