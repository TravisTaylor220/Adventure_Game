
# INF360 - Programming in Python
# Travis Taylor 
# Final Project - Text based adventure game "Finding Finn"

###This program is an interactive story with choices for the user to select. If the user chooses an input that results in death or failure to complete the mission
###the program will prompt a message asking the player if they want to close the program.
###
###A critical and debug logging call is in the try and except at the start of the program
###
###imports functions from a seperate document.
###
###Also, I didnt know if it was possible to take some of the while loops and turn them into a function because certain choices lead to the same ending or failure throughout the story.
###
###Asks the user to input their name and weapon of choice before the game starts.


#imports sys and logging modules. logging modules outputs logs to a new document
import sys
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

#try and except to import functions for program. if import fails, critical error is flagged and fails to initiate program
try:
    from functions import *
    logging.debug("functions.py was loaded successfully to the game.")
except:
    logging.critical("functions.py was not loaded successfully. The game will now close.")
    print("functions.py was not loaded successfully. The game will now close.")
    sys.exit()

#start game function asking user if they want to play or not
start_game()
#second set of choices for  the user
second_choice()
#thrid set of choices for the user
third_choice()
#creates a list called fourth_choice that holds choices for user input
fourth_choice = ["cross", "sneak"]
#creates an empty string user_choice
user_choice = ""
#while loop to continue running until user enters list item from fourth choice
while user_choice not in fourth_choice:
    #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input. 
    user_choice = input("The havent pulled the drawbridge up yet...do you cross the drawbridge or sneak around and try to find another way in (cross/sneak)").lower().strip()
    if user_choice == fourth_choice[0]:
        logging.debug("User typed " + user_choice)
        fourth_choice_1()
        fifth_choice = ["roll", "jump"]
        #creates an empty string user_choice
        user_choice = ""
        #while loop to continue running until user enters list item from fifth choice
        while user_choice not in fifth_choice:
            #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input. 
            user_choice = input('"TRESPASSER!" he yells and fires his arrow...you react by rolling or jumping (roll/jump)').lower().strip()
            if user_choice == fifth_choice[0]:
                logging.debug("User typed " + user_choice)
                fifth_choice_1()
                sixth_choice = ["up", "down"]
                #creates an empty string user_choice
                user_choice = ""
                #while loop to continue running until user enters list item from sixth choice
                while user_choice not in sixth_choice:
                    #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input. 
                    user_choice = input("Do you sprint up the stairs or down the stairs (up/down)").lower().strip()
                    if user_choice == sixth_choice[0]:
                        logging.debug("User typed " + user_choice)
                        sixth_choice_1()
                        #creates a list called seventh_choice that holds choices for user input
                        seventh_choice = ["right","up"]
                        #creates an empty string user_choice
                        user_choice = ""
                        #while loop to continue running until user enters list item from seventh choice
                        while user_choice not in seventh_choice:
                            #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input. 
                            user_choice = input("The door on your right is slightly cracked but the stairs in front of leading to the top of the castle are clear..which way do you go? (right/up)").lower().strip()
                            #user entered first list item in seventh_choice
                            if user_choice == seventh_choice[0]:
                                logging.debug("User typed " + user_choice)
                                seventh_choice_1()
                                #creates a list called eighth_choice that holds choices for user input
                                eighth_choice = ["armor", "wait"]
                                #creates an empty string user_choice
                                user_choice = ""
                                #while loop to continue running until user enters list item from eighth choice
                                while user_choice not in eighth_choice:
                                    #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input. 
                                    user_choice = input("Now is your chance to make a move for Finn...do you put on the armor, grab the weapon, and chance it or hide and wait for the knights to pass (armor/wait)").lower().strip()
                                    if user_choice == eighth_choice[0]:
                                        logging.debug("User typed " + user_choice)
                                        eighth_choice_1()
                                        #creates a list called ninth_choice that holds choices for user input
                                        ninth_choice = ["ask", "walk"]
                                        #creates an empty string user_choice
                                        user_choice = ""
                                        #while loop to continue running until user enters list item from ninth choice
                                        while user_choice not in ninth_choice:
                                            #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input. 
                                            user_choice = input("Do you ask the group of 3 knights or walk by them up the stairs(ask/walk)").lower().strip()
                                            #user entered first list item in ninth_choice
                                            if user_choice == ninth_choice[0]:
                                                logging.debug("User typed " + user_choice)
                                                ninth_choice_1()
                                                #creates a list called tenth_choice that holds choices for user input
                                                tenth_choice = ["salute", "walk"]
                                                #creates an empty string user_choice
                                                user_choice = ""
                                                #while loop to continue running until user enters list item from tenth choice
                                                while user_choice not in tenth_choice:
                                                    #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input. 
                                                    user_choice = input("you thank them for cooperation and send them off with a salute or begin walking towards the back of the castle(salute/walk)").lower().strip()
                                                    if user_choice ==  tenth_choice[0]:
                                                        logging.debug("User typed " + user_choice)
                                                        tenth_choice_1()
                                                        eleventh_choice = ["fight", "talk"]
                                                        #creates an empty string user_choice
                                                        user_choice = ""
                                                        #while loop to continue running until user enters list item from eleventh choice
                                                        while user_choice not in eleventh_choice:
                                                        #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input. 
                                                            user_choice = input("You know your cover is busted at this point, do you attack or try to talk your way out of it?(fight/talk)").lower().strip()
                                                            #user entered first list item in eleventh_choice
                                                            if user_choice == eleventh_choice[0]:
                                                                logging.debug("User typed " + user_choice)
                                                                eleventh_choice_1()
                                                            elif user_choice == eleventh_choice[1]:
                                                                logging.debug("User typed " + user_choice)
                                                                eleventhth_choice_2()
                                                    elif user_choice == tenth_choice[1]:
                                                        logging.debug("User typed " + user_choice)
                                                        tenth_choice_2()
                                                        twelth_choice = ["back", "right"]
                                                        #creates an empty string user_choice
                                                        user_choice = ""
                                                        #while loop to continue running until user enters list item from twelth choice
                                                        while user_choice not in twelth_choice:
                                                            #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input. 
                                                            user_choice = input("You contemplate which route would be better for the success of the mission (back/right)").lower().strip()
                                                            #user entered first list item in twelth_choice
                                                            if user_choice == twelth_choice[0]:
                                                                logging.debug("User typed " + user_choice)
                                                                twelth_choice_1()
                                                                thirteenth_choice = ["dismiss", "help"]
                                                                #creates an empty string user_choice
                                                                user_choice = ""
                                                                #while loop to continue running until user enters list item from thirteenth choice
                                                                while user_choice not in thirteenth_choice:
                                                                    #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input. 
                                                                    user_choice = input("You walk up to them and dismiss them for a break or tell them another officer needs their help in the castle(dismiss/help)").lower().strip()
                                                                    #user entered first list item in thirteenth_choice
                                                                    if user_choice == thirteenth_choice[0]:
                                                                        logging.debug("User typed " + user_choice)
                                                                        thirteenth_choice_1()
                                                                        fourteenth_choice = ["save", "leave"]
                                                                        #creates an empty string user_choice
                                                                        user_choice = ""
                                                                        #while loop to continue running until user enters list item from fourteenth choice
                                                                        while user_choice not in fourteenth_choice:
                                                                        #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input. 
                                                                            user_choice = input("Do you go back and try to save the other captives or leave them behind and make it out with Finn(save/leave)").lower().strip()
                                                                            #user entered first list item in fourteenth_choice
                                                                            if user_choice == fourteenth_choice[0]:
                                                                                logging.debug("User typed " + user_choice)
                                                                                fourteenth_choice_1()
                                                                    elif user_choice == thirteenth_choice[1]:
                                                                        logging.debug("User typed " + user_choice)
                                                                        thirteenth_choice_2()
                                                            elif user_choice == twelth_choice[1]:
                                                                logging.debug("User typed " + user_choice)
                                                                twelth_choice_2()
                                                                fifteenth_choice = ["dismiss", "help"]
                                                                #creates an empty string user_choice
                                                                user_choice = ""
                                                                #while loop to continue running until user enters list item from fifteenth choice
                                                                while user_choice not in fifteenth_choice:
                                                                    #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input. 
                                                                    user_choice = input("You walk up to them and dismiss them for a break or tell them another officer needs their help in the castle(dismiss/help)").lower().strip()
                                                                    #user entered first list item in fifteenth_choice
                                                                    if user_choice == fifteenth_choice[0]:
                                                                        logging.debug("User typed " + user_choice)
                                                                        fifteenth_choice_1()
                                                                        sixteenth_choice = ["save", "leave"]
                                                                        #creates an empty string user_choice
                                                                        user_choice = ""
                                                                        #while loop to continue running until user enters list item from sixteenth choice
                                                                        while user_choice not in sixteenth_choice:
                                                                        #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input. 
                                                                            user_choice = input("Do you go back and try to save the other captives or leave them behind and make it out with Finn(save/leave)").lower().strip()
                                                                            #user entered first list item in sixteenth_choice
                                                                            if user_choice == sixteenth_choice[0]:
                                                                                logging.debug("User typed " + user_choice)
                                                                                sixteenth_choice_1()
                                                                            elif user_choice == sixteenth_choice[1]:
                                                                                logging.debug("User typed " + user_choice)
                                                                                sixteenth_choice_2()
                                                                    elif user_choice == fifteenth_choice[1]:
                                                                        logging.debug("User typed " + user_choice)
                                                                        fifteenth_choice_2()
                                            elif user_choice == ninth_choice[1]:
                                                logging.debug("User typed " + user_choice)
                                                ninth_choice_2()
                                                twelth_choice = ["back", "right"]
                                                #creates an empty string user_choice
                                                user_choice = ""
                                                #while loop to continue running until user enters list item from twelth choice
                                                while user_choice not in twelth_choice:
                                                    #takes input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input
                                                    user_choice = input("You contemplate which route would be better for the success of the mission (back/right)").lower().strip()
                                                    #user entered first list item in twelth_choice
                                                    if user_choice == twelth_choice[0]:
                                                        logging.debug("User typed " + user_choice)
                                                        twelth_choice_1()
                                                        thirteenth_choice = ["dismiss", "help"]
                                                        #creates an empty string user_choice
                                                        user_choice = ""
                                                        #while loop to continue running until user enters list item from thirteenth choice
                                                        while user_choice not in thirteenth_choice:
                                                            #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input
                                                            user_choice = input("You walk up to them and dismiss them for a break or tell them another officer needs their help in the castle(dismiss/help)").lower().strip()
                                                            #user entered first list item in thirteenth_choice
                                                            if user_choice == thirteenth_choice[0]:
                                                                logging.debug("User typed " + user_choice)
                                                                thirteenth_choice_1()
                                                                #creates a list called fourteenth_choice that holds choices for user input
                                                                fourteenth_choice = ["save", "leave"]
                                                                #creates an empty string user_choice
                                                                user_choice = ""
                                                                #while loop to continue running until user enters list item from fourteenth choice
                                                                while user_choice not in fourteenth_choice:
                                                                    #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input
                                                                    user_choice = input("Do you go back and try to save the other captives or leave them behind and make it out with Finn(save/leave)").lower().strip()
                                                                    #user entered first list item in fourteenth_choice
                                                                    if user_choice == fourteenth_choice[0]:
                                                                        logging.debug("User typed " + user_choice)
                                                                        fourteenth_choice_1()
                                                                    elif user_choice == fourteenth_choice[1]:
                                                                        logging.debug("User typed " + user_choice)
                                                                        fourteenth_choice_2()
                                                            elif user_choice == thirteenth_choice[1]:
                                                                logging.debug("User typed " + user_choice)
                                                                thirteenth_choice_2()
                                                    elif user_choice == twelth_choice[1]:
                                                        logging.debug("User typed " + user_choice)
                                                        twelth_choice_2()
                                                        fifteenth_choice = ["dismiss", "help"]
                                                        #creates an empty string user_choice
                                                        user_choice = ""
                                                        #while loop to continue running until user enters list item from fifteenth choice
                                                        while user_choice not in fifteenth_choice:
                                                            #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input
                                                            user_choice = input("You walk up to them and dismiss them for a break or tell them another officer needs their help in the castle(dismiss/help)").lower().strip()
                                                            if user_choice == fifteenth_choice[0]:
                                                                logging.debug("User typed " + user_choice)
                                                                fifteenth_choice_1()
                                                                sixteenth_choice = ["save", "leave"]
                                                                #creates an empty string user_choice
                                                                user_choice = ""
                                                                #while loop to continue running until user enters list item from sixteenth choice
                                                                while user_choice not in sixteenth_choice:
                                                                #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input
                                                                    user_choice = input("Do you go back and try to save the other captives or leave them behind and make it out with Finn(save/leave)").lower().strip()
                                                                    #user entered first list item in sixteenth_choice
                                                                    if user_choice == sixteenth_choice[0]:
                                                                        logging.debug("User typed " + user_choice)
                                                                        sixteenth_choice_1()
                                                                    elif user_choice == sixteenth_choice[1]:
                                                                        logging.debug("User typed " + user_choice)
                                                                        sixteenth_choice_2()
                                                            elif user_choice == fifteenth_choice[1]:
                                                                logging.debug("User typed " + user_choice)
                                                                fifteenth_choice_2()
                                    elif user_choice == eighth_choice[1]:
                                        logging.debug("User typed " + user_choice)
                                        eighth_choice_2()
                            elif user_choice == seventh_choice[1]:
                                logging.debug("User typed " + user_choice)
                                seventh_choice_2()
                                twelth_choice = ["back", "right"]
                                #creates an empty string user_choice
                                user_choice = ""
                                #while loop to continue running until user enters list item from twelth choice
                                while user_choice not in twelth_choice:
                                    #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input
                                    user_choice = input("You contemplate which route would be better for the success of the mission (back/right)").lower().strip()
                                    #user entered first list item in twelth_choice
                                    if user_choice == twelth_choice[0]:
                                        logging.debug("User typed " + user_choice)
                                        twelth_choice_1()
                                        thirteenth_choice = ["distract", "sneak"]
                                        #creates an empty string user_choice
                                        user_choice = ""
                                        #while loop to continue running until user enters list item from thirteenth choice
                                        while user_choice not in thirteenth_choice:
                                            #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input
                                            user_choice = input("You see an opportunity to attempt to distract them and make a dash for the dungeon entrance or attempt to sneak around(distract/sneak)").lower().strip()
                                            #user entered first list item in thirteenth_choice
                                            if user_choice == thirteenth_choice[0]:
                                                logging.debug("User typed " + user_choice)
                                                thirteenth_choice_1()
                                                fourteenth_choice = ["save", "leave"]
                                                #creates an empty string user_choice
                                                user_choice = ""
                                                #while loop to continue running until user enters list item from fourteenth choice
                                                while user_choice not in fourteenth_choice:
                                                #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input
                                                    user_choice = input("Do you go back and try to save the other captives or leave them behind and make it out with Finn(save/leave)").lower().strip()
                                                    #user entered first list item in fourteenth_choice
                                                    if user_choice == fourteenth_choice[0]:
                                                        logging.debug("User typed " + user_choice)
                                                        fourteenth_choice_1()
                                                    elif user_choice == fourteenth_choice[1]:
                                                        logging.debug("User typed " + user_choice)
                                                        fourteenth_choice_2()
                    elif user_choice == sixth_choice[1]:
                        logging.debug("User typed " + user_choice)
                        sixth_choice_2()
                        print("You keep running and head down into the cellar, you know this has to lead to captives and Finn.")
                        #creates a list called seventeenth_choice that holds choices for user input
                        seventeenth_choice = ["right", "left"]
                        #creates an empty string user_choice
                        user_choice = ""
                        #while loop to continue running until user enters list item from seventeenth choice
                        while user_choice not in seventeenth_choice:
                            #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input. 
                            user_choice = input("You continue running forward and reach a split in the tunnels...there is a right path and a left path (right/left)").lower().strip()
                            #user entered first list item in seventeenth_choice
                            if user_choice == seventeenth_choice[0]:
                                logging.debug("User typed " + user_choice)
                                seventeenth_choice_1()
                            elif user_choice == seventeenth_choice[1]:
                                logging.debug("User typed " + user_choice)
                                seventeenth_choice_2()
            elif user_choice == fifth_choice[1]:
                fifth_choice_2()
                eighteenth_choice = ["run", "stay"]
                #creates an empty string user_choice
                user_choice = ""
                #while loop to continue running until user enters list item from eighteenth choice
                while user_choice not in eighteenth_choice:
                    #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input. 
                    user_choice = input("Your wound is bleeding bad and running might worsen the damage but staying put could get you killed..so you..(run/stay)").lower().strip()
                    if user_choice == eighteenth_choice[0]:
                        logging.debug("User typed " + user_choice)
                        eighteenth_choice_1()
                        seventeenth_choice = ["right", "left"]
                        #creates an empty string user_choice
                        user_choice = ""
                        #while loop to continue running until user enters list item from seventeenth choice
                        while user_choice not in seventeenth_choice:
                            #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input. 
                            user_choice = input("You continue running forward and reach a split in the tunnels...there is a right path and a left path (right/left)").lower().strip()
                            #user entered first list item in seventeenth_choice
                            if user_choice == seventeenth_choice[0]:
                                logging.debug("User typed " + user_choice)
                                seventeenth_choice_1()
                            elif user_choice == seventeenth_choice[1]:
                                logging.debug("User typed " + user_choice)
                                seventeenth_choice_2()
                    elif user_choice == eighteenth_choice[1]:
                        logging.debug("User typed " + user_choice)
                        eighteenth_choice_2()
    elif user_choice == fourth_choice[1]:
        logging.debug("User typed " + user_choice)
        fourth_choice_2()
        nineteenth_choice = ["rocks", "water"]
    #creates an empty string user_choice
        user_choice = ""
        #while loop to continue running until user enters list item from nineteenth choice
        while user_choice not in nineteenth_choice:
            #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input. 
            user_choice = input("Do you try to find rocks to cross or just chance it and swim through the water? (rocks/water)").lower().strip()
            if user_choice == nineteenth_choice[0]:
                logging.debug("User typed " + user_choice)
                nineteenth_choice_1()
            elif user_choice == nineteenth_choice[1]:
                logging.debug("User typed " + user_choice)
                nineteenth_choice_2()
