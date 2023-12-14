import random
he = random.randint(1,50)
guess = 0
game = print("\t\t\t Guess The Number")
while True:
    try:    
      start = int(input("Enter your guess: "))
    except ValueError:
      print("Wrong input try again")
      continue
    if start>he:
        print(f"Number is less then {start}")
    elif start<he:
        print(f"Number is greater than {start}")
    elif start==he:
        print(f'Congratulations you guessed the number.The number is {he}')
        break
    guess += 1

print(f"It took you {guess} guesses to guess the number.") 
