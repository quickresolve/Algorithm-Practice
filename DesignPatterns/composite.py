class Component(object):
    """Abstract class"""

    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass

class Child(): #inherits from the abstract class, Component
    """Concrete class"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        #This is where we store the name of your child item


    def component_function(self):
        #Print the name of your child item here!
        print("{}".format(self.name))

class Composite(): #Inherits from the abstract class, Component
