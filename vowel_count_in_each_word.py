n=input().lower()
n=n.split()
a="aeiou"
for i in n:
    c=0
    for j in i:
       if(j in a):
           c=c+1
    print(c,end=" ") 
       
       