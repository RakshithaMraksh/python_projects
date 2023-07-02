set1={'Ram','Sita','jenny'}
set2={'Raghav','jenny','Jiya','Ramu'}
set3={'Pradeep','Surekha'}
#
# print(set1.union(set2))
# print((set1 | set2|set3))
print(set1.update(set2))
# print(set1.intersection(set2))
#print(set1 & set2 & set3)
print(set1.difference(set2))
print(set1-set2)
print(set1.difference(set2,set3))

print(set1.isdisjoint(set3))
print(set1.issubset(set2))
print(set1 <= set2)
print(set1.issuperset(set2))
set2.clear()
print(set2)
del set3
print(set3)