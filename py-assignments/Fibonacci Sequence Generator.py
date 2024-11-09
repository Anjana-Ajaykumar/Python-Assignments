#Generate Fibonacci sequence upto n terms
n=int(input("Enter a number :"))
if(n<1):
    print("Please enter a positive integer")
else: #else block is executed only if n>=1
    fib_seq=[0,1]
    a,b=0,1
    c=0
    while (len(fib_seq)<n):
        c=a+b
        fib_seq.append(c)
        a=b
        b=c
    if(n==1): #fib_seq is set to 0 if n==1
        fib_seq=[0]
    print(",".join(map(str,fib_seq)))
    '''converts the list into string and is printed in a line,seperated by commas'''
