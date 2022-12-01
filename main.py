from words import words,example
import random
import string
from termcolor import colored
import os
# PATRICK OWNER OF BASE HANGMAN REPOSITORY

def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def writeWins():
    file = open("match_history.txt", "a")
    file.write("You win!\n")
    file.close()
    file = open("match_history.txt", "r")
    history = file.read()
    wins = history.count("You win!")
    losses = history.count("You lose!")
    print(colored('Veces que te la has pellizcado:', 'magenta'), losses)
    print(colored('Veces que has sido digno:', 'blue'), losses)
    file.close()


def writeLosses():
    file = open("match_history.txt", "a")
    file.write("You lose!\n")
    file.close()
    file = open("match_history.txt", "r")
    history = file.read()
    wins = history.count("You win!")
    losses = history.count("You lose!")
    print(colored('Veces que te la has pellizcado:', 'magenta'), losses)
    print(colored('Veces que has sido digno:', 'blue'), losses)
    file.close() 

def borrarPantalla(): #Limpiar pantalla Dulce Badillo
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def hangman():
    # MAX ALVAREZ
    start = True  # Variable para empezar el juego al menos la primera vez
    while start:  # evalua si la variable es verdadera, en caso de que si, inicia el juego, de lo contrario lo termina
    # MAX ALVAREZ
       
        # Todo el codigo de abajo se ejecutara siempre y cuando no haya una interrupcion del teclado.
        try:
            lives = 6
            word = get_valid_word(example)
            help = 1
            word_letters = set(word)

            alphabet = set(string.ascii_uppercase)
            used_letter = set()

            while len(word_letters) > 0 and lives > 0:
                borrarPantalla() #Dulce Badillo

                print('you have used these letters: ', ' '.join(used_letter))
                user_letter = input("Guess a letter: ").upper()
                if len(user_letter) !=1 :
                    print("usa solo una letra")
                elif user_letter in alphabet - used_letter:
                    used_letter.add(user_letter)
                    if user_letter in word_letters:
                        word_letters.remove(user_letter)
                    else:
                        if help > 0:
                            print(colored("Input # to get a letter", "cyan"))
                        lives = lives - 1

                elif user_letter in used_letter:
                     print(colored('You have already used that character. Please try again.', 'yellow'))
                
                if user_letter == "#":
                    if help > 0:
                        help -= 1
                        print(colored("Try with", "blue"), colored(random.choice(word), "blue"))
                    else:
                        print(colored("You don't have any help :(", "cyan"))
                    
            # Aqui se muestra si ganaste o perdiste - Jose Pablo Gonzalez Barba
            if lives == 0:
                print(colored('Te la pelliscaste!, Nimodo. La palabra era: ', 'red'), word)
                writeLosses()
            else:
                print(colored('AHUEVO! Eres digno de poder ser amigo de ChemssDoggie!!', 'green'))
                writeWins()

            # MAX ALVAREZ --Pregunta si quiere volver a jugar o no y modifica el valor de start
            if input('Wanna play again? (Yes or No): ').upper().startswith('Y'): # Si lo que ingresa empieza con Y entonces es un Yes
                start = True
            else:
                start = False # Se modifica start, lo que afecta el while de start y finaliza el juego
            # MAX ALVAREZ
            
            # Si hay una interrupcion del teclado, se muestra este mensaje y termina el programa.
        except KeyboardInterrupt:
            print("\n\nGracias por interrumpirme cabezon, bye.")
                
    return word_letters  # MAX ALVAREZ-- Movi este return una tabulacion atras para sacarlo del while de start y que pudiese funcionar dicho while

print(hangman())