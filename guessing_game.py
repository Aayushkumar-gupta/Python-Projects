number = 9
i=0
while i<3 :
    guess_one = int(input("Guess : "))
    i+=1
    if guess_one == number :
        print("You Won!")
        break
    elif i>2:
        print("You lost the game!")

# Run this game in your Terminal.
# This is number guessing game. You have three chance to guess the number right. 
# If your able to do so CONGRATULATIONS! you won the game.