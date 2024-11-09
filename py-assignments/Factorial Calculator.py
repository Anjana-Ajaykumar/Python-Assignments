#factorial calculator using recursion and iteration
num=int(input("Enter a positive number :"))

if(num>=0):

    #factorial using recursion
    def fact(num):
        if (num==1) or (num==0):
            return 1
        else:
            return(num*fact(num-1))

    recursive_factorial=fact(num) #function-call
    print("Factorial using recursion:",recursive_factorial)

    #factorial using iteration
    def fact_iterative(num):
        fact=1
        for i in range(1,num+1):
            fact *= i
        return fact

    iterative_factorial=fact_iterative(num)#function-call
    print("Factorial using iteration:",iterative_factorial)

else:
    print("Cannot find factorial for negative numbers")#when input is negative
