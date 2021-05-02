"""
File: boggle.py
Name:Ray lee
----------------------------------------
TODO:
"""
import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
BOGGLE_ROW = 4


# global
words = set()


def main():
	"""
	TODO: Finding all possible words in a BOGGLE_ROW*BOGGLE_ROW boggle grid
	"""
	boggle_words = []
	found = []

	if boggle(boggle_words):
		start_time = time.time()
		read_dictionary()
		prefixes = prefix_set(words)
		for i in range(len(boggle_words)):  # letting every single letter(coordinate) has been being the head
			for j in range(len(boggle_words[i])):
				visited = []
				head = boggle_words[i][j]
				boggle_finder(head,boggle_words, '', i, j, visited, prefixes, found)
		end_time = time.time()
		print(f'There are {len(found)} words in total.')
		print(f'Total spent {round((end_time-start_time),4)} second finding all possible combinations')


def boggle(boggle_words):
	"""
	:param boggle_words: empty list to store boggle letters input
	:return: if not illegal case occurred return boggle_words(list), else return False
	"""
	for i in range(BOGGLE_ROW):	# rows to enter
		letters = input(f'{i+1} row of letters: ').split()
		if len(letters) == BOGGLE_ROW: 	# check if there is any illegal format inputted
			for j in range(len(letters)):
				if len(letters[j]) != 1 or letters[j].isalpha() is False:
					print('Illegal input')
					return False
				letters[j] = letters[j].lower()
			boggle_words.append(letters)
		else:
			print('Illegal input')
			return False

	return boggle_words


def boggle_finder(head, letters, current, x, y, visited, prefixes, found):
	"""
	:param head: starting letter
	:param letters: inserted letters in the 4*4 boggle board
	:param current: current word
	:param x: current x coordinate
	:param y: current y coordinate
	:param visited: a list to record visited coordinate(x,y)
	:param found: words found
	:return: does not return, instead directly update the found(list)
	"""
	global words
	if current in words and len(current) >= 4 and current not in found:
		found.append(current)
		print(f'Found \"{current}\"')
	current += head  # update current word
	if (x, y) not in visited:  # check if visited the coordinate if so then pass
		visited.append((x, y))
		if current in prefixes:  # check the current word if it is possible to make a word, if not then pass
			for k in range(-1, 2):  # the all possible neighbors
				for l in range(-1, 2):  # the all possible neighbors
					if 0 <= x+k < len(letters) and 0 <= y+l < len(letters):  # check if it the coordinate is in the gird
						if k != 0 or l != 0:  # check if the coordinate is itself
							if (x+k, y+l) not in visited:  # check if the current coordinate is visited before
								boggle_finder(letters[x+k][y+l], letters, current, x+k, y+l, visited, prefixes, found)
								if len(visited) != 0:
									visited.pop()  # after the depth search, back one step beforehand


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global words
	with open(FILE, 'r') as f:
		for line in f:
			words.add(line.strip())


def prefix_set(dictionary):
	"""
	:param dictionary: the provided dictionary (set) of words
	:return: all possible letters combinations of words (set)
	"""
	prefixes = set(word[:i] for word in dictionary for i in range(1, len(word)+1))
	return prefixes



if __name__ == '__main__':
	main()
