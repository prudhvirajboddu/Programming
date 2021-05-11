def gen(nums):
    for i in nums:
        yield(i*i)

nums=list(range(1,1000))

print(*(gen(nums)),sep="mawa")
