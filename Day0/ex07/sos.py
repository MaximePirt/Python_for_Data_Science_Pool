import sys

ESTED_MORSE = { " ": "/ ",
				"A": ".-", "B": "-...", "C": "-.-.",
				"D": "-..", "E": ".", "F": "..-.",
				"G": "--.", "H": "....", "I": "..",
				"J": ".---", "K": "-.-", "L": ".-..",
				"M": "--", "N": "-.", "O": "---",
				"P": ".--.", "Q": "--.-", "R": ".-.",
				"S": "...", "T": "-", "U": "..-",
				"V": "...-", "W": ".--", "X": "-..-",
				"Y": "-.--", "Z": "--..",
				"1": ".----", "2": "..---", "3": "...--",
				"4": "....-", "5": ".....", "6": "-....",
				"7": "--...", "8": "---..", "9": "----.",
				"0": "-----"
				}






def main():
	"""Main function here to parse prompt arguments then create answer list"""
	argv = sys.argv

	dico = ESTED_MORSE
	if len(argv) != 2:
		print("AssertionError: the arguments are bad")
		return 1
	answer = list()
	for i in argv[1]:
		if not i.isalnum() and not i == ' ':
			print("AssertionError: the arguments are bad")
			return
		answer.append(dico[i.upper()])
	
	print(*answer)
	return 0

if __name__ == "__main__":
	main()
