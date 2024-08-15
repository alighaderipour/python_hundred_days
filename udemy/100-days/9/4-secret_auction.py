listo = []

def takeInfo():
     first_name= input('what is your name:')
     first_bid = input('what your bid?')
     listo.append({first_name: first_bid})
      
def findMax(listo):  
    max_key=None
    max_val = float('-inf')
    for dict in listo:
        for key,value in dict.items():
               val = int(value)
               if val > max_val:
                    max_val = val
                    max_key = key
    print(f"The winner is {max_key} with a bid of ${max_val}: ")

takeInfo()

while True:
     more = input("are there any other bidders? type 'yes' or 'no' ")
     if more == 'yes':
          takeInfo()
     elif more == 'no':
         findMax(listo)
         break
     else:
         print('invalid input, try again ')
         takeInfo()