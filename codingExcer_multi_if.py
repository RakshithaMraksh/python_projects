size=input("What size do u want?")
bill=0
if size=='S' or size=='s':
    bill+=100
    print("Small Pizza Price is 100 Rs")
elif size=='M' or size=='m':
    bill+=200
    print("Medium Pizza Price is 200 Rs")
elif size=='L' or size=='l':
    bill+=300
    print("Large Pizza price is 300 Rs")
else:
    print("ThanK you !! Visit Again")
add_pepperoni=input("Do want pepperoni?(y/N)")
if add_pepperoni=='Y' or add_pepperoni=='y':
    if size=='S' or size=='s':
        bill+=30
    else:
        bill+=50
else:
    print("OK!!")
extra_cheese=input("Do you want Extra Cheese?(Y/N)")
if extra_cheese=='Y' or extra_cheese=='y':
    bill+=20
else:
    print("Ok!!")
print(f"Your Final Bill is {bill}")
print("Enjoy your Pizza!!")