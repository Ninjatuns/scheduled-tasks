import os
import pandas
import datetime as dt
import random
import smtplib
my_email="hanbetemail@gmail.com"
password="mcsixnjpelovzljy"
connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)


now=dt.datetime.now()
month=now.month
day=now.day
data=pandas.read_csv("birthdays.csv")




for index, row in data.iterrows():
    if month ==row['month']:
        if day == row['day']:
            with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
                letter_choice=file.read()
                new_letter=letter_choice.replace("[NAME]",row["name"])
                connection.sendmail(from_addr=my_email,
                                    to_addrs="stupostuko@yahoo.com",
                                    msg=f"Subject:Happy Birthday!\n\n{new_letter}")
                connection.close()
