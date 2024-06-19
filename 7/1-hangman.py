import random
name_list = ['Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James', 'Benjamin', 'Lucas', 'Henry',
             'Alexander', 'Mason', 'Michael', 'Ethan', 'Daniel', 'Jacob', 'Logan', 'Jackson', 'Levi',
             'Sebastian', 'Mateo', 'Jack', 'Owen', 'Theodore', 'Aiden', 'Samuel', 'Olivia', 'Emma', 'Ava',
             'Charlotte', 'Sophia', 'Amelia', 'Isabella', 'Mia', 'Evelyn', 'Harper', 'Camila', 'Gianna', 'Abigail',
             'Luna', 'Ella', 'Elizabeth', 'Sofia', 'Emily', 'Avery', 'Mila', 'Scarlett', 'Eleanor', 'Madison', 'Layla', 'Penelope']
size_list = len(name_list)
random_index = random.randint(0, size_list - 1)
target_name = name_list[random_index]
num_tries = len(target_name)
lives = num_tries
for item in range (num_tries):
    intial_answer = []
    final_answer = []
    all_guessed =[]
    
    for item in range (len(target_name)):
        intial_answer.append('*')
        
    for item in target_name:
        final_answer.append(item.lower())
    
    guessed_alphabet =input('guess an alphabet :')
    if len(guessed_alphabet) > 2:
        print('please enter only one alphabet')
        lives -=1
        print(f'you have {lives} left')
        print(f'{intial_answer}')
        if lives == 0:
            print('you lost')
            break
        else:
            continue
    else:
        
        if guessed_alphabet in target_name:
             for item in range(len(target_name)):
                 if guessed_alphabet == final_answer[item]:
                     intial_answer[item]= guessed_alphabet
                     if '_' in final_answer and lives ==0 : 
                         print('you lost')
                         break
                     if '_' in final_answer and lives >0 :
                         print('one went')
                 else:
                      lives-=1
                      print(f'you have {lives} left')
                      if lives == 0:
                            print('you lost')
                            break
                      else:
                          continue
                     

