'''count=1
while count<=5:
    print(count)
    count+=1
    if count==3: #Else block wont be exceuted!! becz we are forcefully stopping while
        break
else:
    print("In else block")
print("Out of loop") '''

'''
number=int(input("Enter the  number -1 to quit"))
while number != -1:
    print(number)
    number=int(input("Enter the  number -1 to quit"))
else:
    print("in else block")
print("Out of loop") '''
'''
count=0
while True:
    print(count)
    count+=1
    if count==5:
        break
else:
    print("in else block")
print("Out of loop")'''

'''
total=0
number =int(input("Enter the number:(0 to quit)"))
while number !=0:
    total=total+number
    number =int(input("Enter the number:(0 to quit)"))
print(f"The total value is:{total}")'''
'''
count=1
while count<=10:
    print(count)
    count+=1
    if count==7:
        break
    print("Hello")
print("Out of loop")'''
'''
list1=['Hi','Hello','Welcome']
names=['krishna','ram','lucky']
for item in list1:
    for name in names:
        print(item,name)
        if item=='Hello' and name =='ram':
            break
        print("break")
    print("Out from inner for loop")
print("Out from outer for loop")'''
'''
count=1
while count<=10:
    print(count)
    count+=1
    if count==7:
        continue
    print("Hello")
print("Out of loop")'''
'''
for i in range(1,10):
    if i==7:
        continue
    else:
        print(i)'''
for i in range(1,11):
    pass
print("Out of loop")
count=1
while count<=10:
    print(count)
    count+=1
    if count==7:
        pass
    print("Hello")
print("Out of loop")

