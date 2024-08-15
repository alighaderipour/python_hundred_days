"""how many letters would you like in your passsword:
    
how many symbols you like in your password:
    
how many numbers would you like in your password:
    """
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

how_many_letter = 14
how_many_number = 5
how_many_smybol = 3


letter_counter = 0
number_counter = 0
symbols_counter = 0

rand_pw = []
big_list = letters + numbers + symbols

length  =   how_many_letter + how_many_smybol +  how_many_number




for i in range(1,length*10):
    random_index = random.randint(0,len(big_list)-1)
    if big_list[random_index] in letters and letter_counter < how_many_letter :    
        letter_counter +=1
        rand_pw.append(big_list[random_index])
        
    elif big_list[random_index] in numbers  and number_counter < how_many_number:
        number_counter +=1
        rand_pw.append(big_list[random_index])
        

    elif big_list[random_index] in symbols and symbols_counter < how_many_smybol :
        symbols_counter +=1
        rand_pw.append(big_list[random_index])
        
    if len(rand_pw) == length:
        break
       
rand_pw_str = ''.join(rand_pw)
print(rand_pw_str, length, len(rand_pw_str))

