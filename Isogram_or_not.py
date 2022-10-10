n=input().lower()
f=0
for i in range(len(n)-1):
    for j in range(i+1,len(n)-1):
        if(n[i]==n[j] and i!=j):
            f=1
            break
if(f==0):
    print(True)
else:
    print(False)
