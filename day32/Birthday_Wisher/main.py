import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    print("send an email")
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        print(f'quotes.txt has {len(all_quotes)} lines')
        quote = random.choice(all_quotes)

    print(quote)
else:
    print("don't send email")



# my_email = "robdavis.jr@yahoo.com"
# password = "abcd1234()"
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="rdavis.sauceconcierge@gmail.com",
#         msg="Hello\n\nThis is he body of my email"
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1980, month=6, day=18, hour=9, minute=35)
# print(date_of_birth)

