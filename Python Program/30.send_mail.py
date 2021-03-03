import smtplib
# turn on less secure app access
myemail = "" #enter email   
pasword = "" #enter password
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=myemail, password=pasword)
    connection.sendmail(from_addr=myemail, 
                        to_addrs="", #recipient email
                        msg="Subject:hello\n\nThis is mail"
                        )
