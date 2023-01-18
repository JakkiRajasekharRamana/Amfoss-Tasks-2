import random 
numberOfStreaks=0
L=[]
for i in range(10000):
    L.append(random.randint(0,1))
    
for j in range(9994):
    if(L[j]==L[j+1]==L[j+2]==L[j+3]==L[j+4]==L[j+5]==L[j+6]):
        numberOfStreaks=numberOfStreaks+1
#print(numberOfStreaks)
#print(L)
s=numberOfStreaks/100
print('Chance of streak=',s)
