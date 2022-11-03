n=int(input())
if(n>2):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end="")
        print()
    for i in range(n-1,0,-1):
        for j in range(i):
            print("*",end="")
        if(i>0):
            print()
else:
    print("The pattern is not possible")