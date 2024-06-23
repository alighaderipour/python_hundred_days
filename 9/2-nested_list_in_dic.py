# Dictionary with nested lists
student_courses = {
    "Harry": ["Potions", "Transfiguration", "Defense Against the Dark Arts"],
    "Hermione": ["Charms", "Herbology", "Arithmancy"],
    "Ron": ["Divination", "Quidditch Strategies"],
    "Draco": ["Potions", "Dark Arts"],
}

# Accessing elements in the nested list
print("Courses taken by Harry:", student_courses["Harry"])
print("Courses taken by Hermione:", student_courses["Hermione"])

# Adding a new course for a student
student_courses["Ron"].append("Care of Magical Creatures")
print("Updated courses for Ron:", student_courses["Ron"])



# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# ~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.

dict1 = {
    "Kerman Province" : ["kerman, Rayen"],\
    "National PostCode" : { "Iran" : "98", "China" : "541" }
}
print(dict1["National PostCode"]["Iran"])

#dict are ordered in python 3.7+
for i in dict1 :
    print(i)
    
    
