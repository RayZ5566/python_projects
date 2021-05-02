"""
File: largest_digit.py
Name:Ray Lee
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: a given integer
	:return: the maximum number in the integer
	"""
	return helper(abs(n))


def helper(number):
	if number // 10 == 0:
		return number
	else:
		return max(number % 10, helper(number//10))





if __name__ == '__main__':
	main()
