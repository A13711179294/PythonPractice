class F:
    def pri(self):
        print("FFF")
        pass
class E(F):
    def pri(self):
        print("EEE")
        pass
class D(E):
    print("D")
    pass
class C(D):
    print("C")
    pass
class B(C):
    print("B")
    pass
class A(B,F):
    pass
test=A()
test.pri()
print(A.__mro__)