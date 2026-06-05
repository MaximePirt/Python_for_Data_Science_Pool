

class calculator:
	''' Calculator class creation '''
	@staticmethod
	def dotproduct(V1: list[float], V2: list[float]) -> None:
		''' Print result of the sum of V1[x] by V2[x] x len'''
		res = [x * y for x, y in zip(V1, V2)]
		res = sum(res)
		print("Dot product is :", res)
		return res

	@staticmethod
	''' Print addition result of v1[x] and v2[x] for x len'''
	def add_vec(V1: list[float], V2: list[float]) -> None:
		res = [float(x + y) for x, y in zip(V1,V2)]
		print("Add vector is :", res)
		return res

	@staticmethod
	def sous_vec(V1: list[float], V2: list[float]) -> None:
	''' Print substraction result of v1[x] and v2[x] for x len'''
		res = [float(x - y) for x, y in zip(V1,V2)]
		print("Sous Vector is:", res)
		return res
