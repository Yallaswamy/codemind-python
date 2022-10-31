n,m=map(int,input().split())
a=[]
for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)
sm=su=0
for i in range(0,len(a),2):
    for j in a[i]:
        sm+=j
for i in range(1,len(a),2):
    for j in a[i]:
        su+=j
print(sm,su)

