# Parent class (Superclass)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

# Child class (Subclass)
class Dog(Animal):
    def __init__(self, name, breed):
        # Call the constructor of the parent class to initialize common attributes
        super().__init__(name, species="Dog")
        self.breed = breed

    # Override the make_sound() method
    def make_sound(self):
        return "Woof!"
    

dog = Dog("Buddy", "Golden Retriever")

print(f"{dog.name} is a {dog.species} of breed {dog.breed}.")

print(dog.make_sound())  

