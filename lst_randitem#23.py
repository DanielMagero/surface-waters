import random

def random_pick(lst):
    return random.choice(lst)


lst = [2, 6, 8 , 4, "t", "y"]

print(f"Random value from list: {random_pick(lst)}")