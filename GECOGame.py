import os
import time

#User Welcome
print()
print("Welcome to The Starter Game!")
print()

#Tell user what they are doing today
print()
print("You will be choosing what you want for breakfast!")
print()

time.sleep(3)

#Declare variables
userChoice = '' #this will be what the user choses for breakfast
userKarma = 0 #this will keep track of user's wrong answers

#Set the scene
print()
print("You are standing in front of a very busy road!")
print("You are going to go pick up breakfast on the other side of the street.")
print()
print()

#Ask user to make a choice

print("You can go to either Walmark for bagels or Startbucks for coffee.")
print()
while True:
    userChoice = input("Please type Walmark or Startbucks: ")

    if userChoice.lower() == "startbucks":
        print()
        print("You buy overpriced coffee and don't have enough for a cookie. :( ")
        break
        print()
    elif userChoice.lower() == "walmark":
        print()
        print("You buy reasonably priced bagels, but they don't taste that good. :(")
        break
        print()
    else:
        userKarma = userKarma + 1
        if userKarma >= 3:
            print()
            print("Ninjas fall from the sky and cut your head off because your answers are terrible.")
            break
        print()
        print("Your answer is wrong and you should feel bad.")
        print("Type Walmark or Startbucks like I said. ")
        print()
        print("Your user Karma is now: {}/3".format(userKarma))
        print()
        
#Say goodbye to the user
print()
print("You snap back to reality and realize you already had breakfast and are playing a game.")
print()
print("Thank you for playing!")

time.sleep(5)
