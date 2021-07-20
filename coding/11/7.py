class Book:
    def addCategory(self):
        self.c=input('''Select category name = 
        1. horror
        2. romance
        3. non-friction ''')
    def book_category(self,name,id,price):
        if self.c=='horor':
            self.name=input("Enter name = ")
            self.id=int(input("Enter book id = "))
            self.price=int(input("Enter the price of book = "))
        elif self.c=='romance':
            self.name=input("Enter name = ")
            self.id=int(input("Enter book id = "))
            self.price=int(input("Enter the price of book = "))
        elif self.c=='non-friction':
            self.name=input("Enter name = ")
            self.id=int(input("Enter book id = "))
            self.price=int(input("Enter the price of book = "))
        else:
            print("Invalid input")
    def get_price(self):
        self.s=input("Enter the category of the book = ")
        self.n=input("Enter the name of the book = ")
        # if self.s=='horor' and self.n==self.name:

            
        


