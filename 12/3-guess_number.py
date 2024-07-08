import random, math
guess_count = 0
target_number = random.randint(1,100)
print('target_number: ', target_number)


def user_guess():
    global guess_count
    if guess_count == 10 :
        print(
            f'you ran out of chances, the answer was {target_number}'
        )
        return True
    guessed_number = int(input('guess a number between 1 to 100 , you have 10 try :  '))
    diff = target_number - guessed_number
    if abs(diff) == 0:
        print(f'you won!, the number was {guessed_number}')
        return True
        
    elif abs(diff) < 10:
         
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