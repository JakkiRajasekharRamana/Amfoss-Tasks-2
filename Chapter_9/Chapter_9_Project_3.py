import os,re


path=input("Enter path adress:")
if(os.path.exists(path)==True):
    A=os.listdir(path)
    x=input('What do you want to search?:')
    for i in A:
        if(i.endswith('.txt')):
            file=open(os.path.join(path,i))
            check=file.read()
            if(check ==True):
                print(i)
