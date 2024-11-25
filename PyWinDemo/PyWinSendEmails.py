import win32com.client

def SendOutlookEmail(subject, body, to_email):
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.Subject = subject
    mail.Body = body
    mail.To = to_email
    mail.send

SendOutlookEmail("Automation mail","This is a test mail, generated automatically","sangeethcs2010@gmail.com")