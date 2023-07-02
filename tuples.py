'''tuple1=(10,13,-8,'jenny',True)
print(tuple1[0])
print(type(tuple1))
tuple2=(10)
print(type(tuple2))
#tuple1[0]=0   tuples are immutable .. we cant change 
#print(tuple1)'''

#Sets in python
set1={10,56,89,'jrnny',90,True,10,1}  # duplicates ,indexing, are not allowed, 
print(set1)
print(type(set1)) #<class 'set'>
set2={}  #<class 'dict'>
print(type(set2))
set3=set()
print(type(set3)) #<class 'set'>
set1.add(91)
print(set1)
print(len(set1))
set1.remove(10)
print(set1)
print(len(set1))
set1.discard(10)
print(set1)
#set1.remove(100)  #KeyError: 100
#print(set1)
'''set1.clear()
print(set1) '''
set1.pop()
print(set1)
set1.add((10,20,30)) # WE can add tuples to list becz tuples are immutable
print(set1)
set1.add([1,2,3]) #TypeError: unhashable type: 'list' becz list are mutable
print(set1)

