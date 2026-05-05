import sys
from ft_filter import ft_filter

class ArgException(Exception):
	"""Exception which return AssertionError + personnalised error """
	def __init__(self, message):
		self.message =  "AssertionError: " + message
	def __str__(self):
		return "Invalid character in string"

def give_string(S, N):
	""" Main subject function which compare S len with N"""
	return len(S) > N
	

def parse_arguments(S, N):
	""" This function check args type and content before sending to give_string"""
	try:
		N = int(N)
		if not type(S) == str:
			raise ArgException("Bad entry, arg one is not a string")
		if not type(N) == int:
			raise ArgException("Bad entry, arg two is not an int")
		parseing = [x for x in S if not (x == ' ' or x.isalpha())]
		if len(parseing):
			raise ArgException("Invalid character in string :" + str(parseing))
		S = list(S.split())
		print(ft_filter(lambda x : give_string(x, N), S))
	except (Exception, ArgException) as e:
		if not (type(N)) == int:
			print("AssertionError: Bad entry, arg two is not an int")
		else:
			print(e)
		return 




def main():
	"""Main function here to parse prompt arguments then launch filtering"""
	argv = sys.argv


	if len(argv) != 3:
		print("AssertionError: two arguments are provided, no more no less")
		return 1
	parse_arguments(argv[1], argv[2])
	return 0

if __name__ == "__main__":
	main()


# TODO: BE CAREFUL ABOUT ERROR MESSAGE WHICH CAN ONLY BE : AssertionError: the arguments are bad