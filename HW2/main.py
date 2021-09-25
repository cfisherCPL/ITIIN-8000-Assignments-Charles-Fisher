"""
The project should simulate the operation of a restaurant.
When I run main.py it should start by randomly generating a quantity for
each of the menu items in the restaurant.
These quantities will have to go down when customers order the menu items.
Each customer order can contain an Entree, Side, Wine, and a Dessert.

Entrees (Random quantity between 1 and 6 of each)
Chicken
Beef
Vegetarian

Sides (Random quantity between 5 and 10 of each)
Soup
Salad

Wines (Random quantity between 2 and 5 each)
Merlot
Chardonnay
Pinot Noir
Rose

Desserts (Random quantity between 1 and 3 each)
Flan
Creme Brulee
Chocolate Moose
Cheesecake

After generating the random quantities of each menu item
the program should prompt the user to input a role and an action
(this does not need to be done as a single input).

The roles and the actions each role can take are defined below

Waiter
Read Menu: lists how much of each menu item is available
What are the (Entrees/Wines/Sides/Desserts): lists how much of each of the chosen categories is available

Customer
Order (ordered food): takes an order from the customer and subtracts the order from the available food total.
Customers are told if what they ordered is not available and asked if they would like something else
Customers must be able to make their selection in any order and leave out choices. For example, they could just ask
for Merlot or they could ask for Flan, Pinot Noir, Salad, and Beef
Random Choice
A random order is made using the choice function from the random module
See Chapter 11 of IP or 3.11 of the Python Cookbook

Manager
Close: Lists the remaining food at the end of the night and then sets all of the values to zero
Open: Restarts the main .py file and generates a new random amount of foods

"""
from MenuFull import MenuFull
import time

# generate our menu
# it does all the stuff for us in the class init!
menu = MenuFull()

# start our main game loop
cafeopen = True
while cafeopen:
    role_select = input('Welcome to the Hades Cafe. Choose a role by typing\n'
                       'WAITER, CUSTOMER, MANAGER or QUIT: \n'
                        '>>>  ')
    if role_select.casefold() == 'quit':
        print("You escaped the sisyphean cycle. Or have you?")
        cafeopen = False
        break
    elif role_select.casefold() == 'waiter':
        print("You're the waiter!")
        while iswaiter := True:
            waiterprompt = input('Options(type one): MENU, ENTREES, SIDES, WINES, DESSERTS, or ROLE\n'
                                 '>>>  ')
            if waiterprompt.casefold() == 'role':
                iswaiter = False
                break
            elif waiterprompt.casefold() == 'menu':
                menu.read_menu()
            elif waiterprompt.casefold() == 'entrees':
                menu.Entrees.list_category()
            elif waiterprompt.casefold() == 'sides':
                menu.Sides.list_category()
            elif waiterprompt.casefold() == 'wines':
                menu.Wines.list_category()
            elif waiterprompt.casefold() == 'desserts':
                menu.Desserts.list_category()
            else:
                print("Let's try that again...")


            
            
    elif role_select.casefold() == 'customer':
        print("You're the customer!")
        while iscustomer := True:
            custprompt = input('Type your order choices, each separated by a single "," and no spaces.\n'
                               "Please note any '-' hyphens in menu names.\n"
                               'Type RANDOM for a meal selected by chance.\n '
                               '>>>  ')
            orderlist = custprompt.split(',') #bc can type in any order, feed em into a list
            # iterate over that list to pull each out one by one for comparisons
            for x in orderlist:
                x.casefold()
                if x=='chicken' or x=='beef' or x=='vegetarian':
                    menu.Entrees.check_order(x)
                elif x=='soup' or x=='salad':
                    menu.Sides.check_order(x)
                elif x=='pinot-noir' or x=='chardonnay' or x=='merlot' or x=='rose':
                    menu.Wines.check_order(x)
                elif x=='flan' or x=='creme-brulee' or x=='chocolate-mouse' or x=='cheesecake':
                    menu.Desserts.check_order(x)
                elif x == 'random':  # whenever we see random, generate a whole meal
                    menu.Entrees.random_pick()
                    menu.Sides.random_pick()
                    menu.Wines.random_pick()
                    menu.Desserts.random_pick()
                else:
                    print("We don't serve {} here.".format(x))

            custprompt2 = input('\n'
                                'Type anything you want to order MORE\n'
                                'or type ROLE to return to selection \n'
                            '>>>  ')
            if custprompt2.casefold() == 'role':
                ismanager = False
                break

    #  Here's where we can pretend to be a manager!
    elif role_select.casefold() == 'manager':
        print("You're the manager...")
        while ismanager := True:
            mgrprompt = input('Options(type one): CLOSE, OPEN, or ROLE\n'
                                 '>>>  ')
            # return to role selection
            if mgrprompt.casefold() == 'role':
                ismanager = False
                break
            # close the store as per project outline
            elif mgrprompt.casefold() == 'close':
                menu.read_menu()
                menu.close()
                print("All menu items have been destroyed.")
            # open the store as per project outline
            elif mgrprompt.casefold() == 'open':
                ismanager = False
                menu.reset()
                print("Regenerating menu and reopening.")
                time.sleep(1)
                print("..")
                time.sleep(1)
                print("..")
                time.sleep(1)
                print("..")
                break


    # catch those misspellings and re-prompt at top of loop
    else:
        print("Let's try again...\n")