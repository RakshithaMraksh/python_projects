numbers=input("Enter the numbers:")

numbers_list=numbers.split()
print(numbers_list)
count=0
for i in numbers_list:
    count+=1
print(f" The count of number lis is :{count}")
for i in range(0,len(numbers_list)):
    numbers_list[i]=int(numbers_list[i])
print(numbers_list)
maximum_number=numbers_list[0]
for number in numbers_list:
     if number > maximum_number:
         maximum_number=number
print(f"The maximum number in the list is:{maximum_number}")