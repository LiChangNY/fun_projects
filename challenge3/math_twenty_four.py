import itertools, random
from termcolor import colored

#random shuffle deck and throw four cards
def throw_cards(deck):
    random.shuffle(deck)
    cards_thrown = []
    for i in range(4):
        cards_thrown.append(deck[i])
    return cards_thrown

#ckeck against player's solution    
def check(player_solution, cards_thrown):
    
    #check if the same numbers assigned are used in solution
    solution_number = [int(s) for s in player_solution if s.isdigit()]
    cards_number = [n for i, (n, l) in enumerate(cards_thrown)]
        
    if sorted(solution_number) != sorted(cards_number):
        print colored("Invalid entry.\
                      \nCards are returned back to the deck.", 'red')
        return False
    
    #check if the solution returns 24
    try:
        if eval(player_solution) == 24:
            return True
    except:
        1

    print colored("Your solution doesn't return 24.\
                  \nCards are returned back to the deck. \n", 'red')       
    return False    

#summarize points
def scoring(player_one, player_two, players):
    print colored("\nCards gained: %s: %i vs. %s: %i\n\n" % (\
          player_one, len(players['a']['cards_gained']), \
          player_two, len(players['l']['cards_gained'])
          ), 'blue') 

#exit game early
def end():
    print colored("Okay, laters", 'blue')
    exit()
    
##############################################################################
#**********************READ GAME INSTRUCTOINS********************************#    
print colored("This is a simple mental arithmetic game between TWO players. \
I will throw four cards (out of 36 cards in total) from 1-9 and your goal is \
to manipulate these four numbers to achieve 24 by using addition, \
subtraction, multiplication or division. \
\n\nEvery card can be used only once in your equation. For example, \
if you are given 6,2,3,3, you should type in (3-2+3)*6 or (6-2)*(3+3). \
Player 1 presses 'A' and Player 2 'L' to compete for the rights to try the \
cards, and whose letter shows up first on the screen earns the rights to answer.\
\n\nYou only have one chance to type in your solution to prevent you from  \
gaming. If anything goes wrong, the cards will be taken back to the deck.\
If your solution works, you will gain those four cards.\
The game culminates when the deck is exhausted and whoever \
has more cards wins the game. \n \n", 'blue') 
#****************************************************************************#
##############################################################################

#get players' name info
player_one = raw_input("Enter the name of player One: ")
print "Welcome, %s! You should press 'A' as soon as you \
      \nhave the answer.\n" % player_one
player_one_cards = []
player_two = raw_input("Enter the name of player Two: ")
print "Welcome, %s! You should press 'L' as soon as you \
      \nhave the answer.\n" % player_two
player_two_cards = []

players = {"a": {'name':player_one, 'cards_gained':[]},
           "l": {'name':player_two, 'cards_gained': []}}   

#check if players are ready to play
ready_to_play = raw_input("Ready to play? Y/N: " )

while ready_to_play.lower() not in ['y', 'n']:
    print colored("Not sure what you wanted. Press Y to play or N to exit. \n",
                  "red")
    ready_to_play = raw_input("Ready to play? Y/N: " )
    
if ready_to_play.lower() == "n":
    end()
    
else:
    #initiate card deck
    deck = list(itertools.product(\
           range(1,10),['Spade','Heart','Diamond','Club']))
    #keep throwing cards until it's exhausted
    while len(deck) >= 4: 
        
        #throw 4 cards from the existing deck
        cards_thrown = throw_cards(deck)  
        print colored(cards_thrown, 'blue')
        print 
        
        #compete for rights to try the solution
        message = "-%s, type 'A', \
                  \n-%s, type 'L',  \
                  \n-press ENTER to try four new cards, \
                  \n-type 'END' to quit the game: " % (\
                  player_one, player_two)
        rights = raw_input(message)
        
        #exit game 
        if rights.lower() == 'end':
            end()
   
        #give new cards if enters nothing
        if len(rights)== 0:
            print colored("\nCards sare returned back.\n", 'red')
            continue
        #check if players used wrong keys
        if rights[0].lower() not in players.keys(): 
            print colored("\nWrong key used. Cards sare returned back.\n", 'red')
            continue
        
        player_rights = players[rights[0].lower()]['name']
          
        #get the solution        
        print "\nLooks like %s got the right to answer \n" % player_rights         
        message_for_inputs = "%s, enter your solution here: " % player_rights
        player_solution = raw_input(message_for_inputs)
                
        #check if the solution meets expectation
        if check(player_solution, cards_thrown) is False:
            continue
        else: 
            print colored("Great job, %s.\n \n " % player_rights, 'green')  
            #remove cards from the existing deck
            for i in cards_thrown:
                deck.remove(i)
                
            #give these four cards to the player who gets the right solution
            players[rights[0].lower()]['cards_gained']=\
            players[rights[0].lower()]['cards_gained'] + cards_thrown
            scoring(player_one, player_two, players)
            
    #summarize players' points
    print "Final scores:"        
    scoring(player_one, player_two, players)
             
    


