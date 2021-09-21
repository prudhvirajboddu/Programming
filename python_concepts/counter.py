from collections import Counter,namedtuple

li = [1,2,2,3,4,4,4,5,5,6]

print(Counter(li))

print(Counter(li).most_common())

nn=namedtuple('name','name,age,sex')

a=nn('prudhvi',22,'male')

print(a)    