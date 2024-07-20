import random

def shuffle_lst(lst1):
    random.shuffle(lst1)
    return lst1

lst = ["w", "t", 5 ,6 ,"f" ,"y"]

print(shuffle_lst(lst))