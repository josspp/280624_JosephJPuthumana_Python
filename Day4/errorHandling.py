try:
    num1=int(input("enter numerator"))
    num2=int(input("enter denomerator"))
    print("Result:"+str(num1/num2))
except ZeroDivisionError as e:
    print("error in input")

print("Completed")