n=input().lower()
c=0
co="~`!@#$%^&*()_+-={[}]\|''"":;?/>.<,"
for i in n:
    if(i  in co and i!=" "):
        c=c+1
print(c)