############### Blackjack Project #####################
import random
import time
from art import logo
import os

def black_jack():
  print(logo)
  game_continue = True
  def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9,10, 10, 10, 10]
    return random.choice(cards)
 
  user_cards = []
  computer_cards = []
  for card in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  def calculate_score(hand_cards):
    hand = sum(hand_cards)
    if hand == 21 and len(hand_cards) == 2:
      return 0
    elif hand > 21 and 11 in hand_cards:
      hand_cards[hand_cards.index(11)] = 1
      hand = sum(hand_cards)
  
    return(hand)
  
  def compare(user_score, computer_score):
    if user_score == computer_score:
      print("It's a draw")
    elif user_score == 0 or user_score == 21:
      print("BlackJack You Win!")
    elif computer_score == 0 or computer_score == 21:
      print("BlackJack Computer Wins")
      print("Sorry that means you lose")
    elif user_score > 21:
      print("BUSTED You Lose")
    elif computer_score > 21:
      print("BUSTED Computer Loses")
    elif user_score > computer_score:
      print("You Win")
    else:
      print("You Lose")

  
  
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
  
  if computer < 17:
    while computer < 17:
      computer_cards.append(deal_card())
      computer = calculate_score(computer_cards)
      print(f"Computer's cards are now: {computer_cards} and their score is {computer}")
  else:
    print(f"Computer's cards are now: {computer_cards} and their score is {computer}")
  
  

  
    
  compare(user,computer)  

black_jack()
while input("Would you like to play again? Type 'y' to play again, type 'n' to quit:") == "y":
  print("Restarting...")
  time.sleep(1)
  os.system('cls')
  black_jack()