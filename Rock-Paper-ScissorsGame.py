import random
'''
1 for rock
-1 for paper
0 for scissor
'''
computer=random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youDict = { "rock": 1,"paper": -1,"scissor": 0}
reversedict = {1:"rock",-1:"paper",0:"scissor"}
you=youDict[youstr]
print(f"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")
if(computer == you):
  print("It's a draw")
else:
  if((computer-you)==1 or (computer - you)==2):
    print("You lose")
  else:
    print("You win")
