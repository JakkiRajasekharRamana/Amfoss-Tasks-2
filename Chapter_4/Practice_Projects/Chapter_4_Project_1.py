n=int(input("Enter Value:"))
L=[]
#X=[]
for i in range(n):
    L.append(input("Enter:"))
    
#for k in range(len(L)):
 #   X.append(int(input(L(k))))
#print(X)
#for x in L:
#    X.append(int(L[x]))
#print(X)
count=0
for k in range(len(L)):
    if(L[k]==''):
        count=count+1
if(count==len(L)):
    print("The given list is  empty,plese enter a valid list!!")
else:
    for j in range(len(L)):
        if(j==len(L)-1):
            print("and",L[j],end=" ")
        else:
           print(L[j],end=" ")

