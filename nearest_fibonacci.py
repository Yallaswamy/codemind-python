n=int(input())
a=0
b=1
c=0
d=[]
for i in range(0,n):
    c=a+b
    d.append(c)
    a=b
    b=c
k=s=0
for i in d:
    if(i<n):
        k=i
        #print(i)
    elif(i>n):
        s=i
        #print(i)
        break
if(n-k<s-n):
    print(k)
elif(n-k>s-n):
    print(s)
elif(n-k==s-n):
    print(k,s)