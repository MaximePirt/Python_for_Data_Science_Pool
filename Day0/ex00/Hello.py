ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#List 
ft_list[1] = 'World!'


#Tuple - immutable so need convertion
tmp_tuple = list(ft_tuple)
tmp_tuple[1] = 'France!'
ft_tuple = tuple(tmp_tuple)


#Set - unordered
ft_set.add("Angoulême!")
ft_set.remove("tutu!")

#Dict
ft_dict["Hello"] = '42Angoulême!'

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

