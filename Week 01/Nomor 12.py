x1, y1 = map(int,input().split())
x2, y2 = map(int,input().split())
x3, y3 = map(int,input().split())

AkhirkeAwal     = ((((x3 - x2) ** 2) + ((y3 - y2) ** 2)) ** 0.5)
AkhirkeTitik    = ((((x3 - x1) ** 2) + ((y3 - y1) ** 2)) ** 0.5)
AwalkeTitik     = ((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)

if (AkhirkeTitik > AkhirkeAwal):
    print("Yes")
else:
    print("No")