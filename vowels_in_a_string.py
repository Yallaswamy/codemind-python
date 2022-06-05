n=input()
k=input()
m=0
for i in range(len(n)):
    if(n[i]==k):
        m=1
        break
if(m==1):
    print(True)
    print(i)
else:
     print(False)