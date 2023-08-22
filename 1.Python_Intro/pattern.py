# 1 
# 3 2 
# 4 5 6 
# 10 9 8 7 
# 11 12 13 14 15

n=int(input("Enter the number-:\n"))
c=1
for i in range(1,n+1):
    if(i%2!=0):
        for j in range(1,i+1):
            print(c,end="")
            print("\t",end="")
            c+=1
    else:
        for j in range(i,0,-1):
            # print("j,c-:",j,c)
            print(c+j-1,end="")
            print("\t",end="")
        c=c+i    
    print("\n",end="")

