weight=float(input("Enter the weight in kg:"))
height=float(input("Enter the height in m:"))
bmi=round(weight)/(height)**2 
if bmi<18.5:
    print(f"Your BMI is {bmi} and your underweight")
elif bmi<25:
    print(f"You BMI is {bmi} and your normal weight")
elif bmi<30:
    print(f"You BMI is {bmi} and your overweight")
elif bmi<35:
    print(f"You BMI is {bmi} and your obese")
else:
    print(f"You BMI is {bmi} and your obese")