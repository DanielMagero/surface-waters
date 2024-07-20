#MUGULO DANIEL MAGERO M24B38/017


#LISTS


#2
#multiply all items in the list
def multiply_lst(num):
    ans = 1
    for number in num:
        ans *= number
    return ans

num = [2, 7, 8, 9]
print(multiply_lst(num))
    


#4
#checks fpr the smallets number in a list
def min_num(lst):
    return min(lst)

lst = [3, 6, 7, 2, 10]
print(min_num(lst))



#8
#checks if a list is empty
def empty_lst(lst):
    return len(lst) == 0

lst1 = []
lst2 = [2, 6, 8]

print(empty_lst(lst1))
print(empty_lst(lst2))




#11
#the common elemnets in one set in reference to another
def intersection_members(lst1, lst2):
    for item in lst1:
        if item in lst2:
            return True
    return False

lst1 = [4, 6, 7 , 9]
lst2 = [6, 8, 2, 1]

print(intersection_members(lst1, lst2))



#14
#remove te even numbers and list only the odd numbers
def remove_even(lst):
    return [num for num in lst if num % 2 != 0]

lst1 = [5, 7, 2, 4, 6 ,4, 2, 5, 8, 9]

print(remove_even(lst1))




#15
#shuffles the items withim a list
import random

def shuffle_lst(lst1):
    random.shuffle(lst1)
    return lst1

lst = ["w", "t", 5 ,6 ,"f" ,"y"]

print(shuffle_lst(lst))



#22
#add a list to a list
def append_lst(lst1, lst2):
    lst1.extend(lst2)
    return lst1


lst1 = ["q", "g", "u"]
lst2 = [3, 7, 8, 0]

print(f"The combined list is: {append_lst(lst1, lst2)}")



#23
#picking a random item from a particular list
import random

def random_pick(lst):
    return random.choice(lst)


lst = [2, 6, 8 , 4, "t", "y"]

print(f"Random value from list: {random_pick(lst)}")



#30
#make the sublists of a given list
def sublist(lst1):
    subs = []
    for i in range(len(lst1) + 1):
        for j in range(i):
            subs.append(lst1[j:i])
    return subs

lst1 = [2, 7, 4, 7, 0]

print(f"All sublists of {lst1} are : {sublist(lst1)}")



#36
#combining list into a single integer
def lst_one_integer(lst1):
    return ''.join(map(str, lst1))

lst1 = [300, 4, 6 , 70]

print(lst_one_integer(lst1))




#DICTIONARIES
#3
#combining a 3 dictionaries into 1
def join_dictionaries(dict1, dict2, dict3):
    dict_final = {**dict1, **dict2, **dict3}
    return dict_final

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

print(join_dictionaries(dic1, dic2, dic3))

#9
#multiply all values within the dictionary
def dict_multiply(dict1):
    ans = 1
    for value in dict1.values():
        ans *= value

    return ans

dict1 = {"i":56, "ii":7, "iii":89}

print(f"The product of the dictionary is: {dict_multiply(dict1)}")





#TUPLES
#3
#create a tuple and check the position of any item in the tuple
def tuple_make(pos):
    num = (1, 3, 7, 9)
    print(f"The number in postion {pos} is {num[pos]}")

pos = int(input("Enter a postion of your choice to identify the number:"))

tuple_make(pos)



#6
#converting a tuple to a string
def tupl2str(tupl1):
    return ''.join(map(str, tupl1))


tupl = ("a", "n", "t")

print(f"The string made from the tuple is: {tupl2str(tupl)}")




#SETS
#3
#adding new members to a set
def new_mem(oldset, newset):
    oldset.update(newset)
    return oldset

current_set = {2, 7, 8 , 9}
new_members = {"r", "y", "j"}

print(f"The updated set is: {new_mem(current_set, new_members)}")



#12
#remove all members from a set
def remove_members(set1):
    set1.clear()
    return set1

full_set = {5, 8, 9, 5, 2}

print(f"The empty set: {remove_members(full_set)}")