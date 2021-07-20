class Train:
    def __init__(self,name,seats,fare):
        self.name=name
        self.seats=seats
        self.fare=fare
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
    def fareInfo(self):
        print(f"The price of {self.name} is {self.fare}")
    def bookTicket(self):
        if self.seats>0:
            self.seats=self.seats-1
            print(f"Your Ticket has been book! Number of ticket available is {self.seats}")
        else:
            print("No Booking Available")
RajdhaniExpress=Train("RajdhaniExpress : 14015",2,400)
RajdhaniExpress.getStatus()
RajdhaniExpress.fareInfo()
RajdhaniExpress.bookTicket()
RajdhaniExpress.getStatus()
RajdhaniExpress.bookTicket()
RajdhaniExpress.bookTicket()


