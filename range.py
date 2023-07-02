'''total=0
for i in range(1,101):
    if i%2 ==0:
       total+=i
print(f"The sum of even numbers :{total}")

'''
#ALTERNATE WAY:
total=0
for i in range(2,101,2):
    total+=i
print(f"The sum of even numbers :{total}")
