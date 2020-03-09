
class A(object):
    
    def test(self):
        print("A --- test 方法")

    def demo(self):
        print("A --- demo 方法")


class B(object):
    
    def demo(self):
        print("B --- demo 方法")


class C(A, B):
    pass

c = C()

c.test()
c.demo()

print(C.__mro__)
