import sys


def take_args():
	argv = sys.argv
	if len(argv) == 1:
		return 1
	if len(argv) != 2:
		print("AssertionError: more than one argument is provided")
		return 1
	try:
		number = int(argv[1])
		if number % 2 :
			print("I'm Odd.")
		else:
			print("I'm Even.")
	except:
		print("AssertionError: argument is not an integer")



take_args()
