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
        return Dog()

    def get_food(self):
        #returns dog food object
        return "Dog Food!"

class PetStore:
#PetStore houses our abstract Factory

    def __init__(self, pet_factory=None):
        #pet_factory is our abstract Factory

        self._pet_factory = pet_factory

    def show_pet(self):
        #utility method to display the details of the objects returned by the DogFactory

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("It's food is '{}'!".format(pet_food))


#Create a Concrete Factory
factory = DogFactory()

#Create a pet store housing our Abstract Factory
shop = PetStore(factory)


#Invoke the utility method to show the details of our pet
shop.show_pet()
