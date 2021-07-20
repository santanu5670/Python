class Vegetable:
    def __init__(self,vname):
        self.vname=vname
    def display(self):
        print("Vegetable name is",self.vname)
class Red_vegetable(Vegetable):
    def __init__(self, vname,price,color):
        super().__init__(vname)
        self.price=price
        self.color=color
    def display(self):
        print(f"Vegetable under {self.color} colour price is {self.price}")
class Green_vegetable(Vegetable):
    def __init__(self, vname,price,color):
        super().__init__(vname)
        self.price=price
        self.color=color
    def display(self):
        print(f"Vegetable under {self.color} colour price is {self.price}")
v=Vegetable("Tomato")
v.display()
r=Red_vegetable("Tomato",30,"Red")
r.display()
g=Green_vegetable("Cabbage",20,"Green")
g.display()

