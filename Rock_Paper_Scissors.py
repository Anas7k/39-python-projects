rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
random_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"))
List = [rock, paper, scissors]
my_choose = List[random_choose]

print(my_choose)

computer_choose = random.choice(List)
print("Computer chose: ")
print(computer_choose)
if (my_choose == rock) and (computer_choose == scissors):
    print("You win!")
elif (my_choose == scissors) and (computer_choose == paper):
    print("You win!")
elif (my_choose == paper) and (computer_choose == rock):
    print("You win!")
elif (my_choose == rock) and (computer_choose == paper):
    print("You lose.")
elif (my_choose == scissors) and (computer_choose == rock):
    print("You lose.")
elif (my_choose == paper) and (computer_choose == scissors):
    print("You lose")
else:
    print("It's a draw.")
