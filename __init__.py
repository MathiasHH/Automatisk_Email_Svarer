#Skal initialisere alle klassene på en gang
from .email_answerer import EmailAnswerer
from .config import EMAIL_USER, EMAIL_PASS

def start_email_bot():
    answerer = EmailAnswerer(EMAIL_USER, EMAIL_PASS)
    answerer.process_emails()

if __name__ == "__main__":
    start_email_bot()
