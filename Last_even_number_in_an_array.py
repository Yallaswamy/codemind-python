n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i%2==0:
        b.append(i)
for i in b[::-1]:
    print(i)
    break
