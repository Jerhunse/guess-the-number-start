#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
from art import logo

print(logo)
print("Welcome to the Guessing Game!")

guess = random.randint(1,100)
print(f"FYI the number is {guess}")
# Allow the player to submit a guess for a number between 1 and 100.
difficulty = input("Choose a difficulty 'easy' or 'hard': ")

# If they got the answer correct, show the actual answer to the player.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
if difficulty == "easy":
  guess_left = 10
  print(f"You have {guess_left} attempts left to guess the number")
  while guess_left > 0:
    users_guess = int(input("Make a guess: "))
    if users_guess == guess:
      print(f"You got it!😁 The answer was {guess}")
      break
    elif users_guess < guess:
      print(f"Too low \n you have {guess_left} attempts left")
      guess_left -= 1
    elif users_guess > guess:
      print(f"Too high \n you have {guess_left} attempts left")
      guess_left -= 1
    
    if guess_left == 0:
      print("you ran out of attempts, you lose")
      print(f"The number was {guess}")

# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

#Hard difficulty settings 
if difficulty == "hard":
  guess_left = 5
  print(f"You have {guess_left} attempts left to guess the number")
  while guess_left > 0:
    users_guess = int(input("Make a guess: "))
    if users_guess == guess:
      print(f"You got it! The answer was {guess}")
      break
    elif users_guess < guess:
      print(f"Too low \n you have {guess_left} attempts left")
      guess_left -= 1
    elif users_guess > guess:
      print(f"Too high \n you have {guess_left} attempts left")
      guess_left -= 1
    if guess_left == 0:
      print("you ran out of attempts, you lose")




