from typing import Any

def callLimit(limit: int):
	count = 0
	def callLimiter(function):
		def limit_function(*args: Any, **kwds: Any):
			nonlocal count
			if count < limit:
				count +=1
				res = function(*args, **kwds)
			else:
				res = "Error: " + repr(function) + " call too many times"
				print(res)
				return None
			return res
		return limit_function
	return callLimiter