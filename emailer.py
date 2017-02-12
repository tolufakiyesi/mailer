import smtplib
import getpass

# Import the email modules we'll need
from email.mime.text import MIMEText

class Emailer:

    def __init__(self):
        pass

    def login(self):
        try:
            email_addr = input('Enter your email: ')
            password = getpass.getpass()
            self.s = smtplib.SMTP('smtp.gmail.com', 587)
            self.s.ehlo()
            self.s.starttls()
            self.s.login(email_addr, password)
            print ('Sucessfully logged in')
            password = 'hahahaha'
            return True
        except:
            password = 'hahahaha'
            print ('Login Failed')
            raise
            return False
    

    def write_mail(self):
        recepient = input('Recepient: ')
        message_subject = input('Subject: ')
        message_body = input('Enter your message:\n ')
        
        message = """From: %s\n To: %s\n Subject: %s\n\n %s """ % ('teepfakk@gmail.com', ", ".join(recepient), message_subject, message_body)
        self.send_email(recepient, message_body)
        
    def send_email(self, receiver, msg):
        
        try:

            self.s.send_mail(self.email, receiver, msg)
            self.s.quit()
        except:
            print ('Error')
            
    def main(self):
        
        if self.login() == True:
            self.write_mail()
        else:    
            pass    
        
if __name__ == '__main__':
    test = Emailer()
    test.main()
