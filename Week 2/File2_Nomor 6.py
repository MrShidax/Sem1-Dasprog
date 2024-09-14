x1, y1 = map(float,input("Masukkan koordinat X dan Y dalam format X(Spasi)Y => ").split())

if (x1 == 0 or y1 == 0):
    if (x1 == 0 and y1 == 0):
        print(f"({x1}, {y1}) is on center")
    elif (x1 == 0 and y1 != 0):
        print(f"({x1}, {y1}) is on the y-axis")
    else:
        print(f"({x1}, {y1}) is on the x-axis")

elif (x1 < 0):
    if (y1 > 0):
        print(f"({x1}, {y1}) is in quadrant II")
    else:
        print(f"({x1}, {y1}) is in quadrant III")

else:
    if (y1 > 0):
        print(f"({x1}, {y1}) is in quadrant I")
    else:
        print(f"({x1}, {y1}) is in quadrant IV")