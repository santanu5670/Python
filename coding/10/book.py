class Book_property:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        print(f"Book name is {self.name} and id is {self.id}")
book1=Book_property("C++",1)
book2=Book_property("Python",2)
book1.show()
book2.show()

