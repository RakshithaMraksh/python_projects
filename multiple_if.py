height=int(input("Enter your height?"))
bill=0
if height>=3:
    print("You can Ride!!")
    age=int(input("Enter your age:"))
    if age<12:
        bill=150
        print("Ticket price is 150 Rs")
    elif age<=18:
        bill=200
        print("Ticket price is 200 Rs")
    else:
        bill=500
        print("Your ticket price is 500 Rs")
    want_photo=input("Do you want to take photo?(Y/N)")
    if want_photo=='y' or want_photo=='Y':
        bill=bill+50
        print(f"your total bill is{bill}")
    else:
        print("Cant Ride!!!")
    print("Thank you...Enjoy your Ride!!")
else:
    print("BYE!!")