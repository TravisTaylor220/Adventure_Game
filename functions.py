#Functions used in Text-based adventure game for final project INF360

class Player:
    def __init__ (self):
        self.getname()
        self.getweapon()
        self.health = 100


    def getname(self):
        while True:
            print("What is your name soldier!?!")
            name = input("Name: ")
            if not name.istitle():
                print("That is not you name! Tell me your name!")
            else:
                self.name = name
                break

    def getweapon(self):
        while True:
            print("What is your weapon of choice?")
            weapon = input("Weapon: ").lower()
            self.weapon = weapon
            break



player = Player()

def start_game():
    first_choice = ["yes","no"]
    #creates an empty string user_choice
    user_choice = ""
    #while loop to continue running until user enters list item from first choice
    while user_choice not in first_choice:
        print("Welcome to Finding Finn")
        print("The game grants your character, " + player.name + ", 100 health and ability to use your " + player.weapon + ". Your goal is to find Finn and escape his captors.")
        #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input. 
        user_choice = input("Would you like to take an adventure through the swamps of Llavonnine to try and save Finn Glery (yes/no)").lower().strip()
        if user_choice == first_choice[0]:
            #function call to the story intro
            story_intro()
            print("")
        elif user_choice == first_choice[1]:
            print("You missed an opportunity to save Finn in my adventure game. Sorry you did not want to play. Goodbye!")
            #asks the user if they want to exit the game
            quit()

#Function created to hold the story intro
def story_intro():
    print("Darkness begins to descend on the trail, moonlight beaming through foliage")
    print("lighting the mud tattered path through the marsh.")
    print("You ponder what could have happened to Finn...")
    print("Did the cavalry capture him along with the rest of the village?")
    print("More and more scenarios begin to fill your head..why would someone take a high ranking officer.")
    print("You know you must complete your mission of rescuing Finn.")
    print("The darkness has now overtaken the forest and you decide to set up camp.")
    print("You find a quiet place under a willow tree to conceal your location for the night")
    print('..."CRACK"...you are awoken from a large branch being snapped near your campsite.')
    print("You look around at your surroundings and panic begins to set in.")

def second_choice():
    second_choice = ["fight", "hide"]
    #creates an empty string user_choice
    user_choice = ""
    #while loop to continue running until user enters list item from second choice
    while user_choice not in second_choice:
        #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input. 
        user_choice = input("You notice a club-like branch laying on the ground..do you grab the branch or do you hide behind the tree? (fight/hide)").lower().strip()
        if user_choice == second_choice[0]:
            second_choice_1()
        elif user_choice == second_choice[1]:
            second_choice_2()

def second_choice_1():
    print("")
    print("You pick up the branch and get ready for the threat...you hear them coming closer and closer")
    print("3...2...1...")
    print("You step out and see 2 knights lagging behind the group that captured everyone.")
    print("BANG..you knock the first one out with ease and the second is now ready to fight..")
    print("The fight begins and after several minutes you emerge victorious but not without a few battle wounds.")
    #max health went from 100 to 90
    player.health -= 10
    print("You have lost 10 health, your health is now " + str(player.health))
    print("You tend to your wounds and daylight begins to emerge through the trees.")


def second_choice_2():
    print("")
    print("you hide in the tree above your campsite as the knights approach.")
    print("The knights notice the fire has recently been lit and is freshly made..")
    print("They begin to think they are being followed and start searching the surrounding area.")
    print("The search on the ground has turned up nothing but one knight glances up and sees your foot hanging out of the tree")
    print("He reaches up and rips you out of the tree with ease..they grab you and take you as their prisoner now")
    print("You failed your mission..Finn and the captives are never seen again..")
    #asks the user if they want to exit the game
    quit()

def third_choice():
    #creates a list called third_choice that holds choices for user input
    third_choice = ["run", "walk"]
    #creates an empty string user_choice
    user_choice = ""
    #while loop to continue running until user enters list item from third choice
    while user_choice not in third_choice:
        #takes user input and makes all input lowercase and removes whitespaces to further prevent user error and prompt wrong input. 
        user_choice = input("You know the cavalry have to be close to reaching the castle, that would be the end of Finn..do you run to try and catch the knights or continue walking? (run/walk)").lower().strip()
        if user_choice == third_choice[0]:
            third_choice_1()
        elif user_choice == third_choice[1]:
            third_choice_2()

