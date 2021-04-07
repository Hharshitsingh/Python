import sys
import os
os.system('clear')
os.system('setterm -cursor off')
chbt = {"hi": "\nHello👋\n", "who are you": "\nI'm bot🤖\n", "what is your name": "\nArsenal\nMay I know your Name??\n","how are you":"Good😉\nHow are you" ,"what can you do": "\nAnything 😜\n","how old are you": "\n1 Day✨\n", "where do you live": "\nI'm Everywhere🌏\n","harsh":"\nOk\n","good":"Ok","ok":"\nHmm🙂\n"}
print("\t\t\t\tWELCOME\n")
f = open("5.chatbot.txt", 'a')
while True:
    a = input(" \t\t\t\t\t\t\t")
    f.write(a)
    f.write("\n")
    b = a.lower()
    try:
        print(chbt[b])
        f.write(chbt[b])
        f.write("\n")
    except:
        print("Sorry, I can't your answer your Question")
        i = input("If you want to ask more Questions Enter Y: ").lower()
        if(i != 'y'):
             break
print("Thank You!")
f.close()
os.system('setterm -cursor on')