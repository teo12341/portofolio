import random

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

images = [rock, paper, scissors]

my_choice = int(input(" 0 for Rock, 1 for paper or 2 for scissors?"))

if my_choice >= 0 and my_choice <= 2:
    print(images[my_choice])

computer_choice = random.randint(0, 2)
print("Computer s choice:")
print(images[computer_choice])

if my_choice >= 3 or my_choice == 0:
    print("You typed the wrong number")

elif my_choice == computer_choice:
    print("It s draw")

elif my_choice == 0 and computer_choice == 2:
    print("You won")

elif my_choice == 2 and computer_choice == 0:
    print("You lose")

elif my_choice > computer_choice:
    print("You won")

elif my_choice < computer_choice:
    print("You lose")


