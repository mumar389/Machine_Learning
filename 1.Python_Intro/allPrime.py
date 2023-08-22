n=int(input("Enter the number-:\n"))
for i in range(2,n+1):
    count=1
    for j in range(2,i+1):
        if(i==j):
            continue
        elif(i%j==0):
            count+=1
    # print("Count-:",count)        
    if(count>1):
        continue
    else:
        print("Prime",i)          