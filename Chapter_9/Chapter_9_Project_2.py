testFile = open('test','w')
x=input("Enter:")
testFile.write(x)
testFile.close()
testFile = open('test')
content=testFile.read()
testFile.close()
print(content)
a=b=c=d=' '
for i in (x.split()):
    if(i=='ADJECTIVE'):
        a=input('Enter an adjective:')
    elif(i=='NOUN'):
        b=input("Enter a noun:")
    elif(i=='ADVERB'):
        c=input('Enter an adverb:')
    elif(i=='VERB'):
        d=input("Enter an verb:")

for i in (x.split()):
    if(i=='ADJECTIVE'):
        print(a,end=" ")
    elif(i=='NOUN'):
        print(b,end=" ")
    elif(i=='ADVERB'):
        print(c,end=" ")
    elif(i=='VERB'):
        print(d,end=" ")
    else:
        print(i,end=" ")