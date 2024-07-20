def remove_even(lst):
    return [num for num in lst if num % 2 != 0]

lst1 = [5, 7, 2, 4, 6 ,4, 2, 5, 8, 9]

print(remove_even(lst1))