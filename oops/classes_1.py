class A:
    def __init__(self, a):
        self.a = a
        print(self.a)


class B(A):
    super.__init__(self,a)

    def __init__(self, b):
        self.b = b
        print(self.b)

class C(A,B):
    super.__init__(self,a,b)
    def __init__(self,c):
        self.c=C
        print(self.c)

c=C(43,100,1000)

b=B(311,423)

a=A(666)