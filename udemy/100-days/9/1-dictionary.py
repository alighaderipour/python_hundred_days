student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {
    
}
print(student_scores.items())
for item, value in  student_scores.items():
    if   value<70     : 
        student_grades[item]= "fail"
    if   71<=value<80    : 
        student_grades[item]= "Acceptable"
    if   81<=value<90    : 
        student_grades[item]= "Exceeds Expectations"
    if   91<=value<100    : 
        student_grades[item]= "Outstanding"
print(student_grades)


#! 👆 above code does not work 👆
#! 👆 above code does not work 👆
#! 👆 above code does not work 👆
#! 👆 above code does not work 👆
#! 👆 above code does not work 👆

#?  👇 use blow code 👇
#?  👇 use blow code 👇
#?  👇 use blow code 👇
#?  👇 use blow code 👇
#?  👇 use blow code 👇

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

    
for item, value in  student_scores.items():
    if value<=70 : 
       grade= "Fail"
    elif 71<=value<80    : 
        grade= "Acceptable"
    elif 81<=value<90    : 
        grade= "Exceeds Expectations"
    elif   91<=value<=100    : 
        grade= "Outstanding"
    else:
        pass
    student_grades[item] = grade


print(student_grades)