def append_lst(lst1, lst2):
    lst1.extend(lst2)
    return lst1


lst1 = ["q", "g", "u"]
lst2 = [3, 7, 8, 0]

print(f"The combined list is: {append_lst(lst1, lst2)}")