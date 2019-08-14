import time

#Welcome user to the game
print()
print ("")
print()


#Begin start of main game while loop

#Declare and initialize yo in-game variables
userInput1 = '' # user input for the game, keep blank here

#Describe setting
print()
print ("")
print()
   
#User decision point
print()
print ("") #Ask user a question
print()
        
#Input
userPathLook = input("") #add an input prompt betwen the quotes
        
#User choice number 1
if userPathLook == "": #add whatever choice 1 can be, ex yes or no
    print()
    print ("") #tell the user what happens for choice 1
    print()
#User choice number 2
elif userPathLook == "no": #add whatever choice 2 can be, ex yes or no
    print()
    print ("") #tell the user what happens for choice 2
    print()
        

#End of game code

#User goodbye
print()
print("") #say thank you and goodbye to the user
print()

time.sleep(5)
