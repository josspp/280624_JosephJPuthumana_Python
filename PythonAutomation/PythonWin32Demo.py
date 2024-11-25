import win32api
import win32com.client
import win32gui

# print("Windows version:",win32api.GetVersion())
# print("Computer Name:",win32api.GetComputerName())
# print("System Metrics:",win32api.GetSystemMetrics(0))



def custom_messagebox():
    result = win32gui.MessageBox(0,"Hello Sangeeth do you like Python?","Custom Question",1)
    print(result)

    if(result==1):
        win32gui.MessageBox(0,"Thanks!! you love Python?","Info",1)
    elif(result==2):
        win32gui.MessageBox(0,"Oops!! sorry","Info",1)        

custom_messagebox()