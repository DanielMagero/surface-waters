def multiply_lst(num):
    ans = 1
    for number in num:
        ans *= number
    return ans

num = [2, 7, 8, 9]
print(multiply_lst(num))
    