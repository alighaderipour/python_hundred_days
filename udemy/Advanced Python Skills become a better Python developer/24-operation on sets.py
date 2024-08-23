"""

Operation	               Notation                             	Example
Union	                    A ∪ B	                            A.union(B) or `A
Intersection	            A ∩ B	                        A.intersection(B) or A & B
Difference	                A \ B	                          A.difference(B) or A - B
Symmetric Difference	    A Δ B	                     A.symmetric_difference(B) or A ^ B

"""

# define two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# calculate the union
union = A.union(B)
print(union)  # {1, 2, 3, 4, 5, 6}
union = A | B
print(union)  # {1, 2, 3, 4, 5, 6}


# define two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# calculate the intersection
intersection = A.intersection(B)
print(intersection)  # {3, 4}
intersection = A & B
print(intersection)  # {3, 4}


# define two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# calculate the difference
difference = A.difference(B)
print(difference)  # {1, 2}
difference = A - B
print(difference)  # {1, 2}

# define two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# calculate the symmetric difference
symmetric_difference = A.symmetric_difference(B)
print(symmetric_difference)  # {1, 2, 5, 6}

symmetric_difference = A ^ B
print(symmetric_difference)  # {1, 2, 5, 6}
