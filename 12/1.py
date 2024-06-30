##scope##
friends = 1

# variable inside a function is local scope and cannot be accessed outside
#? local scope
def increase_friends():
    friends = 2
    print('friends inside the function: ', friends)
    
increase_friends()
print('enemies outside the function', friends)

#? global scope
player_health = 100

def print_health():
    player_str = 100
    print(f'current player health :  {player_health}')

print_health()


#? modify global scope's value  ---> need "global keyword"
def drink_potion():
    global player_health
    player_health -=10
    print(f'drinking potion will decrease the player health, new health is {player_health}')

drink_potion()

