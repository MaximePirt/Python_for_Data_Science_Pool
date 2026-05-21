

def check_type(arg_list: list[int | float]) -> int:
    try:
        for i in arg_list:
            float(i)
            int(i)
    except:
        print("TypeError : argument is neither an int or a float")
        return 1

def bmi_parsing(arg1: list[int | float], arg2: list[int | float]) -> int:
    if check_type(arg1) or check_type(arg2):
        return 1
    if len(arg1) != len(arg2):
        print("ValueError: List 1 and 2 needs to be same sizes")
        return 1


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
        Input : list [int | float] & list [int | float]
        This function calculate BMI from given height and weight lists
        Return list of BMI results
    """    
    if bmi_parsing(height, weight):
        return 1
    res = list()
    lst_len = len(height)
    i = 0
    while i < lst_len:
        bmi = weight[i] / (height[i] * height[i]) 
        res.append(bmi)
        i += 1
    
    return res

    #  Formule: BMI (IMC) = poids / taille(m)².



def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if check_type(bmi):
        return 1
    try:
        int(limit)
    except:
        print("TypeError : argument is not an int")
        return 1

    res = list()
    lst_len = len(bmi)
    i = 0
    while i < lst_len:
        if bmi[i] > limit:
            res.append(bool(True))
        else:
            res.append(bool(False))
        i += 1
    return res