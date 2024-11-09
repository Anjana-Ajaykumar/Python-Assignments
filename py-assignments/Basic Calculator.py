#basic calculator to perform operations in 2 operands

n1=float(input("Enter first number:"))
n2=float(input("Enter second number:"))
operation=input("Select an operation [+,-,*,/]:")

if(operation=='+'):
    result=n1+n2
elif(operation=='-'):
    result=n1-n2
elif(operation=='*'):
    result=n1*n2
elif(operation=='/'):
    if(n2==0):
        print("Can't divide by zero")
        result=None #avoids division by zero
    else:
        result=n1/n2
else:
    print("INVALID OPTION")
    result=None #display result only if valid

if (result!=None):
    print(f"{n1} {operation} {n2} = {result}")
