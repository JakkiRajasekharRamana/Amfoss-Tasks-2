import re

X=input("Enter any date in the form of DD/MM/YYYY:")
dateRegex= re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
mo=dateRegex.search(X)
#print(mo.group(1))
#print(mo.group(2))
#print(mo.group(3))
count=0
if((int(mo.group(2))==(2) or (4) or (6) or (8) or (9) or (11) ) and int(mo.group(1))>=31):
    print("Please enter a valid date !!")
    count=1
if(int(mo.group(1))>31 or int(mo.group(2))>12 or 1000<int(mo.group(3))<2999):
    print("Enter a valid date!!")
    count=1
x=False
if(int(mo.group(3))%4==0):
        x=True
        if(int(mo.group(3))%100==0):
            x=False
            if(int(mo.group(3))%400==0):
                x=True
                count=1
if(x==False):
    if(int(mo.group(2))==2 and int(mo.group(1))>=29):
        print("Please enter a valid date!")
        count=1
if(count==0):
    print("Thanks for entering a valid date :D")


