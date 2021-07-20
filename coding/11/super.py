class A:
    def show(self):
        print("I am under A")
class B(A):
    def show(self):
        super().show()
        print("I am under B")
obj=B()
obj.show()