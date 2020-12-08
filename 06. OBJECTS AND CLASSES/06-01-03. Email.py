# 06-01. OBJECTS AND CLASSES [Lab]
# 03. Email

class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


class MailBox:
    def __init__(self):
        self.emails = []

    def add_email(self, email):
        self.emails.append(email)

    def send_email(self, to_send):
        for i in to_send:
            self.emails[i].send()

    def print_mailbox(self):
        for i in self.emails:
            print(i.get_info())


mailbox = MailBox()

while True:
    command = input()
    if command == 'Stop':
        break
    email_sender, email_receiver, email_content = command.split(' ')
    email_current = Email(email_sender, email_receiver, email_content)
    mailbox.add_email(email_current)

mailbox.send_email(list(map(int, input().split(', '))))

mailbox.print_mailbox()
