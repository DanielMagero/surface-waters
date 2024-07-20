def sublist(lst1):
    subs = []
    for i in range(len(lst1) + 1):
        for j in range(i):
            subs.append(lst1[j:i])
    return subs

lst1 = [2, 7, 4, 7, 0]

print(f"All sublists of {lst1} are : {sublist(lst1)}")