import random
from playsound import playsound
from replit import clear
from arts import logo,stages
from words import word_list

choosen_word = random.choice(word_list)
lenght_of_word = len(choosen_word)
lives = 6
clear()
print(logo)
cheat_code = input("Press Enter to continue!!!\n")
clear()
if cheat_code == '8dec':
    print(f"the word is {choosen_word}")

display = []
print(stages[lives])
for _ in range(lenght_of_word):
    display += "-"
print(display)

end_of_game = True
while end_of_game:
    guess = input('Guess the letter ').lower()
    clear()

    if guess in display:
      print(f"You've already guessed {guess}")

    for position in range(lenght_of_word):
        letter = choosen_word[position]
        if letter == guess:
            display[position]=letter

    if guess not in choosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives-=1
    print(stages[lives])
    print(display)

    if "-" not in display:
        end_of_game = False
        print('You Win')
    elif lives == 0:
        end_of_game = False
        print('You Loose')
        playsound("sound.mp3")