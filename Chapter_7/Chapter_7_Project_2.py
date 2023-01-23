import re

X=input("Enter Your New Password:")
count=0
Words=len(X.split())
if(Words>1):
    print('The password must not contain any spaces')
else:
    if(len(X)>=8):
        a=re.compile(r'[a-z]')
        A=a.findall(X)
        b=re.compile(r'[A-Z]')
        B=b.findall(X)
        c=re.compile(r'[0-9]')
        C=c.findall(X)
        if(len(A)>0 and len(B)>0 and len(C)>0):
            count=1
        else:
            print('''
            Please,Try again
            The Password must contain both uppercase and lowercase characters, and has at least one digit ")
            ''')
    else:
        print("The password must contain atleast 8 letters")

if(count==1):
    print("Your New Password is Set :D")