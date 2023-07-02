height=int(input("Enter height in feet:"))
if height>=3:
    print("You can Ride!!")
    age=int(input("Enter your age:"))
    if age<=18:
        print("Pay 250 rps")
    else:
        print("Pay 500 rps")
else:
    print("You cannot ride!!")
print("BYE!!!")