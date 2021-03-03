a=input("Enter your E-mail\n: ")
b=a.lower()
if("@gmail.com"==b[-10:] or "@yahoo.com"==b[-10:] or "@redif.com"==b[-10:] or "@hotmail.com"==b[-12:]):
    print(a," is Valid E-mail")
else:
    print(a,"is Invalid E-mail")