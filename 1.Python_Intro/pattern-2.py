n=int(input("Enter the number-:\n"))

space=(2*n)-2
print("Space-:",space)
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
        print("\t",end="")
    for k in range(space):
        print("\t",end="")
    space-=2
    for h in range(i,0,-1):
        print(h,end="")    
        print("\t",end="")
    print("\n",end="")