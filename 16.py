n=1
a=[]
cnt=0
while n!= 0:
    n=int(input(""))
    a.append(n)
    
for i in a:
    if a[i] < a[i+1] and a[i] < a[i-1]:
        cnt+=1    
print(cnt)