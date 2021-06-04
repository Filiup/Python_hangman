from constants import *
from functions import *

run = True
word = choice(RANDWORDS)
word_auxiliary = word
word_hidden = HideWord(word, revealed_chars(word))
mistakes = 0

def game():
    global word_hidden, mistakes, run, word_auxiliary

    # Z pomocnej premennej word_auxiliary odstránime písmená ktoré sa nacádzajú v skrytom slove
    # Robíme to kvôli tomu lebo  uživateľ uź dané písmená neháda keďže mu už boli ukázané
    # Príklad: 
        # keď word = "Filip" a word_hidden = "_i_i_" tak word_auxiliary = F_l_p

    word_hidden_chars = [index for index, letter in enumerate(word_hidden) if letter.isalpha()]
    for letter_index in word_hidden_chars:
        word_auxiliary = word_auxiliary[:letter_index] + "_" + word_auxiliary[letter_index+1:]

    print(colorize(Fore.CYAN ,word_hidden)) 

    user_guess = CheckInput("Typni si písmenko: ")

    if user_guess in word_auxiliary: # Uhádli sme správne písmeno 
        char_index = word_auxiliary.find(user_guess) # Zistime, ktore písmenko sme uhádli
        word_hidden = word_hidden[:char_index] + user_guess + word_hidden[char_index+1:] # Písmenko ktoré sme uhládli pridáme do word_hidden
        print(colorize(Fore.LIGHTGREEN_EX, "Správne !"))

        # Z pomecnej premennej word_auxiliary odstránime písmeno, ktoré sme uhádli
        # Robíme to kvôli tomu aby sa v pomocnej premennej word_auxiliary nemohlo vyskytnúť znova 
        # (V podmienke sa pýtame že či sa písmeno ktoré si typol uživateľ nacháza v word_auxiliary)

        # Príklad:
            # Keď máme napríklad slovo "Erik" a uhádnem "k" tak sa premenná word_auxialary zmení na "Eri_" 
        word_auxiliary = word_auxiliary.replace(user_guess, "_", 1)

        # Pokiaľ sa skryté slovo rovná vybranému slovu tak sme vyhrali  
        if word_hidden == word:
            print(colorize(Fore.GREEN, "\nVyhral si !!!!!!"))
            print(colorize(Fore.GREEN, "Šikovný/á si, chválim ťa :)"))
            run = False

    else: # Neuhádli sme správne písmeno 
        mistakes += 1 
        print(HANGMAN[mistakes - 1])
        print(colorize(Fore.RED, "Zlý typ !"))

        # Pokiaľ spravíme 7 chýb tak sme už prehrali 
        if mistakes == 7:
            print(colorize(Fore.RED, "Tvoj počet pokusov vypršal, prehral si ! :("))
            print(colorize(Fore.RED, f"Správne slovo bolo: {colorize(Fore.GREEN, word)}"))
            run = False


def mainloop():
    while run:
        game()
              
if __name__ == '__main__':
    mainloop()
    