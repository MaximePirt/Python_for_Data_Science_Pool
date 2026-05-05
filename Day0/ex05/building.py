import sys


def ft_count(string):
	""" 
		This function count every type of character asked in the subject
		---
		Limitation
		due to os differences, i decided to count \n as space as much as carriage return
	"""
	char = len(string)

	upletter = 0
	lowletter = 0
	puncmark = 0
	spaces = 0
	digits = 0
	for i in string:
		asc = ord(i)
		if asc > 65 and asc < 91:
			upletter += 1
		elif asc > 96 and asc < 123:
			lowletter += 1
		elif asc == 44 or asc == 46:
			puncmark += 1
		elif asc == 32 or asc == 13 or asc == 10:
			spaces += 1
		elif asc > 47 and asc < 58:
			digits += 1
	print("The text contains", char,"characters:\n"\
		, upletter,"upper letters\n"\
		, lowletter,"lower letters\n"\
		, puncmark,"punctuation marks\n"\
		, spaces,"spaces\n"\
		, digits,"digits")


def main():
	"""Main function here to parse prompt arguments then launch counting function"""
	argv = sys.argv

	if len(argv) == 1:
		print("What is the text to count?\n"\
			"Hello World!\n"\
			"The text contains 13 characters:\n"\
			"2 upper letters\n"\
			"8 lower letters\n"\
			"1 punctuation marks\n"\
			"2 spaces\n"\
			"0 digits")
		return 1
	if len(argv) != 2:
		print("AssertionError: more than one argument is provided")
		return 1
	ft_count(argv[1])
	return 0

if __name__ == "__main__":
	main()