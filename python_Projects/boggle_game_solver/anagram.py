"""
File: anagram.py
Name:Ray Lee
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global
words = {}  # store all words from the dictionary


def main():
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        if find_anagrams(input('Find anagrams for: ').lower()) == '-1':
            break


def read_dictionary():
    global words
    with open(FILE, 'r') as f:
        for line in f:
            line = line.strip('\n')
            words[line] = 1


def find_anagrams(s):
    """
    :param s:
    :return: if input(s) == '-1', stop case
    """

    if s != '-1':
        start = time.time()
        co = [0]  # counter
        found = []  # words found
        read_dictionary()
        print('Searching...')
        anagrams_finder(list(s), '', found,co)
        print(f'{len(found)} anagrams: {found}')
        print(co)
        end = time.time()
        print(f'總花費搜尋時長: {round(end-start,4)}秒')
    else:
        return s


def anagrams_finder(target, current, found,co):
    co[0] += 1
    global words
    if len(target) == 0:
        if current in words:
            if current not in found:
                found.append(current)
                print(f'Found: {current}')
                print('Searching...')
    else:
        for i in range(len(target)):
            # choose
            alphabet = target.pop(0)
            current += alphabet
            # explore
            # if has_prefix(current):
            anagrams_finder(target, current, found, co)
            # un-choose
            current = current[:-1]
            target.append(alphabet)


def has_prefix(sub_s):
    """
    :param sub_s: current substring
    :return: If there is any words with prefix stored in sub_s
    """
    global words
    if len(sub_s) >= 1:
        for word in words:
            if word.startswith(sub_s) is True:
                return True





if __name__ == '__main__':
    main()
