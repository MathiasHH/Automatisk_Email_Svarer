#Implementer kode som kan lese email
import imaplib
import email
from email.header import decode_header

class EmailReader:
    #intialiserer nødvendige variabler
    def __init__(self, email_user, email_pass):
        self.email_user = email_user 
        self.email_pass = email_pass
        self.mail = imaplib.IMAP4_SSL("imap.gmail.com")
        self.mail.login(self.email_user, self.email_pass)

    def fetch_unread_emails(self):
        self.mail.select("inbox")
        status, messages = self.mail.search(None, 'UNSEEN')
        email_ids = messages[0].split()
        unread_emails = []

        for email_id in email_ids:
            status, msg_data = self.mail.fetch(email_id, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else 'utf-8')
                    sender = msg.get("From")
                    body = self.get_email_body(msg)
                    unread_emails.append({"subject": subject, "sender": sender, "body": body})
        return unread_emails

    def get_email_body(self, msg):
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    return part.get_payload(decode=True).decode()
        else:
            return msg.get_payload(decode=True).decode()

