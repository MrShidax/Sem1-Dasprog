YardLength = float(input("Masukkan panjang halaman (feet) => "))
YardWidth = float(input("Masukkan lebar halaman (feet) => "))
HouseLength = float(input("Masukkan panjang rumah (feet) => "))
HouseWidth = float(input("Masukkan lebar rumah (feet) => "))
LuasYard = (YardLength * YardWidth) - (HouseLength * HouseWidth)
Waktu = LuasYard / 2
print("Waktu yang dibutuhkan untuk memotong rumput halaman adalah",Waktu,"Detik")