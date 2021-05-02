"""
File: complement.py
Name:
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    The programme will found the minimum complement of the inserted DNA sequence.
    """
    while True:
        dna = input('please give me a DNA strand and I\'ll find the complement: ').upper()
        if dna.isalpha() is False:
            print('the DNA strand is invalid, please recheck')
        else:
            new_dna = build_complement(dna)
            print('The complement of '+dna+' is '+new_dna)
            break

def build_complement(dna):
    ans = ''
    for base in dna:
        if base == 'A':
            ans += 'T'
        elif base == 'T':
            ans += 'A'
        elif base == 'G':
            ans += 'C'
        elif base == 'C':
            ans += 'G'
    return ans

###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
