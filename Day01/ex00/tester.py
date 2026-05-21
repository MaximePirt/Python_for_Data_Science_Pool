from give_bmi import give_bmi, apply_limit

#Parsing tests

#Too much arg1
arg1 = [1, 2, 3]
arg2 = [1, 2]
test1 = give_bmi(arg1, arg2)
print("Result test 1:", test1)
#Expected output : ValueError: List 1 and 2 needs to be same sizes

print("-------------")

# Arg no int or float
arg1 = [1, "test", 3]
test2 = give_bmi(arg1, arg2)
print("Result test2:", test2)
#Expected output : TypeError : argument is neither an int or a float

print("-------------")

#Subject test
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

print("-------------")


# Arg no int in apply_limit
arg = "test3"
print("Result test3:", apply_limit(bmi, arg))

#Expected output : TypeError : argument is not an int

