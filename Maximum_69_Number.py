n=input()
c=0
for i in str(n):
    if(c==0):
        if(int(i)==6):
            i=9
            c=c+1
    print(i,end="")
    