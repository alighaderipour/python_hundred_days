import random, math
guess_count = 0
target_number = random.randint(1,100)
print('target_number: ', target_number)


def user_guess():
    guessed_number = int(input('guess a number between 1 to 100 '))
    diff = target_number - guessed_number
    if abs(diff) == 0:
        print(f'you won!, the number was {guessed_number}')
        return True
        
    elif abs(diff) < 10:
        global guess_count 
        guess_count +=1
        if guessed_number < target_number:
            print('abit low, guess again!')
            
        else:
            print('abit high, guess again!')
            
        print(f'you guessed {guess_count} times')
            
    else:
       guess_count +=1
       if guessed_number < target_number:
            print('too low, guess again!')
            
       else:
            print('too high, guess again!')
            
       print(f'you guessed {guess_count} times')
    return False

while True:
    if user_guess():
        break