heights=input("Enter all the heights separated by a space: ")
height_list=heights.split()
count=0
for i in height_list:
    count+=1
print(count)
for i in range(count):
    height_list[i]=int(height_list[i])
print(height_list)
total=0
for person in height_list:
    total+=person
print("Sun is :",total)
avg=total/count
print("Average height is:",round(avg))