# Recode your own ft_filter, it should behave like the original built-in function
# (it should return the same thing as "print(filter.__doc__)"), you should use list comprehensions to recode your ft_filte


def ft_filter(func, iterable: any):
	''' copy of real filter() function in python
		-- iterate value by function
	'''
	if func is None:
		newlist = [value for value in iterable if bool(value)]
	else :
		newlist = [value for value in iterable if bool(func(value))]
	return newlist



# def is_even(n):
#     return n % 2 == 0

# def test(n):
# 	return n

# def is_a(c):
#     return c == "a"

# # This test is supposed to crash
# # print("test0")
# # print(ft_filter(3, [1, 2, 3]))
# # print(list(filter(3, [1, 2, 3])))


# print("test1")
# print((ft_filter(None, [0, 1, "", "x", [], [1], None, True, False])))
# print(list((filter(None, [0, 1, "", "x", [], [1], None, True, False]))))


# print("test2")
# print((ft_filter(is_a, "abracadabra")))
# print(list((filter(is_a, "abracadabra"))))

# print("test3")
# print((ft_filter(test, [0, 1, 2, 0, 3])))
# print(list((filter(test, [0, 1, 2, 0, 3]))))


# print("test4")
# print((ft_filter(is_even, [1, 2, 3, 4, 5, 6])))
# print(list((filter(is_even, [1, 2, 3, 4, 5, 6]))))
