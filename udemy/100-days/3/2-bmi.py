
height = "1.80"

weight = "81"



#‍ 
#*  اينجا يك نكته داريم اينكه اگر رشته ما دسيمال پوينت داشته باشه نميتوني با اينت تبديل كني
# print(int(15.3))
# print(int("15"))
#!الان اين خط پايين خطا ميده
# print(int("15.2"))  
bmi = float(weight)/(float(height)**2)

#* اينارو با elif  همي ميشه نوشت
if(bmi <18.5 ):
    print(f"Your BMI is {bmi}, you are underweight.")
    
if(  18.5 <= bmi < 25 ):
    print(f"Your BMI is {bmi}, you have a normal weight.")
    
if( 25  <=bmi < 30 ):
    print(f"Your BMI is {bmi}, you are slightly overweight.")
if(30  <=bmi < 35 ):
    print(f"Your BMI is {bmi}, you are obese.")

if(bmi >=35 ):
    print(f"Your BMI is {bmi}, you are clinically obese.")
    
#? hala fargh on if haye poshte sare ham ba if/elif/else dar ine ke
#? oon if haye pey dar pey dar har soorat check mishan momkene chand tashoon dorost bashe
#? vali to if/elif/else faghat yekishoon dorost dar miad