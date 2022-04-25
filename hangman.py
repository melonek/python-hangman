import random
from words import list_of_words

def get_word():
    word = random.choice(list_of_words)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed - False
    guessed_letters = []