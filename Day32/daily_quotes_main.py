import smtplib
import random
import datetime as dt

MY_EMAIL = 'septdac@gmaol.com'
MY_PASSWORD = 'qwertyui'

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
     with open ("quotes.txt") as quote_file:
         all_quotes = quote_file.readlines()
         quote = random.choice(all_quotes)

     print(quote)
     with smtplib.SMTP('smtp.gmail.com') as connection:
         connection.starttls()
         connection.login(MY_EMAIL, MY_PASSWORD)
         connection.sendmail(from_addr=MY_EMAIL, to_addrs="septdac@gmail.com",msg="Subject:Hello\n\nthis is Body of email")
