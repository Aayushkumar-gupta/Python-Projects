import random

x = random.randint(0, 9)
i = 0

while i < 3:
  y = int(input("Guess the number : "))
  i += 1
  if x == y :
    print("You've guessed it right, You Won!")
    break
  elif i > 2:
    print("Oops, wrong guess try again!")

# Guess a number between 0 to 9
# You've three chances to guess
# If you guessed the number in three try. CONGRATULATIONS! you won the game