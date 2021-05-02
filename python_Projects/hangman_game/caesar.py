"""
File: caesar.py
Name:
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    TODO: This will decipher the sentence
    """
    cipher = int(input('Secret Number: '))
    d_string = input('What\'s the ciphered string? ').upper()
    deciphered = decipher(d_string, cipher)
    print('The deciphered string is : ' + deciphered)


def decipher(d_string, cipher):
    """
    :param d_string: string, sentence to be deciphered
    :param cipher:int, steps of ALPHABET shifted
    :return: deciphered string
    """
    d_alpha = ALPHABET[-cipher:]+ALPHABET[:-cipher]   # create the decipher alphabet
    deciphered_str = ''  # deciphered string
    for i in d_string:
        if i.isalpha():  # if i is alphabet then decipher or concat to string directly
            n = d_alpha.find(i)
            deciphered_str += ALPHABET[n]
        else:
            deciphered_str += i
    return deciphered_str


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
