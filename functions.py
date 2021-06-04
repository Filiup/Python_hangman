from random import randint, sample, choice
from colorama import Fore, Style

def HideWord(word, number_of_revealed_chars = 2):
    number_of_hidden_chars = len(word) - number_of_revealed_chars
    hidden_chars = "".join(sample(word, number_of_hidden_chars))
    for i in hidden_chars:
        word = word.replace(i, "_", 1)

    return word


def CheckInput(messenge):
    user_input = input(messenge)

    while len(user_input) > 1 or user_input.isalpha() == False:
        user_input = input(messenge)

    return user_input

    
def revealed_chars(word):
    if len(word) <= 3:    chars = 0
    elif len(word) <= 5:  chars = 1
    elif len(word) <= 8:  chars = 2
    elif len(word) <= 11: chars = 3
    else:                 chars = 4

    return chars

def colorize(color, text):
    return color + text + Style.RESET_ALL 

