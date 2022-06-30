n=input()
n=n.lower()
c=0
n=n.split()
for i in n:
    m=i
   # print(i)
    j=i[::-1]
    #print(j)
    if(m==j):
        c=c+1
print(c)