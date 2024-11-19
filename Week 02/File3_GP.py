n, AtoBee, BeetoC, CtoD, DtoE = map(int,input("Masukkan n, A to Bee, Bee to C, C to D, D to E : ").split())
if (n > 0 and AtoBee >= 0 and BeetoC >= 0 and CtoD >= 0 and DtoE >= 0):
    if (n >= AtoBee and n >= BeetoC and n >= CtoD and n >= DtoE):
        print("YES HE CAN")
    else:
        print("NO HE CAN'T")
else:
    print("ERROR! DONT USE ZERO FOR THE n AND OR NEGATIVE NUMBER!")