# class A:
#     def __init__(self,a=0,b=0) -> None:
#         self.a = a
#         self.b = b
#         print(self.a,self.b)

# # @A
# class B(A):
#     pass

# b=B(44,3)

# if True:
#     class A:
#         i=1234
#         def __init__(self) -> None:
#             print("Hello class inside the if block")
#             print(self.i*2)
        
    
#     a=A()
#     a.counter=85
#     while a.counter<500:
#         a.counter = a.counter+10
#         print(a.counter)
#         break
#     del a.counter

class Myclass:
    def f(self):
        # print(a , "is here")
        return "mawa"

z = Myclass()
zf=z.f
print(zf())