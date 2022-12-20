import time
import sys

start = input("Hello there citizen of the lands of Pass. Please type in your name: ")

time.sleep(1)

game = input("Do you want to start a game in Slot 1 (y/n)? ")

if game == "y" or game == "Y":
    print("Your journey through the lands of Pass begin here.")
    print("You enter through the Teleporter")
    firstInput = input("Do you want to start level 1 (y/n)? ")
else:
    print("Exiting.")
    sys.exit()

if firstInput == "Y" or firstInput == "y":
    print("Starting level 1")
else:
    print("Exiting.")
    sys.exit()


# Level 1 starts here.
