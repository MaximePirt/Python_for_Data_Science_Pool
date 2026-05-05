def NULL_not_found(object: any) -> int:
	match(object) :
		case None:
			print("Nothing: None <class 'NoneType'>")
		case float() as x if x != x:
			print("Cheese: nan <class 'float'>")
		case bool(False) :
			print("Fake: False <class 'bool'>")
		case str(""):
			print("Empty: <class 'str'>")
		case int(0) :
			print("Zero: 0 <class 'int'>")
		case _:
			print("Type not Found")
			return 1
	return 0
