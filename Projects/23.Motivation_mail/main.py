import datetime as dt
from os import device_encoding
import smtplib
import random
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open(r"./quotes.txt") as quote_file:
        print(quote_file)
        all_quotes = quote_file.readline()
        quote = random.choice(all_quotes)
    my_email = ""
    paswd  = ""
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=paswd)
        connection.sendmail(from_addr=my_email,
                            to_addrs="",
                            msg=f"Subject:Monday Motivation\n\n {quote} "
                            )
