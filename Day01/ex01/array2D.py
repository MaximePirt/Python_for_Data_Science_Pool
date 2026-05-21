import numpy as np



def parsing(family: list, start: int, end: int) -> int:
    try:
        int(start)
        int(end)
        list(family)
    except:
        print("TypeError : One argument is not an int a float or a list")
        return 1
    return 0




def slice_me(family: list, start: int, end: int) -> list:
    if parsing(family, start, end):
        return 1
    a = np.array(family)
    print("My shape is", a.shape)

    a = a[start:end]

    print("My new shape is", a.shape)
    return a.tolist()