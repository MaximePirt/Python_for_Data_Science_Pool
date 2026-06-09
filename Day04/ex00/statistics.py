
# Standard Deviation and Variance

def check_args(*args) -> list:
	if len(args) == 0:
		print("ERROR")
		return
	res = []
	for i in args:
		if not type(i) is int:
			print("Not a number :", i)
			raise TypeError()
		res.append(i)
	res.sort()
	return res

def mean_calc(args):
	res = sum(args) / len(args)
	return res

def median_calc(args):
	l = len(args)
	res = []
	if l % 2:
		l += 1	
	l //= 2
	res = args[l - 1]
	return l - 1

def quartile(args):
	# Get first median
	median = median_calc(args)
	quart = []
	median_tab = args[0:-median]
	# calculate first quartile
	quart1 = median_calc(median_tab)
	quart.append(median_tab[quart1])
	# calculate last quartile
	last_med_tab = args[median:]
	quart3 = median_calc(last_med_tab)
	quart.append(last_med_tab[quart3])

	print("quartile : ", quart)

def variance_calc(args):
	mean = mean_calc(args)
	tmp_var = []
	for i in args:
		tmp_var.append((i - mean) ** 2)
	
	variance = sum(tmp_var)
	variance = variance / len(args)
	return variance





def ft_statistics(*args: Any, **kwargs: Any) -> None:
	for i, value in kwargs.items():
		num = check_args(*args)
		if num :
			match value:
				case "mean":
					res = mean_calc(num)
					print("mean :", res)
				case "median":
					res = median_calc(num)
					print("median :", num[res])
				case "quartile":
					quartile(num)
				case "std":
					deviation = variance_calc(num)
					deviation = deviation ** (1/2)
					print("std : ", deviation)
				case "var":
					variance = variance_calc(num)
					print("var :", variance)
				case _:
					pass