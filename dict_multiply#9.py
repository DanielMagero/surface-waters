def dict_multiply(dict1):
    ans = 1
    for value in dict1.values():
        ans *= value

    return ans

dict1 = {"i":56, "ii":7, "iii":89}

print(f"The product of the dictionary is: {dict_multiply(dict1)}")