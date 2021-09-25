from MenuItem import MenuItem
import random

class MenuCategory():

    # init makes name and sets ranges for the random filler quantities per item
    # num and max items used for adding new item to category
    # MenuItem objects stored in itemList that starts as empty strings
    def __init__(self, cat_name='None', rng_btm=1, rng_top=10):
        self.catName = cat_name
        self.numItems = 0
        self.maxItems = 4
        self.rng_btm = rng_btm
        self.rng_top = rng_top
        self.itemList = ['','','','']
    
    # basic getter for num items in categroy
    def get_num_items(self):
        return numItems

    # core function to add a MenuItem to the category
    # pulls input name as name of menu item
    # sets that menuitems quantity based on top and btm ranges of category
    # then adds that item to the storage list index based on current num of items
    # if full prints statement of notice
    def add_item(self, itemname):
        if self.numItems <= self.maxItems:
            newitem = MenuItem(itemname)
            quant = random.randint(self.rng_btm, self.rng_top)
            newitem.setQuant(quant)
            index = self.numItems
            self.itemList[index] = newitem
            self.numItems+=1
            # return "Item added to category."
        else:
            print("Menu category full!")

    # Prints all the menuitems in category
    # and their quantity
    def list_category(self):
        print('For {} we have:'.format(self.catName))
        for x in self.itemList:
            if x == '':
                pass
            else:
                print(x.toString())
    
    # Sets all menuitems in category to quantity of zero           
    def close_category(self):
        for x in self.itemList:
            if x == '':
                pass
            else:
                x.setQuant(0)
                
    def random_pick(self):
        picked_one = False
        while not picked_one:
            picker = random.randint(0,(self.numItems)-1)
            if self.itemList[picker] != '':
                # if self.itemList[picker].getQuant() > 0:
                self.itemList[picker].take_one()
                picked_one = True
                    # break
        # current sub issue with this function
        # is that it will pick potentially empty item
        # let's fix that with a while loop!
        # make this thing loop until it picks one that has items
        # MORE UPDATE: we need it to pull nothings bc of close function
        # damn manager


    def check_order(self, order):
        order = order
        for x in self.itemList:
            if x == '':
                pass
            elif order.casefold() == (x.getName()).casefold():
                x.take_one()
            else:
                pass
        

# Below here be testing...
"""
Entrees = MenuCategory('Entrees', 1, 6)
print(Entrees)
Entrees.add_item('steak')
Entrees.add_item('fish')
Entrees.add_item('vegetarian')

Entrees.list_category()
"""