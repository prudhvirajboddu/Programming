# # def mydecorator(func):
# #     def wrapper():
# #         print('<>'*20)
# #         print('~'*40)
# #         print("\t  ",end="")
# #         func()
# #         print('~'*40)
# #         print('<>'*20)

# #     return wrapper

# # #applying decorator through @
# # @mydecorator
# # def hello():
# #     print("Hi i am hello")

# # #call the decorated hello
# # hello() # calling func mydecorator by passing func hello as an argument to implement behaviour of mydecorator

# # mydecorator(hello)
# def decorator1(func):
#     def wrapper():
#         x=func()
#         print(x.upper())
#         return x.upper()
#     return wrapper
    
# def decorator2(func):
#     def wrapper():
#         x =func()
#         print(x.lower())
#         return x.lower()
#     return wrapper 

# @decorator1
# @decorator2
# def hello():
#     return  "Hello World NerD are you"
    
# # print(hello())
# hello()
# h=hello()
# Factorial program with memoization using
# decorators.

# A decorator function for function 'f' passed
# as parameter
def memoize_factorial(f):
	memory = {}

	# This inner function has access to memory
	# and 'f'
	def inner(num):
		if num not in memory:		
			memory[num] = f(num)
		return memory[num]

	return inner
	
@memoize_factorial
def facto(num):
	if num == 1 or num==0:
		return 1
	else:
		return num * facto(num-1)

print(facto(1000))
