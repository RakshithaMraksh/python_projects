#Addition
a=int(input("Enter value of a:"))
b=int(input("Enter value od b:"))
c=a+b
print("Addition of a and b:",c)
print(type(c))
#Subtraction
d=a-b
print("Subtraction of a and b:",d)
#Multiplication
e=a*b
print("Multiplication of a and b:",e)
#String concatination
s="Hello World!!"
t="This is simple String"
r=s+t
print(r)
#Get length of string
print("Lenght of s is:",len(s))
print("Lenght of t is:",len(t))
print("Length of r is:",len(r))
#Convert string to integer
x="100"
print(type(x))
y=int(x)
print(type(y))
#Formatting output
print("The string(The string(Hello World!!)has 12 characters )")
#Covert to UPpercase/lower case
print(s.upper())
print(s.lower())
#Accessing sub string
print(s[0])
print(s[6:])
print(s[6:-1])
#strip: returnss a copy oof

#Create list
fruits=['apple','orange','kiwi','banana']
print(type(fruits))
print(len(fruits)) #getting length
print(fruits[0]) #Accessing list elements
print(fruits[1])
print(fruits[2])
print(fruits[3])
#Appending list elements
fruits.append('pear')
print(fruits)
#removing an item from list
fruits.remove('kiwi')
print(fruits)
#inserting an item to list
print(fruits.insert(1,'mango'))
#Combinig list
vegetables=['potato','carrot','radish','onion']
print(vegetables)
eatables=fruits+vegetables
print(eatables)
#Mixed data types
mixed=['data',5,100.0,1.3832839]
print(type(mixed))
print(type(mixed[0]))
print(type(mixed[1]))
print(type(mixed[2]))
print(type(mixed[3]))
#Change the individual elements of a list
