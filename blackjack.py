from blackjack_setup import *

a = Deck()
a.shuffle()

current_hand = []
dealer_hand = []
def deal_cards():
    card1 = Deck(a[0])
    card2 = Deck(a[2])
    current_hand.append(card1)
    current_hand.append(card2)
    card3 = Deck(a[1])
    card4 = Deck(a[3])
    dealer_hand.append(card3)
    dealer_hand.append(card4)


i = 0
while i<10:
    deal_cards()
    print(current_hand)
    print(dealer_hand)
    i +=1
# b = Card(5, 'Spades')
# print(b)
# #
# class Blackjack:
#     current_hand = []
#     def __init__(self, hand_value):
#         self.hand_value = hand_value
#
#     def deal_hands(self):



# a = Card('Hearts', '5')
# b = Card('Hearts', '6')
# print(a == b)
# d = Deck()
# d.shuffle
# print(d)
