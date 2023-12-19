import smtplib

sender = "cismj105@gmail.com"
receiver = "jcanterino0503@gmail.com"
password = input("gimme: ")

message = """
I love ransomware

From Python
"""

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()
s.login(sender, password)


s.sendmail("jcanterino0503@gmail.com", receiver, message)

s.quit