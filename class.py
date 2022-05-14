class Dog:

    #instance constructor
    def __init__(self, name, age) -> None:
       self.name = name
       self.age = age 

    def bio(self):
        return f"My name is {self.name} and I'm {self.age}"   

Huskie = Dog('Huskie', 5)







