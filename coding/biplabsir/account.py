class Account:
    def __init__(self,name,age):
        self.name=name
        self.ahe=age
class Savings(Account):
    ammount=0
    def __init__(self, name, age,account_no):
        super().__init__(name, age)
        self.account_no=account_no
    def deposite(self,val_d):
        self.ammount=self.ammount+val_d
        print("Transaction successfully completed")
        print(f"Your ammount is {self.ammount}")
    def withdrawn(self,val_w):
        if val_w<=self.ammount:
            self.ammount=self.ammount-val_w
            print("Transaction successfully completed")
            print(f"Your ammount is {self.ammount}")
        else:
            print("insufficient Balance")
class loan(Account):
    ammount=0
    def __init__(self, name, age,account_no_loan):
        super().__init__(name, age)
        self.account_no_loan=account_no_loan
    def deposite(self,val_d):
        self.ammount=self.ammount+val_d
        print("Transaction successfully completed")
        print(f"Your ammount is {self.ammount}")
    def withdrawn(self,val_w):
        if val_w<=self.ammount:
            self.ammount=self.ammount-val_w
            print("Transaction successfully completed")
            print(f"Your ammount is {self.ammount}")
        else:
            print("insufficient Balance")
s=Savings("Santanu",21,565222)
val_d=int(input("Enter ammount for deposite"))
s.deposite(val_d)
val_w=int(input("Enter ammmount for withdrwan"))
s.withdrawn(val_w)
s=loan("Santanu",21,565222)
val_d_l=int(input("Enter ammount for deposite"))
s.deposite(val_d_l)
val_w_l=int(input("Enter ammmount for withdrwan"))
s.withdrawn(val_w_l)

    