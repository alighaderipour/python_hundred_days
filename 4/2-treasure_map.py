line1 = ["", "",""]
line2 =["", "",""]
line3 = ["", "",""]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position ="B3" # Where do you want to put the treasure?


position0 = ord(position[0].lower()) - ord("a") + 1 
position1 = int(position[1])



# 🚨 Don't change the code above 👆
# Write your code below this row 👇


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
map[position1-1][position0-1] = "X"
print(f"{line1}\n{line2}\n{line3}")



"""
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

"""