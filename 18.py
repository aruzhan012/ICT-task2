n=int(input())
a=[]
cnt=0
for i in range (0,n):
    k=int(input())
    a.append(k)
x=a[n-1]  
a.insert(0, x)
#a.append(x)
a.pop()
print(a)