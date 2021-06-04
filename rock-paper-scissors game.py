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
human_choice=int(input("Enter 0 for rock, 1 for paper, 2 for scissors "))
list=[rock,paper,scissors]
tmp=list[human_choice]
print(tmp)
computer=random.randint(0,2)
print("Computer choice")
computer_chance=list[computer]
print(computer_chance)

if tmp==computer_chance:
  print("Match Drawn")
elif tmp==rock and computer_chance==scissors:
  print("You won")
elif tmp==scissors and computer_chance==paper:
  print("You won")
elif tmp==paper and computer_chance==rock:
  print("You won") 
else:
  print("You loss")
