def remove_members(set1):
    set1.clear()
    return set1

full_set = {5, 8, 9, 5, 2}

print(f"The empty set: {remove_members(full_set)}")