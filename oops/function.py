class A:
    def func1(self,a) -> int:
        return a*2

    def func1(self,a) -> str:
        return a+a
    

obj=A()

print(obj.func1(100))

print(obj.func1("res"))