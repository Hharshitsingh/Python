from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Name",["Dog", "Cat" ])
table.add_column("Sound",["Bark", "Meow"])


print(table)