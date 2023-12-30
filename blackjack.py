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

  
user = calculate_score(user_cards)
computer = calculate_score(computer_cards)

if user == 0 or computer == 0 or user > 21:
  print("Game Over As Soon As It Started!")
  print(f"Your cards: {user_cards}, Total: {user}")
  print(f"Computer's cards: {computer_cards}, Total: {computer}")
  if user == 0:
    print("You Win")
  elif computer == 0:
    print("You Lose")
  elif user > 21:
    print("You Lose")
  game_continue != True
else:
  print(f"Your cards: {user_cards}, current score: {user}")
  print(f"Computer's first card:{computer_cards[0]}")
  game_continue = True

  while game_continue:
    user_choice = input("Type 'y' to get another card, type 'n' to pass:").lower()
    if user_choice == "y":
      user_cards.append(deal_card())
      user = calculate_score(user_cards)
      print(f"Your cards are now: {user_cards} and your score is {user}")
    else:
      print("You've passed, lets check on the dealer")
      game_continue = False