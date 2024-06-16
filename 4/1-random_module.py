import random
random_tail = random.randint(0,1)
if random_tail == 0 :
    print ("Tails")
else:
    print("Heads")

"""
another example for random

"""

import random
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
random_choice = random.randint(0, len(names)-1)
print(f'{names} , {random_choice}, {names[random_choice]} is going to buy the meal today!')