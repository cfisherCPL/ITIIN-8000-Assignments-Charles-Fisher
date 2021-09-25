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

# generate our menu using the MenuFull Class as written
# it does all the stuff for us in the class init!


# start our main game loop
#prompt for role selection or allow to quit!

    # check for quit option first. let ppl quit when they loop back to role selection

    # pretend to be a waiter
        # prompt selection of full menu or each category
        # allow return to role select from here

        # if they misstyped, prompt to top of waiter menu loop


    #  Here's where we pretend to be a customer!
        # prompt for menu input
        # bc can type in any order, feed em into a list with delimiter
            # iterate over that list to pull each out one by one for comparisons
            # use x in list
                # check each menu category item as OR statments in elifs to save time
                # use x.casefold

                # if they spelled it wrong or entered junk, prompt and reloop

            # prompt user to order more or go back to role select


    #  Here's where we can pretend to be a manager!

            # return to role selection

            # close the store as per project outline

            # open the store as per project outline

    # catch those misspellings and re-prompt at top of loop
