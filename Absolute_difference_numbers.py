n,k=map(int,input().split())
n=str(n)
x=int(n[:k])
x1=int(n[-k:])
print(abs(x-x1))