import random

current_hand = []
dealer_hand = []
dealer_value = 0
hand_value = 0

class Card:
    values = {'Ace':1,
             '2':2,
             '3':3,
             '4':4,
             '5':5,
             '6':6,
             '7':7,
             '8':8,
             '9':9,
             '10':10,
             'Jack':10,
             'Queen':10,
             'King':10}


    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value

    def get_next_card(self):
        if self.current_position >= len(self.cards):
            return None
        out = self.cards[self.current_position]
        self.current_position += 1
        return out

    def __getitem__(self, index):
        return self.value[index]

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

    def __str__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:
    current_position = 0
    def __init__(self):
        self.cards = []
        for v in Card.values:
            for s in Card.suits:
                c = Card(v, s)
                self.cards.append(c)

    # def __getitem__(self, index):
    #     return self.cards[index]

    def hit(self):
        next_card = self.cards[0]
        self.cards = self.cards[1]
        return next_card

    def get_next_card(self):
        out = self.cards[self.current_position]
        self.current_position += 1
        return out

    def deal_cards(self):
        card1 = self.cards[0]
        card2 = self.cards[2]
        current_hand.append(card1)
        current_hand.append(card2)
        card3 = self.cards[1]
        card4 = self.cards[3]
        dealer_hand.append(card3)
        dealer_hand.append(card4)

    def shuffle(self):
        random.shuffle(self.cards)

    def __repr__(self):
        return "".join(repr(self.cards))


def get_hand_value(current_hand):
    hand_value = 0
    for v in current_hand:
        card_val = int(Card.values[v.value])
        hand_value += card_val
    return hand_value

def get_dealer_value(dealer_hand):
    dealer_value = 0
    for v in dealer_hand:
        card_val = int(Card.values[v.value])
        dealer_value += card_val
    return dealer_value
#
# a = Deck()
# a.shuffle()
#
def main(dealer_value, hand_value, current_hand, dealer_hand):
    a = Deck()
    a.shuffle()
    Deck.deal_cards(a)
    print(current_hand)
    while dealer_value < 22:
        if hand_value < 22:
            print("Your hand's value is: {}".format(get_hand_value(current_hand)))
            action_step = input("Would you like to hit or stand? ")
            if action_step == 'hit':
                current_hand.append(a.get_next_card())
                print(current_hand)
            elif action_step == 'stand':
                if hand_value > dealer_value:
                    win_condition()
                else:
                    loss_condition()

a = Deck()
a.shuffle()
main(dealer_value, hand_value, current_hand, dealer_hand)
