num = int(input())
a=[]
for i in range(2,num):
    if(num%i == 0):
        a.append(i)
a.sort()
print("The smallest divisor is:",a[0])