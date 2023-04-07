logo = '''
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
'''
from random import randint
EASY_TURN = 10
HARD_TURN = 5

def set_difficulty():
    level = input('''In easy you have 10 attempts \nIn hard you have 5 attempts \nSelect your difficulty level 'Easy' or 'Hard' \n''')
    if level == 'easy':
        return EASY_TURN
    else:
        return HARD_TURN

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high\n")
        return turns-1
    elif guess < answer:
        print("Too low\n")
        return turns-1
    else:
        print(f"You got it! right answer was {guess}")


def game():
    print(logo)
    answer = randint(1,100)
    answer = 88
    print('''I select the number between 1 to 100! \n Now, It's your turn guess the number ''')
    # print(f"The correct answer is {answer}")
    turns = set_difficulty()
    guess = 0
    while guess!= answer:
        print(f"You have {turns} remmaing to guess the number")
        guess = int(input("Guess the Number: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print('You ran out of turns you loose')
            return
        elif guess != answer:
            print("Guess again.")
        
game()
