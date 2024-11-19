Berat = float(input("Masukkan berat anda dalam Pon : "))
Tinggi = float(input("Masukkan tinggi anda dalam inchi : "))

BMI = round(((703 * Berat) / (Tinggi ** 2)),1)

if (BMI < 18.5):
    Hasil = "Underweight"
elif (18.5 <= BMI <= 24.9):
    Hasil = "Normal"
elif (25 <= BMI <= 29.9):
    Hasil = "Overweight"
elif (BMI > 30):
    Hasil = "Obese"

print(f"BMI anda adalah {BMI}, Sehingga anda termasuk ke dalam kategori {Hasil}")