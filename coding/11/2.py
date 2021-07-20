class Animal:
    animalType="Mamal"
class Pet(Animal):
    color="White"
class  Dog(Pet):
    @staticmethod
    def bark():
        print("Bow Bow!")
d=Dog()
d.bark()