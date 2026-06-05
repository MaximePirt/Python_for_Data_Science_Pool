class calculator:
	''' Calculator class creation '''

	def __init__(self, vector):
		self.vector = vector

	def __add__(self, object) -> None:
		self.vector = [object + x for x in self.vector]
		print(self.vector)
	def __mul__(self, object) -> None:
		self.vector = [object * x for x in self.vector]
		print(self.vector)

	def __sub__(self, object) -> None:
		self.vector = [object - x for x in self.vector]
		print(self.vector)

	def __truediv__(self, object) -> None:
		try: 
			if object == 0:
				raise ZeroDivisionError("Cannot divided by 0")
			self.vector = [object / x for x in self.vector]
			print(self.vector)
		except ZeroDivisionError as err:
			print(err, ": " + ZeroDivisionError.__name__)