import smtplib
import random

sender_email = 'mohshinmansuri123@gmail.com'
receiver_email = 'mohshinmansuri370@gmail.com'
password = 'yzax zyxa xyza ayzx'
otp = random.randint(100000,999999)
mail = f"{otp} is Your OTP for login. Thanks from moh technology"

with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, mail)

print("Email Sent!")
