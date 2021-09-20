class A:
    def func1(self,a) -> int:
        return a*2

    def func1(self,a) -> str:
        return a+a
    

obj=A()

# print(obj.func1(100))

# print(obj.func1("res"))

class B:
    def __call__(self) -> None:
        print("Hello check")

b=B()

b()

# print(callable(b))

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def printname(aa): #can define any name but self is prefferable
        print("my name is :"+aa.name)

S1 = Student("arathi",22)
print(S1.name)
print(S1.age)
S1.printname()


class private:
    def __init__(self,a,b) -> None:
        self.a=a
        self.__b = 23

class Hide(private):
    def __init__(self, a, b,c) -> None:
        super().__init__(a, b)
        self.c=c

h = Hide(23,24,11)

print(h.a,h.c)
