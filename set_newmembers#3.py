def new_mem(oldset, newset):
    oldset.update(newset)
    return oldset

current_set = {2, 7, 8 , 9}
new_members = {"r", "y", "j"}

print(f"The updated set is: {new_mem(current_set, new_members)}")