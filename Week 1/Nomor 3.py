# Jam = float(input("Masukkan Jam => "))
# Menit = float(input("Masukkan Menit => "))
Jam , Menit , detik = map(float,input("Masukkan Jam dan menit => ").split())
t = Jam + (Menit / 60)
T = round(((4 * t ** 2) / (t + 2)) - 20,3)
print("Suhu di dalam freezer adalah =>",T,"derajat celsius")
print(detik)