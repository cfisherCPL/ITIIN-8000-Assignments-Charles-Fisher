
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
