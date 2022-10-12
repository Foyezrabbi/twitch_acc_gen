from tempmail import TempMail


def mail():
    tm = TempMail()
    email = tm.get_email_address()  # v5gwnrnk7f@gnail.pw
    print(tm.get_mailbox(email))  # list of emails
    print(email)



