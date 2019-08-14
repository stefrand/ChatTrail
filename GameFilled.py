import time

#Welcome user to the game
print()
print ("Hi")
print()


#Begin start of main game while loop

#Declare and initialize yo in-game variables
userInput1 = '' # user input for the game, keep blank here

#Describe setting
print()
print ("You are in the woods.")
print()
   
#User decision point
print()
print ("Do you want to go home?") #Ask user a question
print()
        
#Input
userPathLook = input("Type yes to go home or no to continue: ") #add an input prompt betwen the quotes
        
#User choice number 1
if userPathLook == "yes": #add whatever choice 1 can be, ex yes or no
    print()
    print ("You turn around and go home.") #tell the user what happens for choice 1
    print()
#User choice number 2
elif userPathLook == "no": #add whatever choice 2 can be, ex yes or no
    print()
    print ("You go hiking for the rest of the day.") #tell the user what happens for choice 2
    print()
        

#End of game code

#User goodbye
print()
print("Thank you for playing!") #say thank you and goodbye to the user
print()

time.sleep(5)