#def third_choice_1():
def third_choice_1():
    print("")
    print("You start running down the path and see the cavalry over the horizon but you feel a sharp pain in your leg and the cut has reopened from your fight")
    #max health went from 90 to 85
    player.health -= 5
    print("You lose 5 health, your health is now " + str(player.health))
    print("You fight through the pain and continue down the path")
    print("and you see them less than 100 yards infront of you but the castle is in sight!")
    print("They begin to cross the drawbridge and you see an opportunity to get in the castle")

def third_choice_2():
    print("")
    print("You continue walking knowing hoping to see the cavalry")
    print("The night grows darker and you continue walking and still have yet to see them..")
    print("You begin to question whether you lost them or took a wrong route through the marsh.")
    print("You never find the cavalry or the castle and eventually have to give up and return to the king.")
    print("You failed your mission..Finn and the captives are never seen again..")
    #asks the user if they want to exit the game
    quit()


def fourth_choice_1():
    print("")
    print("You dash across the drawbridge hoping nobody saw you..")
    print("")
    print("it looks like you are in the clear...then you hear a loud voice coming from the top of the wall")
    print("you look up quickly and see a knight with his bow drawn pointing directly at you")

def fourth_choice_2():
    print("")
    print("you see the drawbridge being raised and know you know missed your opportunity.")
    print("You have to sneak around the castle and try to find an entry point.")
    print("The moat posses a problem too..you need to find a way across avoiding the alligators in the water..")
    print("You notice a large crack in the wall so you have a decision to make..")


def fifth_choice_1():
    print("")
    print("You roll out of the way and narrowly avoid his shot!")
    print("you start running next the wall and notice stairs that lead up into the castle or down into the cellars")

def fifth_choice_2():
    {}

def sixth_choice_1():
    print("")
    print("The stairs leading up look promising so you sprint up them and make a right turn into the castle")
    print("but you hear the knights voices getting louder and louder so you continue running down the hall.")

def sixth_choice_2():
    {}

def seventh_choice_1():
    print("")
    print("You sneakily open the rightside door and notice it looks like the room of a high ranking knight with his set of armor placed on the wall")
    print("The armor looks like it would fit you well enough to sneak past and grab Finn with the rest of the captives")

def seventh_choice_2():
    {}

def eighth_choice_1():
    print("")
    print("The armor seems to fit and you walk back into the hallway")
    print("The cavalry is walking right towards you but you need to know where Finn and the captives are being held")

def eighth_choice_2():
    {}

def ninth_choice_1():
    print("")
    print('"Hey, where have we taken the captives to be held" you ask...')
    print("")
    print('after a small pause they respond "Umm where we keep all the other captives sire, at the rear of the castle in the dungeon"')

def ninth_choice_2():
    print("")
    print("You walk by them without saying a word and continue up the stairs")
    print("You need to find where the captives are being held..you continue walking upstairs until you reach the top of the castle.")
    print("You overlook the surrounding buildings and happen to catch them escorting Finn into a building in the very back.")
    print("You lucked out and need to make your move asap...you dont know how long Finn and the captives have now...")
    #creates a list called twelth_choice that holds choices for user input
    print("You move swiftly down the stairs and head out to the back of the castle")

def tenth_choice_1():
    print("")
    print('"Hey, where have we taken the captives to be held" you ask...')
    print("")
    print('after a small pause they respond "Umm where we keep all the other captives sire, at the rear of the castle in the dungeon"')

def tenth_choice_2():
    print("")
    print("A quick turn and you begin walking towards the rear of the castle so you can begin to plot the rescue of Finn.")
    print("You take the stairs infront of you to get a birdseye view of the surrounding area.")
    print("You notice the swamp grows thick behind the dungeon and it could be difficult for everyone to get out but a definite escape for you and Finn.")
    print("Although...you could try and take everyone through the open field to the right leading back to the path through the marsh but that comes with a larger risk")

