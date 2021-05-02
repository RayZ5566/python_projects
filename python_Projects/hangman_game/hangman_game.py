"""
File: hangman.py
Name: Ray Lee
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Hangman game
    """
    ans = random_word()
    hangman(ans)


def hangman(ans):
    """
    :param ans:str, the correct answer of the hangman
    :return: the result of the hangman
    """
    left = len(ans) * '-'  # record changes after each guess
    chances = N_TURNS  # chances left
    while True:     # loop of hangman
        print('The word looks like: ' + left)
        print('Your have ' + str(chances) + ' guesses left.')
        guess = input('Your guess: ').upper()
        if len(guess) != 1 or guess.isalpha() is False:  # check if the guess is legal format
            print('illegal format')
        else:
            temp = ''   # empty string to record this guess
            count = 0
            for i in range(len(ans)):
                if guess == ans[i] and left[i] == '-':
                    temp += guess
                elif guess == ans[i] and left[i].isalpha():
                    temp += guess
                elif guess != ans[i] and left[i].isalpha():
                    temp += left[i]
                    count += 1
                else:
                    temp += '-'
                    count += 1
                    if count == len(ans):
                        print('There is no '+guess+'\'s in the word.')
                        chances -= 1
            left = temp
            hangman_p(chances)
            if left == ans:
                print('You are correct!\nYou won!!')
                print('The word was: '+ans)
                break
            elif chances == 0:
                print('you are completely hung QAQ!')
                print('The word was: ' + ans)
                break


def hangman_p(c):
    """
    :param c: int, chances left can make a guess
    :return: the pic of hangman
    """
    print('"""""""')
    if c <= N_TURNS-1:
        print(' | ')
    if c <= N_TURNS-2 and c != 0:
        print(' O ')
    if c == 0:
        print(' X ')
    if c <= N_TURNS-5 or c == 0:
        print('/I\\ ')
    elif c <= N_TURNS-4 or c == 0:
        print(' I\\')
    elif c <= N_TURNS-3 or c == 0:
        print(' I ')
    if c <= N_TURNS-6 or c == 0:
        print('/ \\')
    if c == 0:
        print('!!you dead!!')
    print('"""""""')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
