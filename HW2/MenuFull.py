from MenuCategory import MenuCategory


class MenuFull:
    
    # init makes 4 categories with their random ranges
    # then each category is filled with named items
    # quantity is generated via the add_item function call
    # this might be dumb vs using a dictionary? 
    def __init__(self):
        self.Entrees = MenuCategory('Entrees', 1, 6)
        self.Sides = MenuCategory('Sides', 5, 10)
        self.Wines = MenuCategory('Wines', 2, 5)
        self.Desserts = MenuCategory('Desserts', 1, 3)

        self.Entrees.add_item('Chicken')
        self.Entrees.add_item('Beef')
        self.Entrees.add_item('Vegetarian')

        self.Sides.add_item('Soup')
        self.Sides.add_item('Salad')

        self.Wines.add_item('Merlot')
        self.Wines.add_item('Chardonnay')
        self.Wines.add_item('Pinot-Noir')
        self.Wines.add_item('Rose')

        self.Desserts.add_item('Flan')
        self.Desserts.add_item('Creme-Brulee')
        self.Desserts.add_item('Chocolate-Mouse')
        self.Desserts.add_item('Cheese-Cake')
    
    # full menu is printed
    def read_menu(self):
        self.Entrees.list_category()
        self.Sides.list_category()
        self.Wines.list_category()
        self.Desserts.list_category()
    
    # reinitializes the menu with new quantities
    def reset(self):
        self.__init__()
    
    # sets all the menu items to zero quantity
    def close(self):
        self.Entrees.close_category()
        self.Sides.close_category()
        self.Wines.close_category()
        self.Desserts.close_category()


# Below here be testing...
"""
the_menu = MenuFull()
the_menu.read_menu()

the_menu.Desserts.list_category()

the_menu.close()
the_menu.read_menu()
the_menu.reset()
the_menu.read_menu()
"""