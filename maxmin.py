def maxmin(list):
    high = list[0]
    low = list[0]
    for n in list:
        if n > high:
            high = n
        elif n < low:
            low = n
    return [low, high]
