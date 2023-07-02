'''import random
a=random.randint(1,7)
#print(a)
b=random.randrange(1,3)
#print(b)
c=random.uniform(1,6)
#print(c)
l=[10,20,4,-4.78,90]
d=random.choice(l)
print(d)'''

import random
side=random.randint(0,1)
print(side)
if side==1:
    print("Heads")
else:
    print("Tails")