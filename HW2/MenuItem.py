class MenuItem():
    # init sets the name and quanity to zero
    def __init__(self, name='Gray paste'):
        self.name = name
        self.quantity = 0
    # basic getter for name
    def getName(self):
        return self.name
    
    # basic setter for name
    def setName(self, newName):
        self.name = newName

    # basic getter for quantity
    def getQuant(self):
        return self.quantity

    # basic setter for quanity
    def setQuant(self, newQuant):
        self.quantity = newQuant
    
    # function to take one item from the quantity
    def take_one(self):
        if self.quantity > 0:
            self.quantity-=1
            print("We'll bring you one {}".format(self.name))
        else:
            print('We are out of {}'.format(self.name))
    
    # function to return a basic string of quantity and item name in order
    def toString(self):
        return "{} {}".format(self.quantity, self.name)


# Below here be testing...
"""
beef = MenuItem("beef")
print(beef.toString())

beef.setQuant(7)
print(beef.toString())

beef.setName("Steak")
print(beef.toString())
"""