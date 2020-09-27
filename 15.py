x = int(input())

if (x == 0):
    print(0)

else:
    y = 1
    prev = 0
    next = 1
    
    while next <= x:
        if next == x:
            print(y)
            break
        prev, next = next, prev + next
        y += 1
    else:
        print(-1)