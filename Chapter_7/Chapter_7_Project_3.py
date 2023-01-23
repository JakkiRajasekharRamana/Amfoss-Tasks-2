import re
A=input("Enter:")
x=re.compile(r'(\s\s)')
X=x.sub('',A)
print(X)
