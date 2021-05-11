import functools
# @lru_cache
@functools.lru_cache
def fact(n):
    return n*fact(n-1) if n else 1

print(fact(100))