name=input("Enter your Name:")
age=input("Enter your age:")
height=float(input("Enter your height in cm:"))
weight=float(input("Enter your weight in kg:"))

height=height/100

BMI=weight/(height*height)

def bmi_category(BMI):
    if BMI<18.5:
        return "You are in under weight"
    elif BMI<=25:
        return "you are in normal weight"
    elif BMI<=30:
        return "you are in overweight"
    else:
        return "you are in obese"

category=bmi_category(BMI)

print("your body mass index:", BMI)

#receipt structure
print("--------------------------------------------")
print("               BMI REPORT                   ") 
print("--------------------------------------------")
print(f"Name             :  {name}                 ")
print(f"Age              :  {age}                  ")
print(f"Height           :  {height}               ")
print(f"Weight           :  {weight}               ")
print("--------------------------------------------")
print(f"BMI              :  {BMI:.2f}              ")
print(f"Category         :  {category}             ")
print("--------------------------------------------")


  