class Dog:
#One of the objects to be returned
    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
#Concrete Factory
    def get_pet(self):
        # returns a dog object

    def get_food(self):
        #returns dog food object

class PetStore:
#PetStore houses our abstract Factory

    def __init__(self, pet_factory=None):
        #pet_factory is our abstract Factory

    def show_pet(self):
        #utility method to display the details of the objects returned by the DogFactory


        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("It's food is '{}'!".format(pet_food))
