import random

game_continue = True

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

user_cards = []
computer_cards = []
for card in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
def calculate_score(hand_cards):
    hand = sum(hand_cards)
    if hand == 21 and len(hand_cards) == 2:
        hand = 0
    elif hand > 21 and 11 in hand_cards:
        hand_cards[hand_cards.index(11)] = 1
        hand = sum(hand_cards)
    return hand 

  
