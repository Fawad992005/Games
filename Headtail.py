import random as rd
options = ["Heads","Tails"]
while True:
  try:
      choice = input("Choose (Heads or Tails):")
      if choice in options:
          break
      else:
          print("Wrong input!!")
  except ValueError:
      print("Wrong input!1")


while True:
    computer = rd.choice(options)
    if computer == choice:
        print(f"It's {computer}.You win")
        break
    else:
        print(f"It's {computer}.You lose")
        break