def eleventh_choice_1():
    print("")
    print("You unsheath your " + player.weapon + " threatening the 3 knights...warning them to not take a step towards you..")
    print("They look at you with such little respect and make their move..you cut the first one down and the other two continue coming forward")
    print("You slash at the next knight but he parries and slashes across your armor leaving a 4 inch gash upon your right arm...")
    #max health is reduced to 50 from 85
    player.health -= 35
    print("You lose 35 health, your health is now " + str(player.health))
    print("you feel your glove begin filling up with blood and your grip begins to loosen on your " + player.weapon)
    print("you look up and see the second knight stepping towards you to finish you but you swing your " + player.weapon + "  in an unpward motion")
    print("catching him off guard and killing him in one blow....but not without taking another blow to your left shoulder..you collapse to your knees")
    print("your adrenaline is in overdrive now due to the immense pain...you have lost feeling in your right arm and your shoulder has been split open.")
    print("This can't be it you murmur to yourself...planting the " + player.weapon + "  in the ground and lifting yourself to your feet.")
    print("The knight points his " + player.weapon + "  at you as if this was childsplay to him..he swipes across your body but you parry it with the strength you have left.")
    print("He swings again...another parry...and again...and again...you fall to your knees in defeat")
    print('He looks at you and chuckles..."Was it all worth it...worth dying for" he scoffs...')
    print("He grabs your shoulder and squeezes it and you let out a shriek and he throws you to the ground.")
    print("He takes his " + player.weapon + "  and thrusts it into your back leaving to bleed out and die in the spot")
    #reduces max health by 50 to 0 ending the game
    player.health -= 50
    print("you continue bleeding out, losing 50 health...your health is now " + str(player.health) + " and you die in that spot...")
    print("You have failed the mission and did not save Finn and the captives")
    #asks the user if they want to exit the game
    quit()

def eleventhth_choice_2():
    print("")
    print('You look at them with conviction and tell them "You show little for a captian? I\'ll have your head for this disrepect!"')
    print("Your attempt was futile at best...they scoff at your pathetic self..")
    print('"We have the intruder!" they yell...grabbing you by the arm and escorting you to the dungeon along with everyone else, including your target Finn.')
    print("You know your run is over and you have failed the mission...")
    #Ends the players game, they have lost    
    #asks the user if they want to exit the game
    quit()

def twelth_choice_1():
    print("")
    print("The back route would be a more successful route to rescue Finn...I have to ensure he makes it out alive.")
    print("You make your way back down the stairs and begin moving towards the dungeon in the rear of the castle.")
    print("You notice guards near the dungeon entrance..you know you need to get them to leave their post so you can sneak them out..")

def twelth_choice_2():
    print("")
    print("You decide to try and get everyone out as fast as possible though the field..")
    print("You make your way back down the stairs and begin moving towards the dungeon in the rear of the castle.")
    print("You notice guards near the dungeon entrance..you know you need to get them to leave their post so you can sneak them out..")

def thirteenth_choice_1():
    print("")
    print('"Knights! Youre dismissed..I will keep this post for the rest of the evening" you commannd.')
    print("They look at you with gratitude and accept the break. You realise your opportunity to try to get everyone out is soon.")
    print("Dusk is starting to fall upon the castle..you make your way to the dungeon and find Finn and the captives.")
    print("You know your chance is now...you break the lock off the gate with your " + player.weapon + "  and you find Finn")
    print('"WE HAVE TO GO NOW! EVERYONE OUT THE BACK TOWARDS THE THICK MARSH!" you yell..making sure Finn is the first person out')
    print('Everyone makes it the thick area and you hear the guards yell "THE CAPTIVES...THEYRE GONE..FIND THEM NOW!"')
    print("The guards begin charging towards the thicket after noticing some captives lagging behind...")
    print("They are hot on your trail and you are caught in between ensuring the safety between Finn and trying to escort everyone out")

def thirteenth_choice_2():
    print("")
    print('You tell them another officer needs their help and they look confused..."another officer? which one captain?"')
    print("You hesitate and tell them you are unsure..just go up to the castle and go to the front, he was up there")
    print('They look at you with more confusion "Give us his name captain" they pressure..you dont know what to say')
    print('"He is upfront, just go see him" you respond..."go now!"')
    print('They ignore your attempt "No and I am starting to believe you are not even a captain" they reply')
    print('"What is your name" they demand, not accepting your attempt to talk around the issue, drawing their ' + player.weapon + '  and holding it to your neck')
    print("You have no response and draw your " + player.weapon + " ..they both attack at the same time!")
    print("You take a lethal blow to your shoulder, disabling your " + player.weapon + "  arm...")
    #reduces player health from 85 to 45
    player.health -= 40
    print("You lose 40 health, your health is now " + str(player.health))
    print("With one swift blow, they remove your other arm")
    #reduces player health from 45 to 0
    player.health -= 45
    print("You lose 45 health, your health is now " + str(player.health))
    print("You bleed out right there and fail the mission..")
    #Ends the program because player health reached 0
    #asks the user if they want to exit the game
    quit()

