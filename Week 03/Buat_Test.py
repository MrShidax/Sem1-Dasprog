UHP = int(input("HP Ucup : "))
BanyakM = int(input("Banyak Minion : "))
BanyakK = int(input("Banyak Knight : "))
M = (M % 2) + M // 2
K = (K % 2) + K // 2
dmgM = M * 2
dmgK = K * 5
if (dmgM >= U):
    print("Yah! Ucup Meninggoy.")
elif (dmgM + dmgK >= U):
    print("Yah! Ucup Meninggoy.")
elif (dmgM + dmgK + 100 >= U):
    print("Yah! Ucup Meninggoy.")
else:
    print(f"Yey! Ucup Menang! HP tersisa: {UHP - dmgM - dmgK - 100}")