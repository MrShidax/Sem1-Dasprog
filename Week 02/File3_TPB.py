print("Rules : 2 <= n <= 1000")
Angka = int(input("Masukkan Angka : "))
if (2 <= Angka <= 1000):
    if (Angka <= 3):
        print("IT IS A PRIME!")
    elif (Angka % 2 == 0 or Angka % 3 == 0):
        print("IT IS NOT A PRIME!")
    else:
        i = 5
        while (i * i <= Angka):
            if (Angka % i == 0 or Angka % (i+2) == 0):
                print("IT IS NOT A PRIME!")
                break
            i += 6
        print("IT IS A PRIME!")
else:
    print("ERROR! TOLONG IKUTI ATURAN!")