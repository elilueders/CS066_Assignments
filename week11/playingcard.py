import random

class PlayingCard:
    
    def __init__(self,v,s):
        
        if type(v) != type(1) or v > 14 or v < 2:
            raise Exception("A PlayingCard's value must be an integer in the range 2-14.")
        self.__value = v
        self.__suit = s
        
    def __repr__(self):
        printval = self.__value
        if self.__value == 11:
            printval = "J"
        elif self.__value == 12:
            printval = "Q"
        elif self.__value == 13:
            printval = "K"
        elif self.__value == 14:
            printval = "A"
        return str(printval)+str(self.__suit)
    
    def __lt__(self,other):
        if self.__value < other.__value:
            return True
        else:
            return False
        
class Deck:
    
    def __init__(self):
        self.__card_list = []  #the deck will be initially empty

    def __repr__(self):
        return str(self.__card_list)
        
        
    def put_on_top(self,card):
        self.__card_list.append(card)
        
    def remove_from_top(self):
        if len(self.__card_list) == 0:
            raise Exception("This deck has no cards left.")
        else:
            return self.__card_list.pop()
    
    def shuffle(self):
        random.shuffle(self.__card_list) 
    
    def is_empty(self):
        return self.__card_list == []

#Game
#Game
high_card_deck = Deck()

#create each of the 52 playing cards and put them in the deck
suits = ["♠","♣","♡","♢"]
for s in suits:
    for v in range(2,15):
        curr_card = PlayingCard(v,s)
        high_card_deck.put_on_top(curr_card)
        
#look at the deck both before and after shuffling        
print("Here's the pre-shuffled deck:",high_card_deck)
high_card_deck.shuffle()
print("Here's the deck after the shuffle:",high_card_deck)


p1score = 0
p2score = 0


#keep going until all cards are dealt out
while not high_card_deck.is_empty():
    
    #draw a card for each player
    p1card = high_card_deck.remove_from_top()
    p2card = high_card_deck.remove_from_top()
    
    print("Player 1:",p1card,", Player 2:",p2card)
    
    #check which player wins this hand
    if p1card < p2card:
        p1score += 1
        print("Player 1 wins this hand.")
    elif p1card > p2card:
        p2score += 1
        print("Player 2 wins this hand.")
    else:
        print("This hand is a draw.")
        
        
#Figure out who wins and display the game-end message
print("Player 1 score:",p1score,", Player 2 score:",p2score) 
if p1score > p2score:
    print("Player 1 wins the game!!!")
elif p2score > p1score:
    print("Player 2 wins the game!!!")
else:
    print("The game is a tie :(")
