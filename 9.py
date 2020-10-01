a = int(input())
b = int(input())
c = int(input())
a1 = int(input())
b1 = int(input())
c1 = int(input())

V1 = a * b * c
V2 = a1 * b1* c1
if(V1>V2):
    print("the first box is larger than the second one")
if(V2>V1):
    print("the first box is smaller than the second one")

if (V1 == V2):
    print("Boxes are equal")
else:
    print("Boxes are  incomparable")
