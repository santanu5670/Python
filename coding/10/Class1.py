''' EmployeeName --> PascalCase
isFloatOrInt, isNumeric -> camleCase'''
class RaliwayForm:
    fromtype="RailwayForm"
    def printdata(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
santanu_from=RaliwayForm()
santanu_from.name="Santanu"
santanu_from.train="RajdhaniExpress"
santanu_from.printdata()
