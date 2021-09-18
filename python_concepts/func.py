# def fun(a):
#     """
#     returns square of a number when passes with a integer or floating point num
#     """
#     return a**2
    

# print(fun.__doc__,fun.__sizeof__())

# print(fun(3))

li = [1,2,3,4,5,6,7,8]

for i in li[::-1]:
    print(i)

from collections import deque

queue = deque([1,2,3,4,5])

print(queue)

queue.popleft()

queue.popleft()

queue.append(111)

print(queue)

p = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

print(p)
print(len(p))

