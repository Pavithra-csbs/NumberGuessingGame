import random
print("Hi guys! Welcome to number guessing game.\n You 10 chances to guess the number.\n LET'S GET STARTED !! ")
low = int(input("Enter the lower number:"))
high = int(input("Enter the high number:"))
num = random.randint(low,high)
chance = 10
guesscount = 0
while (guesscount < chance):
    guesscount +=1
    guess = int(input("Enter the guess number:"))
    if guess == num:
        print(f"Correct! You guessed the number is {num} \n CONGRATS!!")
        break
    elif guesscount >= chance and guess != num:
        print("correct number is ",num,"Try next time")
    elif guess < num:
        print("too low ")
    elif guess > num:
        print("TOO high")





