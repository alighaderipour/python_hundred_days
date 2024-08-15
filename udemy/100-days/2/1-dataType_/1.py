#subscripting
print('hello'[0]) #first index of hello
print(type(34_529.678)) # because instead of using , for 1000 like 345,243 we use _ in python (jus for human eyes, the interperter will ignore this underescore)


# converting data types
nameLen = len(input('your name?'))
nameLenStr = str(nameLen)
print("your name containts "+nameLenStr + " characters")

print(int(3.14)) # output will be converted to integer


two_digit_number = input('234')
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
print(two_digit_number[0] + two_digit_number[1])


#pemdas
#parantheses > exponent > multiplataion > divide > additon > subtraction > 
print(3*3+3/3-3)