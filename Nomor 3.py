Jam = float(input("Masukkan Jam => "))
Menit = float(input("Masukkan Menit => "))
t = Jam + (Menit / 60)
T = ((4 * t ** 2) / (t + 2)) - 20
print("Suhu di dalam freezer adalah =>",T,"derajat celsius")