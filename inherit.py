class Mammals:

    legs = 4

class Dog(Mammals):

    name = 'Puppy'
    age = 1

    #instance constructor, object initializer
    def __init__(self, name=name, age=age):
       self.name = name
       self.age = age 

    def bio(self):
        return f"My name is {self.name} and I'm {self.age}"   

Huskie = Dog('Huskie', 5)
Bulldog = Dog()
