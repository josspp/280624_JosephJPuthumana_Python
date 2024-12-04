import time


def myMenu():
    print("Enter your choice")
    print("1. Enter name")
    print("2. Enter Street")
    print("3. Exit")
    
    while True:
        userinput=input("Enter your choice:")
        if userinput=="1":
            name=input()
            print("The name entered is:",name)
        elif userinput=="2":
            street=input()
            print("The street entered is:",street)
        elif userinput=="3":
            print("Exiting the menu")
            break
        else:
            print("Invalid choice")


    
myMenu()