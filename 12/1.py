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
    player_str = 15
    print(f'current player health :  {player_health}')
    print(f'current player strength :  {player_str}')

print_health()


#? modify global scope's value  ---> need "global keyword"
def drink_potion():
    global player_health
    player_health -=10
    print(f'drinking potion will decrease the player health, new health is {player_health}')

drink_potion()

"""
#? this code does not work! you need define player_weight as global variable in order to be able to modify it
player_weight = 70

def getting_fat():
    player_weight +=10
    print(player_weight)

getting_fat()

#? corrected code 👇
player_weight = 70

def getting_fat():
    global player_weight  # Declare player_weight as global
    player_weight += 10
    print(player_weight)

getting_fat()  # Output: 80

"""
def game():
    def show_inventory_size():
        inventory =1
        print(inventory)
# show_inventory_size() # this won't work because show_inventory_size() is nested to game() function



#! does python have a block scope????

enemies = ['skeleton', 'zombie', 'alien']
game_level = 3
if game_level < 5:
    new_zombie = enemies[0]

print(new_zombie)


# modify global variable
# one way is to use global keyword
my_height = 170
def increase_height():
    global my_height
    my_height+=1
    print('my_height: ', my_height)
increase_height()   
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
#? a better approach for modifying global variable 👇👇
my_age = 20
def increase_age():
    return my_age + 1

my_age = increase_age()
print(my_age)
my_age = increase_age()
print(my_age)
#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
#? global constant is a variable you never wanna change
#? you just name it in uppercase , that's all 
URL = 'https://www.google.com'
TWITTER_ID = '@Shahaz'
TOKEN_CODE = '234435w34599384590340985098q34805995q34905iodfgjasdfjasdofasdfp'


