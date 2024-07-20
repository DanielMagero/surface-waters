def intersection_members(lst1, lst2):
    for item in lst1:
        if item in lst2:
            return True
    return False

lst1 = [4, 6, 7 , 9]
lst2 = [6, 8, 2, 1]

print(intersection_members(lst1, lst2))