def fourteenth_choice_1():
    print("")
    print("You turn and see the knights attacking the innocent captives...you charge the knights and begin attacking!")
    #reduces max health from 85 to 35
    player.health -= 50
    print("you cut one knight down and another but out of nowhere..an arrow pierces your chestpiece..dropping you to your knees")
    print("You lose 50 health, your health is now " + str(player.health))
    print("They see you are wounded and rush you, you stand up and look over your shoulder and nod to Finn to get everyone out")
    #reduces max health by 35 to 0 ending the game
    player.health -= 35
    print("He nods back in agreeance...you look back to the enemy and charge..you swing with precision and slice the first, the second, the third guy down but eventually are hit with multiple arrows")
    print("You lose 35 health, your health is now " + str(player.health))
    print("You fall but not without a valiant effort...you have tried and succeeded on getting everyone out but not without costing you your life...")
    print("")
    print("Congrats! You have won the game and saved Finn and the rest of the captives!")
    #asks the user if they want to exit the game
    quit()

def fourteenth_choice_2():
    print("")
    print("You look back and see the other captives getting killed but you stay true to your mission.")
    print("You know you cannot help them so you grab Finn and vanish into the thicket but not without sacrifice")
    print("Congratulations, you have succeeded in your mission and saved Finn")
    #asks the user if they want to exit the game
    quit()

def fifteenth_choice_1():
    print("")
    print('"Knights! Youre dismissed..I will keep this post for the rest of the evening" you commannd.')
    print("They look at you with gratitude and accept the break. You realise your opportunity to try to get everyone out is soon.")
    print("Dusk is starting to fall upon the castle..you make your way to the dungeon and find Finn and the captives.")
    print("You know your chance is now...you break the lock off the gate with your " + player.weapon + "  and you find Finn")
    print('"WE HAVE TO GO NOW! EVERYONE TOWARDS THE FIELD!" you yell..making sure Finn is the first person out')
    print('Everyone starts running through the field but is left unprotected and you hear the guards yell "THE CAPTIVES...THEYRE GONE..FIND THEM NOW!"')
    print("The guards on top of the castle see everyone running through the field and begin firing arrows volley style into the captives.")
    print("The knights begin running from the castle on foot as well...")
    print("People are getting hit all over the place but Finn is still alive and running...you see other captives crying for help but your mission is Finn..")

def fifteenth_choice_2():
    print("")
    print('You tell them another officer needs their help and they look confused..."another officer? which one captain?"')
    print("You hesitate and tell them you are unsure..just go up to the castle and go to the front, he was up there")
    print('They look at you with more confusion "Give us his name captain" they pressure..you dont know what to say')
    print('"He is upfront, just go see him" you respond..."go now!"')
    print('They ignore your attempt "No and I am starting to believe you are not even a captain" they reply')
    print('"What is your name" they demand, not accepting your attempt to talk around the issue, drawing their ' + player.weapon + '  and holding it to your neck')
    print("You have no response and draw your " + player.weapon + " ..they both attack at the same time!")
    print("You take a lethal blow to your shoulder, disabling your " + player.weapon + "  arm...")
    #reduces player health from 85 to 45
    player.health -= 40
    print("You lose 40 health, your health is now " + str(player.health))
    print("With one swift blow, they remove your other arm")
    #reduces player health from 45 to 0
    player.health -= 45
    print("You lose 45 health, your health is now " + str(player.health))
    print("You bleed out right there and fail the mission..")
    #Ends the program because player health reached 0
    #asks the user if they want to exit the game
    quit()

