s1=input().lower()
s2=input().lower()
s1=s1.split()
s2=s2.split()
s=[]
se=[]
for i in s2:
    if(s2.count(i)==1):
        s.append(i)
for i in s1:
    if(s1.count(i)==1):
        se.append(i)
        
c=0
for i in se:
    if( i in s):
        c=c+1
print(c)