#Validating Email Addresses With a Filter

import re

def validation():

    n=int(input("Enter Number of email : "))

    email=[input("Mail : ")  for _ in range(n)]

    valid_mail=[]

    for mail in email:
        pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$'

        if re.match(pattern,mail):
            valid_mail.append(mail)

    return valid_mail



