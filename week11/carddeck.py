import random

class PlayingCard:

    def __init__(self, v, s):

        if type(v) != type(1) or v > 14 or v < 2:
            raise Exception(
                "A PlayingCard's value must be an integer in the range 2-14.")
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

    def __lt__(self, other):
        if self.__value < other.__value:
            return True
        else:
            return False

    def __eq__(self, other):
        return self.__value == other.__value

    # added suit match
    def suit_match(self, other):
        return self.__suit == other.__suit


class Deck:

    def __init__(self):
        self.__card_list = []  # the deck will be initially empty

    def __repr__(self):
        return str(self.__card_list)

    def __lt__(self, other):
        return len(self.__card_list) < other

    def __ge__(self, other):
        return len(self.__card_list) >= other

    def put_on_top(self, card):
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
    #duplicated deck class so i could make it specific to the cards in play
    def __init__(self):
        self.__card_list = []

    def __repr__(self):
        return str(self.__card_list)

    def size(self):
        return len(self.__card_list)

    def put_on_top(self, card):
        self.__card_list.append(card)

    def remove_from_top(self):
        if len(self.__card_list) == 0:
            raise Exception("This deck has no cards left.")
        else:
            return self.__card_list.pop()

    # specific "peeks" because the game only needs to check 1st and 4th cards
    def top_card(self):
        return self.__card_list[-1]

    def fourth_card(self):
        return self.__card_list[-4]


# Game
# stock = Deck()
# hand = Hand()
standard_deck = Deck()

# create each of the 52 playing cards and put them in the deck
suits = ["♠", "♣", "♡", "♢"]
for s in suits:
    for v in range(2, 15):
        curr_card = PlayingCard(v, s)
        standard_deck.put_on_top(curr_card)
print(standard_deck)

def one_hand_solitaire(stock):
    # Game
    # shuffle stock
    stock.shuffle()
    hand = Hand()
    waste_deck = Deck()
    print("stock",stock)
    # loop until stock is empty
    loop_count=0
    while not stock.is_empty():
        # loop_count+=1
        # print("#",loop_count)
        # print("  stock",stock)
        # print("  hand",hand)
        # print("  waste",waste_deck)

        # draw cards if hand has less than 4
        if hand.size() < 4:
            hand.put_on_top(stock.remove_from_top())

        # loop until hand has less than 4 cards
        while hand.size() >= 4:
            # check if values match
            if hand.top_card() == hand.fourth_card():
                # removes top 4 cards
                for x in range(4):
                    waste_deck.put_on_top(hand.remove_from_top())
            #check if suits match
            elif hand.top_card().suit_match(hand.fourth_card()):
                # set top card aside
                temp = hand.remove_from_top()
                # pops next two
                waste_deck.put_on_top(hand.remove_from_top())
                waste_deck.put_on_top(hand.remove_from_top())
                # puts temp back on top
                hand.put_on_top(temp)
            # if there is no match draw card from stock to put on hand
            else:
                if not stock.is_empty():
                    hand.put_on_top(stock.remove_from_top())
                # if hand is still less than 4 need to break from this loop to get to the first loop where 
                # it'll accumlate the hand till it has 4 again (this probably confused me the most out of everything)
                break
    # print("stock",stock)
    # print("hand",hand)
    # print("waste",waste_deck)
    print("Score: ",hand.size())


one_hand_solitaire(standard_deck)
"""
OPTION 2: ONE-HANDED SOLITAIRE
the game is simple and predetermined by the shuffle and almost impossible to win (0 cards in hand): 
-draw cards from stock into your hand
-check top and 4th from top for value or suit match
--if value match remove top 4 cards
--if suits match remove the 2 cards between them
- game is over when stock is empty and you have no matches in hand

got a little in the weeds trying to figure out what to print to the terminal to show it working but i do think it works 
landed on showing the shuffled deck and the score
"""