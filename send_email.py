import smtplib
import os
from dotenv import load_dotenv

## read the dotenv
load_dotenv(override=True)

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")




with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()


    # log in
    smtp.login(user=email, password=password)

    sender = "testwitholu@gmail.com"
    recepient = "profbatuka@gmail.com"

    subject = "Important Message"
    body = "This is an importan message"

    message = f"Subject: {subject}\n\n{body}"

    print("Attempting to send your email ...")

    try:
        smtp.sendmail(sender, recepient, message)
        print("Email sent successfully")
    except:
        print("We could not send an email at the moment")
    

