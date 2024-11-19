UHP = int(input())
M = int(input())
K = int(input())

M = (M % 2) + M // 2
K = (K % 2) + K // 2

dmgM = M * 2
dmgK = K * 5

if (dmgM >= UHP):
    print("Yah! Ucup Meninggoy.")
elif (dmgM + dmgK >= UHP):
    print("Yah! Ucup Meninggoy.")
elif (dmgM + dmgK + 100 >= UHP):
    print("Yah! Ucup Meninggoy.")
else:
    print(f"Yey! Ucup Menang! HP tersisa: {UHP - dmgM - dmgK - 100}")