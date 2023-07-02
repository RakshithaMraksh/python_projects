"""weight=float(input("Enter weight in kg:"))
height=float(input("Enter height in meters:"))
BMI=(weight)/(height**2)
print("BMI is:",BMI)
"""
# Anothe way
weight=input("Enter the weight in kg:")
height=input("Enter the height in m:")
#print(type(weight)) <class,'str'>
#print(type(height))  <class,'str'>
#bmi=weight/height**2  TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
bmi=int(weight)/float(height)**2 
# print(bmi) 21.333333333333332
print(int(bmi)) # 21

