rows=(int(input("Number of rows:")))
columns =(int(input("Number of columns:")))
tableData= [ ]
print("Enter the entries row-wise:")
for i in range(rows):          
    a =[ ]
    for j in range(columns):
         a.append(input())
    tableData.append(a)
for i in range(columns):
    for j in range(rows):
       print(tableData[j][i]," ",end="")
    print("\n",tableData[j][i],"\b\b\b\b",end="")
print("\b\b\b","      ")

