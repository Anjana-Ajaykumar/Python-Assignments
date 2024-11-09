import math
start=int(input("Enter starting range :"))
end=int(input("Enter ending range :"))
if (end<2):
    print("There are no prime numbers in this range")
else:
    if (start<2):
        start=2
    if(start<=end):
        for num in range(start,end+1):
            flag=0
            for i in range(2,int(math.sqrt(num))+1):
                if(num%i==0):
                    flag=1
                    break
            if(flag==0):
                print(num)
    else:
        print("Invalid Range:Ending range is lesser than Starting range")
