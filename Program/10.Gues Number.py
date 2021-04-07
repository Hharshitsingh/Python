import random
n = 5
nog = 0
while True:
    print("Number of Guesses = ",9-nog)
    if nog == 9:
        print("Game  Over")
        break;
    num = int(input("Guess The Number  "))
    if num > n:
        print("You enter Greter number")
    elif num < n:
        print("You enter Lesser number")
    else: 
        print("You win the game")
        break;
    nog = nog + 1
print("No. of Gusses you took ", nog)