# Author	:	Darshan R
# Date		:	2014-04-14	
# Rock-paper-scissors-lizard-Spock Game
import random

# helper functions

def name_to_number(name):
    
    # convert name to number
    if name == 'rock' :
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
       return 3
    elif name == 'scissors':
        return 4
    
    


def number_to_name(number):
    # convert number to a name
    if number == 0 :
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
       return 'lizard'
    elif number == 4:
        return 'scissors'
    
# main function to perform game functionalities
def rpsls(player_choice): 
   
   # a blank line to separate consecutive games
    print
    # print out the message for the player's choice
    print "Player chooses",player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses",comp_choice
    # compute difference of comp_number and player_number modulo five
    difference = (player_number - comp_number) % 5
 
    # Determine winner and print winner message
    if (difference == 1 or difference == 2):
        print "Player Wins!"
    elif (difference == 3 or difference == 4):
        print "Computer Wins!"
    else :
        print "Player and computer tie!!"
    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
