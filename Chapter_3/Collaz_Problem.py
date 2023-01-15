def collatz(number):
        if(number%2==0):
            #number=number//2
            print(number//2)
            #a=number//2
            return number//2
        else:
            print(3*number+1)
            #number=number*3+1
            #a=number*3+1
            return 3*number+1
try:
    number=int(input("Enter any Number:"))
    print(number)
    while(number>=1):
        if(number!=1):
            #print(number)
            number=collatz(number)
except ValueError:
    print("Enter A Valid Integer!!")