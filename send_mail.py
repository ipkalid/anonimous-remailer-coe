import yagmail

port = 465  # For SSL
my_mail = "testanonymousics440@gmail.com"
smtp_server = "smtp.gmail.com"
password = "ics440123"


yag = yagmail.SMTP(my_mail)


def send_mail(receiver_mail, subject, message):
    yag.send(
    to = receiver_mail,
    subject = subject,
    contents = message
)

yag.send(
    to = "ss@dd.com",
    subject = " djjdjd",
    contents = " sdkhfgsdkgfs"
)