import random
names=input("Enter everybod's name separted by coma:")
name_list=names.split(",")
#print(name_list)
length=len(name_list)
random_name=random.randint(0,length-1)
print(f"{name_list[random_name]} Will pay the bill !!")