def sixteenth_choice_1():
    print("")
    print("You turn and see the knights attacking the innocent captives...you charge the knights and begin attacking!")
    #reduces max health from 85 to 35
    player.health -= 50
    print("you cut one knight down and another but out of nowhere..an arrow pierces your chestpiece..dropping you to your knees")
    print("You lose 50 health, your health is now " + str(player.health))
    print("They see you are wounded and rush you, you stand up and look over your shoulder and nod to Finn to get everyone out")
    #reduces max health from 85 to 35
    #reduces max health by 35 to 0 ending the game
    player.health -= 35
    print("He nods back in agreeance...you look back to the enemy and charge..you swing with precision and slice the first, the second, the third guy down but eventually are hit with multiple arrows")
    print("You lose 35 health, your health is now " + str(player.health))
    print("You fall but not without a valiant effort...you have tried and succeeded on getting everyone out but not without costing you your life...")
    print("")
    print("Congrats! You have won the game and saved Finn and the rest of the captives!")
    #asks the user if they want to exit the game
    quit()    

def sixteenth_choice_2():
    print("")
    print("You look back and see the other captives getting killed but you stay true to your mission.")
    print("You know you cannot help them so you grab Finn and vanish into the thicket but not without sacrifice")
    print("Congratulations, you have succeeded in your mission and saved Finn")
    #asks the user if they want to exit the game
    quit()

def seventeenth_choice_1():
    print("")
    print("You take the right path without second thought!")
    print("You hear women and children screaming and yelling...you know the captives have to be down this way!")
    print("you start running down the tunnel and when you get to the dungeon entrance, you cant seem to unlock the gate.")
    print("You panic...you frantically start looking around for a way out with none in sight..")
    print("You hear the knights getting closer and no there is no way for you to get out of this scenario.")
    print("They capture you and place you with the captives...you have failed your mission.")
    #asks the user if they want to exit the game
    quit()

def seventeenth_choice_2():
    print("")
    print("you sprint to the left hoping no one saw you!")
    print("You keep running and running and reach a fake gate...")
    print("there is no possible way of opening it and you feel defeated..")
    print("you have went too far into the tunnel and are lost..you cant find your way out.")
    print("You fail the mission...you never reach the captives and Finn is not rescued.")
    #asks the user if they want to exit the game
    quit()

def eighteenth_choice_1():
    print("You decide to run but when you do, you see a group of knights blocking the exit...you make a quick turn into the cellar entry and begin running down the tunnel")
    print("You see the end of the tunnel but it splits near the end into two different directions.")

def eighteenth_choice_2():
    print("")
    print("You decide to risk it and try to stay hidden. They keep getting closer and closer because of the blood loss")
    print("You cant move at this point as you have loss too much blood. The turn the corner and see you laying in your own blood still breathing")
    print("The grab you by the back and throw you onto the ground and execute you on the spot.")
    print("You fail the mission...you never reach the captives and Finn is not rescued.")
    #asks the user if they want to exit the game
    quit()

def nineteenth_choice_1():
    print("")
    print("You continue sneaking around and notice the rocks seem to form a little bridge.")
    print("That seems like your chance! You cross it with ease but cant seem to find an entrance point.")
    print("You continue searching along the wall and finally find a crack leading into the dungeon.")
    print("You enter the large crack in the back of the dungeon and sneak right in..")
    print("Now you need to find a way to break the lock and escort Finn and the captives out")
    print("You know your chance is now...you try to break the lock off the gate with a large stone next to the gate and you find Finn.")
    print("BANG..BANG...BANG..The rock will not break the lock..you try once more and no success..")
    print("You see the knights smash through the door with bows drawn!")
    print('"GET HIM" they yell..firing their bow and striking you in the back..')
    #reduces player health from 85 to 45
    player.health -= 40
    print("You lose 40 health, your health is now " + str(player.health))
    print("With one last shot, they hit you in the back once more...")
    #reduces player health from 45 to 0
    player.health -= 45
    print("You lose 45 health, your health is now " + str(player.health))
    print("You bleed out right there and fail the mission..")
    #Ends the program because player health reached 0
    #asks the user if they want to exit the game
    quit()

def nineteenth_choice_2():
    print("")
    print("You attempt to cross the water but the alligators sense your presence in the water.")
    print("They rush you and are able to get you before you are able to cross the moat..")
    print("You are killed by the alligators and fail the mission.")
    print("Finn and the captives are never seen again..")
    #asks the user if they want to exit the game
    quit()
