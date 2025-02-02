############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a dealCard() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using dealCard() and append().
#userCards = []
#computerCards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the dealCard() function to add another card to the userCards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import art
import random
from replit import clear


def calculateScore(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def dealCard(userType):
  cards = [
      11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9,
      10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4,
      5, 6, 7, 8, 9, 10, 10, 10, 10
  ]
  card = random.choice(cards)
  #print(userType + "'s card: " + str(card))
  return card


def compareScore(userScore, computerScore):
  if userScore == computerScore:
    return "Push!"
  elif computerScore == 0:
    return "You lose; the opponent has a blackjack!"
  elif userScore == 0:
    return "You win; you have a blackjack!"
  elif userScore > 21:
    return "You busted; you lose!"
  elif computerScore > 21:
    return "Opponent busted; you win!"
  elif computerScore > userScore:
    return "You lose!"
  else:
    return "You win!"


def playGame():
  print(art.logo)
  gameOver = False

  userCards = []
  userCards.append(dealCard('user'))
  userCards.append(dealCard('user'))

  computerCards = []
  computerCards.append(dealCard('computer'))
  computerCards.append(dealCard('computer'))

  computerScore = -1
  userScore = -1

  while not gameOver:
    userScore = calculateScore(userCards)
    computerScore = calculateScore(computerCards)

    print(f"Your cards: {userCards}, total: {userScore}")
    print(f"The computer's first card: {computerCards[0]}")

    if userScore > 21 or userScore == 0 or computerScore == 0:
      gameOver = True
    else:
      dealOrNoDeal = input(
          "To User: Would you like to hit or stand? Type 'H'/'S': ").lower()
      if dealOrNoDeal == "h":
        userCards.append(dealCard('user'))
      else:
        gameOver = True

  while computerScore != 0 and computerScore < 17:
    computerCards.append(dealCard('computer'))
    computerScore = calculateScore(computerCards)

  print(compareScore(userScore, computerScore))
  print(f"The computer's cards: {computerCards},total: {computerScore}")


while input(
    "Would you like to play a game of blackjack? (y/N)").lower() == "y":
  clear()
  playGame()
