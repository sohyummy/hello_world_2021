# THE RED MOON

# all the game objects are defined here

bagItems = []
roomObjects = ["radio" , "tape" , "knife" , "broken glass" , "fire poker"]
murderWeapon = "fire poker"
fingerPrint = "not working"
requiredItems = ["battery" , "tape"]

# this is the welcome function to start the story
def welcome():
    print("Another murder in Chelsea.")
    print("This place looks like a mess!")
    print("Let's look around for the murder weapon first")
    breakLine()

    print("Darn it! My fingerprint reader is out of juice. Must be some batteries lying around here.")
    print(roomObjects)
    


# this function repeats the selection of objects for the gamer
def selection():
    print("I can see the following objects around me")
    print(roomObjects)
    
    return(game())

# break line 
def breakLine():
    return(input("..."))

# this function defines the test results of objects the user wants to test
def game():
    objectSelection = input("Select the object you want to see closely: ")
    
    def testObject():
        if len(bagItems) == 2:
            if objectSelection == murderWeapon:
                print("This is it! Gotta keep it as the evidence")
            else:
                breakLine()
                print("This not the weapon. Gotta keep looking.")
        # elif (bagItems == ["tape"]):
        #     print("Need to find batteries to start this darn thing")
        # if bagItems == ["battery"]:
        #     print("Gotta find some tape to capture the finger prints")
        else:
            print("Gotta find some batteries and tape to make the tester work. I wonder if I can find some here.")
            breakLine()
        return (selection())

    if objectSelection == "radio":
        print("I can use the radio's battery to run my tester!")
        print("Battery is added to your bag")
        bagItems.append("battery")
        print("Your bag has ")
        print(bagItems)
        breakLine()
        return (selection())

    if objectSelection == "tape":
        print("I need tape to read finger prints!")
        print("Tape is added to your bag")
        bagItems.append("tape")
        print("Your bag has ")
        print(bagItems)
        breakLine()
        return (selection())

    if objectSelection == "knife":
        print("Knife with some blood on it, could be the weapon. I should test it")
        action = input("test or back? ")
        if action == "test":
            testObject()

        else:
            breakLine()
            return (selection())

    if objectSelection == "broken glass":
        print("This glass is very sharp and bloody. I should test it.")
        action = input("test or back? ")
        if action == "test":
            testObject()
        else:
            breakLine()
            return (selection())

    if objectSelection == "fire poker":
        print("Almost missed. I should test it.")
        action = input("test or back? ")
        if action == "test":
            testObject()
        else:
            breakLine()
            return (selection())


def main():
    welcome()
    game()


main()

# neededItem = "battery"
# if neededItem in bagItems:
#     print("The batteries work, I can use my Finger_Print_3000 again")
# else:
#     print("Dang it! The batteries are dead. I wonder if I can find some batteries here")





# myItem = ["phone", "wallet", "laptop"]
# neededItem = "keys"
# if neededItem in myItem:
#     print("you're in")
# else:
#     print("you don't have the key")
#     print("Please make a choice")
#     print("a. go to locker")
#     print("b. check under door plant")
#     choice = input("Enter your choice: ")

# if choice == "a":
#     print("you found a key!")
#     myItem.append("key")
#     print (myItem)
#     myItem.remove("key")

# else:
#     print("Sorry, try again")

# this function tests weather the selected weapon is accurate or not
# def testObject()  :
#     if len(bagItems) == 2:
#         if objectSelection == murderWeapon:
#             print("This is it! Gotta keep it as the evidence")
#         else:
#             print("This not the weapon. Gotta keep looking.")
#     elif (bagItems == ["tape"]):
#         print("Need to find batteries to start this darn thing")
#     # if bagItems == ["battery"]:
#     #     print("Gotta find some tape to capture the finger prints")
#     else:
#         print("Gotta find some batteries and tape to make the tester work. I wonder if I can find some here.")
#     return (selection())
    # if requiredItems in bagItems:
    #     if objectSelection == murderWeapon:
    #         print("This is it! Gotta keep it as the evidence")
    #     else:
    #         print("This not the weapon. Gotta keep looking.")
    # if bagItems == ["tape"]:
    #     print("Need to find batteries to start this darn thing")
    # if bagItems == ["battery"]:
    #     print("Gotta find some tape to capture the finger prints")
    # else:
    #     print("Gotta find some batteries and tape to make the tester work. I wonder if I can find some here.")

    
                # if len(bagItems) == 2:
            #     if objectSelection == murderWeapon:
            #         print("This is it! Gotta keep it as the evidence")
            #     else:
            #         print("This not the weapon. Gotta keep looking.")
            # elif (bagItems == ["tape"]):
            #     print("Need to find batteries to start this darn thing")
            # # if bagItems == ["battery"]:
            # #     print("Gotta find some tape to capture the finger prints")
            # else:
            #     print("Gotta find some batteries and tape to make the tester work. I wonder if I can find some here.")
            # return (selection())





