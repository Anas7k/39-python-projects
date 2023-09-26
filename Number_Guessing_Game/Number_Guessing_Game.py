import random
from art import logo 
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
def numbers():
  random_number = random.randint(1,100)
  #print(f"Pssst, the correct answer is {random_number}")  # this is the answer You can display by removing the "#"
  return random_number

target = numbers()
type = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
if type == "easy":
  attempts = 10
  print(f"You have {attempts} attempts remaining to guess the number.")
else:
  attempts = 5
  print(f"You have {attempts} attempts remaining to guess the number.")

end = True
while end:
  
  guess = int(input("Make a guess:"))
  
  if guess < 1 or guess > 100: # also you can use this for more explanation
      print("Please guess a number between 1 and 100.") 
      continue
  attempts -= 1
  if attempts == 0 and guess > target:
    end = False
    print("Too high!")
    print("You've run out of guesses, you lose.")
  elif attempts == 0 and guess < target:
    end = False
    print("Too low!")
    print("You've run out of guesses, you lose.")
    break
  if guess == target:
    end = False
    print(f"You got it! The answer was {target}.")
  elif guess > target:
    print("Too high!")
    print("Guess again.")
    print(f"You have {attempts} attempts remaining to guess the number.")
  elif guess < target:
    print("Too low!")
    print("Guess again.")
    print(f"You have {attempts} attempts remaining to guess the number.")
