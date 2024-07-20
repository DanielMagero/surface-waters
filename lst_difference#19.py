def lst_diff(lst1, lst2):
    return [item for item in lst1 if item not in lst2]

lst1 = ["a", "h", 6, 7 , 5]
lst2 = [7, 4, 6, "h"]

print(f"The difference in the two lists is {lst_diff(lst1, lst2)}")