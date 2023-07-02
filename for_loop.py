'''names=['Ram','Sita','Raghav','Nidhi','Raksh']
for name in names :
    print(name)
    if name=='Raksh':
        print("Hey its me !!")
name='RAKSHITHA'
for i in name:
    print(i)
 '''   '''
numbers=[20,-7,8,5,4]
squares=[]
for i in numbers:
    square=i**2
    squares.append(square)
print(" The list of sqyares is :",squares)'''

#for -else loop
numbers=[2,3,-5,1,0,53]
'''for i in numbers:
    print(i)
else:
    print("Sucessfully completed")'''
'''
for i in numbers:
    print(i)
    if i==53:
       break
else:
    print("Sucessfully completed")
print("Out of for-else loop")'''
for i in numbers:
    if i&6==0:
        print(i)
    else:
        print("There is no number divivsible by 6 !!")
else:
    print("WE are in for -else block now")
