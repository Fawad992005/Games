import random

n = random.randint(1, 3)
while True:
   try:
       inp = int(input("Enter your number Gun(1) water(2) snake(3) quit(0): "))
       if inp == 0:
           break
       elif inp > 3:
           print("Enter number within given range!!")
           continue
       else:
           break
   except ValueError:
       print("Enter number within given range: ")
       continue


if inp == n:
    print(f"Computer is {n}.Draw")
elif inp == 3 and n == 1:
    print(f"Computer is {n}.Comp wins")
elif inp == 1 and n == 3:
    print(f"Player is {inp},Computer is {n}.Player wins")
elif inp > n:
    print(f"Player is {inp},Computer is {n}.Player wins")
elif inp == 0:
    print(f"Exiting the game.")
else:
    print(f"Computer is {n},computer wins")

