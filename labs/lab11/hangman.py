"""
Name: Sara Johnson
hangman.py

Problem: Create a Hangman game

Certification of Authenticity:
I certify that this assignment is entirely my own work
"""

from random import randint


def greeting():
    print('Lets Play Hangman!')

def read_in(file):
    infile = open(file, "r")
    words = []
    for line in infile.readlines():
        line = line.strip('\n')
        words.append(line)
    return words


def random_word(word_list):
    word_num = randint(0, len(word_list) - 1)
    picked_word = word_list[word_num]
    return picked_word

def empty_list(picked):
    pwlist_empty = []
    for n in range(len(picked)):
        pwlist_empty.append('_')
    return(pwlist_empty)


def greeting():
    print('Lets Play Hangman!')



def guess(picked, guess_letter):
    pwlist = []
    new = []
    for letter in picked:
        pwlist.append(letter)

    if guess_letter in pwlist:
        for l in pwlist:
            if l == guess_letter:
                new.append(guess_letter)
            else:
               new.append("_")
        output_str = ''.join(new)
        print(output_str)



def main():
    greeting()
    read_in('wordlist.txt')
    words = read_in('wordlist.txt')
    random_word(words)
    picked = random_word(words)
    while empty_list(picked).count('_') > 0:
        guess_letter = input("Guess a letter: ")
        guess(picked, guess_letter)



main()