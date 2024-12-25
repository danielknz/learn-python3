import art
from game_data import data
import random

print(art.logo)
score = 0
gameContinue = True

def formatData(person):
  person_name = person['name']
  person_desc = person['description']
  person_country = person['country']
  return f"{person_name}; {person_desc}; {person_country}"

def checkFollowerCount(guess, aFollowerCcount, bFollowerCount):
  if aFollowerCount > bFollowerCount:
    return guess == "a"
  else:
    return guess == "b"

while gameContinue:
  person_1 = random.choice(data)
  person_2 = random.choice(data)
  if person_1 == person_2:
    person_2 = random.choice(data)
  
  print(f"Compare Person A: {formatData(person_1)}")
  print(art.vs)
  print(f"Against Person B: {formatData(person_2)}")
  
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  aFollowerCount = person_1['follower_count']
  bFollowerCount = person_2['follower_count']
  isCorrect = checkFollowerCount(guess, aFollowerCount, bFollowerCount)
  
  if isCorrect:
    score += 1
    print(art.correct)
    print(f"Score: {score}")
  else:
    print(art.wrong)
    print(f"Final Score: {score}")
    gameContinue = False







