import smtplib

my_email = "vuong.vlq.test@gmail.com"
password = "uphauterpvfeaoiq"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
# Securing our connection to all email server
connection.login(user=my_email, password=password)
# login email
connection.sendmail(from_addr=my_email, to_addrs="vuong.vlq@yahoo.com", msg="Subject:Hello\n\nThis is body of my email")
# Send email
connection.close()

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1998, month=12, day=12, hour=19)
print(date_of_birth)

