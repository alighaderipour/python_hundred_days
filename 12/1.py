##scope##
friends = 1

# variable inside a function is local scope and cannot be accessed outside
def increase_friends():
    friends = 2
    print('friends inside the function: ', friends)
    
increase_friends()
print('enemies outside the function', friends)



