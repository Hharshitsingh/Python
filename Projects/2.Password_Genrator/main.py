#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '(', ')', '*', '+', '-', '_', '~']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
level = input("Press 'E' for easy and 'H' for hard Password\n")
level = level.lower()
#Eazy Level
password = ""
if level == 'e':
  for char in range(1, nr_letters + 1):
    password += random.choice(letters)

  for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

  for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

#Hard Level
if level == 'h':
  password_list = []
  for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

  for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

  for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

  # print(password_list)
  random.shuffle(password_list)
  # print(password_list)

  for char in password_list:
    password += char

print(f"Your password is: {password}")