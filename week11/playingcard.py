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

    def __eq__(self, other):
        return self.__value == other.__value
    
    def suit_match(self, other):
        return self.__suit == other.__suit
        
class Deck:
    
    def __init__(self):
        self.__card_list = []  #the deck will be initially empty

    def __repr__(self):
        return str(self.__card_list)

    def __lt__(self,other):
        return len(self.__card_list) < other

    def __ge__(self,other):
        return len(self.__card_list) >= other
        
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

class Hand:

    def __init__(self):
        self.__card_list = []

    def __repr__(self):
        return str(self.__card_list)

    def size(self):
        return len(self.__card_list)
    
    def put_on_top(self,card):
        self.__card_list.append(card)
    
    def remove_from_top(self):
        if len(self.__card_list) == 0:
            raise Exception("This deck has no cards left.")
        else:
            return self.__card_list.pop()

    
    def top_card(self):
        return self.__card_list[-1]
    def fourth_card(self):
        return self.__card_list[-4]





#Game
stock_deck = Deck()

#create each of the 52 playing cards and put them in the deck
suits = ["♠","♣","♡","♢"]
for s in suits:
    for v in range(2,15):
        curr_card = PlayingCard(v,s)
        stock_deck.put_on_top(curr_card)
        
#look at the deck both before and after shuffling        
print("Here's the pre-shuffled deck:",stock_deck)
stock_deck.shuffle()
print("Here's the deck after the shuffle:",stock_deck)

hand = Hand()
waste_deck = Deck()

#keep going until all cards are dealt out
while not stock_deck.is_empty():
    print("in while stock_deck not empty")
    hand.put_on_top(stock_deck.remove_from_top())
    # print(hand)
    while hand.size() < 4:
        print("hand has at less than 4")
        hand.put_on_top(stock_deck.remove_from_top())
    if hand.top_card() == hand.fourth_card():
        print("value match")
        print(hand)
        for x in range(4):
            waste_deck.put_on_top(hand.remove_from_top())
        print(hand)
    if hand.top_card().suit_match(hand.fourth_card()):
        print("suit match")
        print(hand)
        temp = hand.remove_from_top()
        waste_deck.put_on_top(hand.remove_from_top())
        waste_deck.put_on_top(hand.remove_from_top())
        hand.put_on_top(temp)
        print(hand)
print(stock_deck)
print(hand)
print(waste_deck)
#     #draw a card for each player
#     hand = stock_deck.remove_from_top()
#     p2card = stock_deck.remove_from_top()
    
#     print("Player 1:",p1card,", Player 2:",p2card)
    
#     #check which player wins this hand
#     if p1card < p2card:
#         p1score += 1
#         print("Player 1 wins this hand.")
#     elif p1card > p2card:
#         p2score += 1
#         print("Player 2 wins this hand.")
#     else:
#         print("This hand is a draw.")
        
        
# #Figure out who wins and display the game-end message
# print("Player 1 score:",p1score,", Player 2 score:",p2score) 
# if p1score > p2score:
#     print("Player 1 wins the game!!!")
# elif p2score > p1score:
#     print("Player 2 wins the game!!!")
# else:
#     print("The game is a tie :(")
