for number in range (1,16):
    if number%3==0 and number%5==0:
        print("fizz-buzz")
       
    elif number%5==0:
        print("Buzz")
    elif number%3==0:
         print("Fizz")
    else:
        print(number)