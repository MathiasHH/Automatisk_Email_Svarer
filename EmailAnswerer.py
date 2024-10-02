#Implementer kode som får python scriptet til å svare på ein email

from email_reader import EmailReader
from email_sender import EmailSender

class EmailAnswerer:
    def __init__(self, email_user, email_pass):
        self.reader = EmailReader(email_user, email_pass)
        self.sender = EmailSender(email_user, email_pass)

    def process_emails(self):
        unread_emails = self.reader.fetch_unread_emails()
        for email in unread_emails:
            print(f"Processing email from {email['sender']} with subject {email['subject']}")
            self.sender.send_auto_reply(email["sender"], f"Re: {email['subject']}")

