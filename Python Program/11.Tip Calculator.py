print("Welcome to Tip Calculator")
bill = float(input("Enter Total Bill? "))
tip_per = float(input("How Percentage you want to give Tip? "))
persons = int(input("How many you are? "))
total_bill = (tip_per/100 * bill)+bill
split_bill = total_bill/persons
print(f"Everyone should pay {split_bill}")