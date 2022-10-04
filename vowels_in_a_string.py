n=input()
s=input()
c=0
for i in range(len(n)):
    if n[i]==s:
        print(True)
        print(i)
        break
else:
    print(False)