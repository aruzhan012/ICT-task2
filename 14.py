max = 0
numof_max = 0
x = 1

while (x != 0):
    x = int(input())
    if (x > max):
        max = x
        numof_max = 1
    elif x == max:
        numof_max += 1       
print(numof_max)