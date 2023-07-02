"""a,b,c=4,5,6
d=a+b
d+=a
print(a,b,c)
a+=2
print(a)

print(d)
"""
a,b=1,2
c=a+b
print(c)
c+=a
print(c)
c%=b
print(c)
c//=a
print(c)

a=5
print(id(a))
a=8
print(id(a))