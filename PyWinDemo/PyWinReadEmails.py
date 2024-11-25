import win32com.client

def ReadOutlookEmail(namespace):
    inbox = namespace.GetDefaultFolder(6)
    messages = inbox.Items
    print(f"Total messages: {len(messages)}")

    for i in range(min(5,len(messages))):
        message = messages[i]
        print(f"Subject: {message.Subject}")
        print(f"Sender: {message.SenderName}")
        print(f"Received Time: {message.ReceivedTime}\n")
        
#Usage
outlook = win32com.client.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")
ReadOutlookEmail(namespace)