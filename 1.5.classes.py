class myClass():
    def method1(self):
        print("myClass method 1")

    def method2(self, someString):
        print("myClass method 2 " + someString)

    def method3(self, someString=""):
        print("myClass method 3 " + someString)


class childClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("myClass method 1")

    def method2(self, someString):
        print("myClass method 2 ")


def main():
    c = myClass()
    c.method1()
    c.method2("wkwk")
    c.method3()
    print("=" * 10)
    d = childClass()
    d.method1()
    d.method2("wkwk")
    d.method3()


main()
