#Implementer kode som kan sende ein email.

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:
    def __init__(self, email_user, email_pass):
        self.email_user = email_user
        self.email_pass = email_pass

    def send_auto_reply(self, to_email, subject):
        smtp_server = "smtp.gmail.com"
        port = 587
        msg = MIMEMultipart()
        msg["From"] = self.email_user
        msg["To"] = to_email
        msg["Subject"] = subject
        body = "Hei, takk for emailen din. Eg vil straks gi deg svar!"
        msg.attach(MIMEText(body, "plain"))

        try:
            server = smtplib.SMTP(smtp_server, port)
            server.starttls()
            server.login(self.email_user, self.email_pass)
            server.sendmail(self.email_user, to_email, msg.as_string())
            print(f"Auto-reply sent to {to_email}")
        except Exception as e:
            print(f"Error sending email: {e}")
        finally:
            server.quit()
