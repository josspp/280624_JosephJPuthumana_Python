def ArithOperation(a, b, option):
    if(option=='add'):
        result= a+b
    elif(option=='sub'):
        result= a-b
    elif(option=='mul'):
        result= a*b
    return result

userInput=''    
while(userInput!='4'):
    print("Math operations")
    print("-----------------")
    print("Please choose one of the below options:\n1.Addition\n2.Substraction\n3.Multiplication\n4.Exit App")
    userInput=input()
    if(userInput=="1"):
        print("Enter first number:")
        num1=int(input())
        print("Enter second number:")
        num2=int(input())
        print("Sum is " ,ArithOperation(num1,num2,'add'))
    elif(userInput=="2"):
        print("Enter first number:")
        num1=int(input())
        print("Enter second number:")
        num2=int(input())
        print("Difference is ",ArithOperation(num1,num2,'sub'))
    elif(userInput=="3"):
        print("Enter first number:")
        num1=int(input())
        print("Enter second number:")
        num2=int(input())
        print("Multiplied result is ",ArithOperation(num1,num2,'mul'))