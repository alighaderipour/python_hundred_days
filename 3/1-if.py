x = 10
message = f"The value of x is {x} and it is {'greater than 5' if x > 5 else 'less than or equal to 5'} aasdfasdf"
print(message)



#simple if (basic)
# If the number can be divided by 2 with 0 remainder.
if number % 2 == 0:
  print("This is an even number.")
# Otherwise (number cannot be divided by 2 with 0 remainder).
else:
  print("This is an odd number.")



# inline if (advanced)
number = 11
print(f"this is an {'even' if number%2 == 0 else 'odd' } number") 

