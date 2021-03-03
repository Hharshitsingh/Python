from replit import clear
logo = """
 _____________________
|  _________________  |
| |0000000000000000 | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(a,b):
    return a+b

def sub(a,b):
    return a-b;

def mult(a,b):
    return a*b

def divide(a,b):
    return a/b


dict = { 
    "+" : add,
    "-" : sub,
    "*" : mult,
    "/" : divide
}

def calculator():
    clear()
    print(logo)
    num1 = float(input("Enter first Number "))
    while True:
        num2 = float(input("Enter Another Number "))
        for symbol in dict:
            print(symbol)
        opt_symbol = input("Choose Symbol for operation: ")
        calc_fun = dict[opt_symbol]
        num1 = calc_fun(num1, num2)
        print(num1)
        bhr =  input("Enter 'q' for quit calculations \nEnter 'n' for new calculations \nEnter for more calculations").lower()
        if bhr == 'q':
            break
        elif bhr == 'n':
            calculator()

calculator()    
