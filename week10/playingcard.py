class PlayingCard:
    
    def __init__(self,v,s):
        self.value = v
        self.suit = s
    def __repr__(self):
        return str(self.value) + " " + str(self.suit)
    def __lt__(self, other):
        return self.value < other.value
    
        
two_of_clubs = PlayingCard(2,"♣")
two_of_hearts = PlayingCard(2,"♡")
ten_of_hearts = PlayingCard(10,"♡")
seven_of_spades = PlayingCard(7,"♠")
four_of_diamonds = PlayingCard(4,"♢")

print("Here's what the card looks like:",ten_of_hearts)

if two_of_clubs < ten_of_hearts:
    print("Player 2 wins the hand")