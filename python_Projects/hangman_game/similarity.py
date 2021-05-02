"""
File: similarity.py
Name:
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    The programme will find the part in the given strand with the highest similarity with the strand inputted.
    """
    l = input('Please give me a DNA sequence to search: ').upper()
    s = input('What DNA sequence would you like to match? ').upper()
    best, similarity = homology(l, s)
    print('The best match is ' + best)
    print('The similarity is ' + str(similarity * 100) + '%')


def homology(long_sequence, short_sequence):
    """
    :param long_sequence: str, the sequence to be compared
    :param short_sequence: str, the comparing sequence
    :return:
    """
    l = long_sequence  # shorten the parameter
    s = short_sequence  # shorten the parameter
    long_l = len(long_sequence)
    short_l = len(short_sequence)
    similarity = 0
    best = ''  # record the part with highest similarity
    for i in range(long_l - short_l + 1):
        adj_l = l[i:i + short_l]  # adjust the length of long sequence equals to short sequence
        correct = 0  # record the number of same factors
        for j in range(short_l):
            if adj_l[j] == s[j]:
                correct += 1
        part_similarity = correct / short_l  # calculate the similarity for each part
        if part_similarity > similarity:
            similarity = part_similarity  # record the highest similarity percentage
            best = adj_l  # record the part with the highest similarity
    return best, similarity


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
