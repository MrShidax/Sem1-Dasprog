print('Rule : 1 <= M, N <= 1000\n1 <= T <= 10000')
M, N, T = map(int,input("M Cars Front, N Cars Behind, T Seconds : ").split())
if (1 <= M <= 1000 and 1 <= N <= 1000 and 1 <= T <= 10000):
    Merah = 20
    Kuning = 5
    Hijau = 60
    MobilperCycle = Hijau // 5
    FullCycle = T // (Merah + Kuning + Hijau)
    WaktuSisa = T % (Merah + Kuning + Hijau)
    MobilLewat = 0
    if (WaktuSisa > (Merah + Kuning)):
        HijauSisa = WaktuSisa - (Merah + Kuning)
        MobilLewat = HijauSisa // 5
    
    TotalMobilLewat = FullCycle * MobilperCycle + MobilLewat

    if (M < TotalMobilLewat):
        Hasil = "YES!"
    else:
        Hasil = "No!"

    MobilTotal = M + N + 1
    MobilSisa = max(0, MobilTotal - TotalMobilLewat)
    print(Hasil,MobilSisa)
else:
    print("ERROR! TOLONG IKUTI ATURAN YANG BERLAKU!")