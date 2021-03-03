def add(a,b):
    c = a + b
    print(a, " + ", b, " = ", c)
def sub(a,b):
    c = a - b
    print(a, " - ", b, " = ", c)
def mult(a,b):
    c = a * b
    print(a, " * ", b, " = ", c)
def div(a,b):
    c = a / b
    print(a, " / ", b, " = ", c)
while True:
    print("\n1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    c=int(input("Enrter your choice: "))
    if(c<5):
        a=int(input("Enter First Numbers: "))
        b=int(input("Enter Second Numbers: "))
        if (c==1):
            add(a,b)
        elif(c==2):
            sub(a,b)
        elif(c==3):
            mult(a,b)
        else:
            div(a,b)
    else:
        print("\tWrong Input")
    i=input("\nEnter Y for more calculations: ")
    if(i!="y" and i!="Y"):
        break