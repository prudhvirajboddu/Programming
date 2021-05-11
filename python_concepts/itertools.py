# import itertools

# # count=itertools.count(1,2)

# # print(type(count))
# # print(next(count))
# # print(next(count))
# # print(next(count))
# # print(next(count))
# # print(next(count))

# # co=itertools.repeat([1,2],5)

# # sq=map(pow,range(1,11),itertools.repeat(2))

# # sqs=itertools.starmap(pow,[(8,2)])

# # print(list(sqs))
# words={'prudhvi','prabhu'}

# # p=itertools.permutations(words,2)

# # print(list(p))

# res=itertools.combinations_with_replacement([1,2,3,4],4)

# print(*(res),sep="\n")
from itertools import product
k,m=3,1000
n = [[2,5,4],[3,7,8,9],[5,5,7,8,9,10]]#[list(map(int, input().split()))[1:] for _ in range(k)]
results=map(lambda x:sum(i**2 for i in x)%m ,product(*n))
print(*(results))
# print(max(results))
# print(list(product(*n)))