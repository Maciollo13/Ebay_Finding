import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from config import config


def send_email():
    fromaddr = config.sending_user_email
    toaddr = config.receiving_user_email

    msg = MIMEMultipart()
    msg["From"] = fromaddr
    msg["To"] = toaddr
    msg["Subject"] = "PKM PSA 10"

    body = "TOP 100 searches"
    msg.attach(MIMEText(body, "plain"))


    filename = "result.csv"
    attachment = open("result.csv", "rb")
    p = MIMEBase(_maintype="application", _subtype="csv")
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header(f"Content-Disposition", f"attachment; filename= {filename}")
    msg.attach(p)
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(fromaddr, config.sending_user_app_password)
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()
