print('welcome to the tip calculator\n')
total= float(input('what was the total bill ? \n'))
percent = float(input('How much tip would you like to give in percent? 10, 12, or 15? \n'))
number_people = int(input('How many people to split the bill?\n'))
pay= (total/number_people ) +  (total/percent)/number_people
print(f'Each person should pay: {pay}  ')

