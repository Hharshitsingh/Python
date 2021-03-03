import datetime


class BikeRentalShop:

    def _init_(self, bikes):
        self.bikes = bikes  # no of bikes in stock

    def display(self):  # to check the no of bikes present
        print("We have", self.bikes, "no. of bikes currently available")

    def renthourlybasis(self, n):  # for renting the bike on hourly basis
        if(n > 0):
            if(n > self.bikes):
                print("Sorry, we only have", self.bikes, " bikes available")
            else:
                a = datetime.datetime.now().hour
                print("You have rented", n, "bikes at", a, "hours ")
                print("You'll have to pay $5 per hour")
                self.bikes -= n

        else:
            print("Enter a valid number")

    def rentdailybasis(self, n):  # for renting the bike on daily basis
        if(n > 0):
            if(n > self.bikes):
                print("Sorry, we only have", self.bikes, " bikes available")
            else:
                a = datetime.datetime.now().hour
                print("You have rented", n, "bikes at", a, "hours ")
                print("You'll have to pay $20 per day")
                self.bikes -= n

        else:
            print("Enter a valid number")

    def rentweeklybasis(self, n):  # for renting the bike on weekly basis
        if(n > 0):
            if(n > self.bikes):
                print("Sorry, we only have", self.bikes, " bikes available")
            else:
                a = datetime.datetime.now().hour
                print("You have rented", n, "bikes at", a, "hours ")
                print("You'll have to pay $60 per week")
                self.bikes -= n

        else:
            print("Enter a valid number")

    def bill(self, basis, bik, hour):  # giving the customer the whole bill
        bill = 0
        if(basis != 0 and bik != 0 and hour != 0):

            if(basis == 1):
                bill = 5*hour*bik
            elif(basis == 2):
                bill = 20*((hour/24)+1)*bik
            elif(basis == 3):
                bill = 60*((hour//(24*7))+1)*bik

            if(3 <= bik <= 5):
                bill -= 0.3*bill

            print("your total amount is", bill)

        else:
            print("We are not sure if you rented a bike with us")


class Customer:

    # basis,no of bikes and duration customer is renting a bike for
    def _init_(self, basis, number, rtime):
        self.basis = basis
        self.nobikes = number
        self.rtime = rtime

    def rentsbike(self):  # customer tells how many bikes he want for how many duration
        b = input("How many bikes you want: ")
        r = input("For how many hours: ")
        try:
            b = int(b)
            r = int(r)
        except:
            print("Enter a valid value")
        else:
            if(b > 0 and r > 0):
                self.nobikes = b
                self.rtime = r
            else:
                print("You need to rent at least 1 bike for at least 1 hour")
            return b

    def requestbill(self):
        a = [self.basis, self.nobikes, self.rtime]
        return a


Bi = BikeRentalShop(15)
Bi.display()
p = Customer(1, 3, 6)
Bi.renthourlybasis(p.nobikes)
Bi.display()

# q = Customer(3,0,0)
# x = q.rentsbike()
# Bi.rentweeklybasis(x)
# Bi.display()

l = p.requestbill()
Bi.bill(l[0], l[1], l[2])
