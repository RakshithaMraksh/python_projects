numbers=[10,0,-1,8]
'''print(numbers)
names=['Ram','sita']
print(names)
mixed_lis=[0,'Sita',10.10]
print(mixed_lis)
print(len(mixed_lis))
print(mixed_lis[-1])
'''
num=[10,0,7,-1,16,90]
#Slicing
'''
print(num[1:5]) #[0, 7, -1, 16]
print(num[0:4]) #[10, 0, 7, -1]
print(num[:]) #[10, 0, 7, -1, 16, 90]
print(num[0:4:2]) #[10, 7] Extended slicing
'''
#Sortinh
num.sort()
print(num)
#REveresing
num.reverse()
print(num)
#Minimum
print(min(num))
#Maximun
print(max(num))
#Append :=insert at last of list
num.append(24)
print(num)
#inserting:=at particular index
num.insert(2,45)
print(num)
num.extend([20,21,22,23]) #[90, 16, 45, 10, 7, 0, -1, 24, 20, 21, 22, 23]
print(num)
num[1]=100
print(num)
num[1:4]=[45,46,47]
print(num)
num.remove(0)
print(num)
num.pop() #REMOVES LAST ELEMENT
print(num[5])
print(num)