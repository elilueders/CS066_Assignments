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

    def top_card(self):
        return self.__card_list[-1]

    def fourth_card(self):
        return self.__card_list[-4]


# Game
stock = Deck()
hand = Hand()
waste_deck = Deck()

# create each of the 52 playing cards and put them in the deck
suits = ["♠", "♣", "♡", "♢"]
for s in suits:
    for v in range(2, 15):
        curr_card = PlayingCard(v, s)
        stock.put_on_top(curr_card)

# shuffle stock
stock.shuffle()

# loop until stock is empty
loop_count=0
while not stock.is_empty():
    loop_count+=1
    print("#",loop_count)
    print("  stock",stock)
    print("  hand",hand)
    print("  waste",waste_deck)

    # draw cards if hand has less than 4
    if hand.size() < 4:
        hand.put_on_top(stock.remove_from_top())
    # else:
    while hand.size() >= 4:
        if hand.top_card() == hand.fourth_card():
            for x in range(4):
                waste_deck.put_on_top(hand.remove_from_top())
        elif hand.top_card().suit_match(hand.fourth_card()):
            temp = hand.remove_from_top()
            waste_deck.put_on_top(hand.remove_from_top())
            waste_deck.put_on_top(hand.remove_from_top())
            hand.put_on_top(temp)
        else:
            if not stock.is_empty():
                hand.put_on_top(stock.remove_from_top())
            break
print("  stock",stock)
print("  hand",hand)
print("  waste",waste_deck)
