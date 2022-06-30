n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s=s+i
c=s/n
print("{:.2f}".format(c))