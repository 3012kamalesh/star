row=int(input('enter the rows'))
for i in range(row):
    for j in range(row-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end=" ")
    print("")
    
