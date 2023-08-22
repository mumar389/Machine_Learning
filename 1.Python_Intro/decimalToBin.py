n=int(input())
ans=0
pv=1
while(n!=0):
    rem=n%2
    ans=ans+int(rem)*pv
    pv*=10
    n=n/2

print(ans)