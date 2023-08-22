def evenSum(n):
    l=[0,1]
   
    even=[]
    c=0
    for i in range(2,n+1):
        res=l[i-1]+l[i-2]
        if(res>n):
            break
        if(res%2==0):
            even.insert(c,res)
            c+=1
        l.insert(i,res)
    sum=0    
    for j in even:
        sum+=j
    return sum    


n=int(input("enter a number-:\n"))
ans=evenSum(n)
print("The answer is-:",ans)