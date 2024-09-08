m = float(input("Masukkan angka pertama (m) => "))
n = float(input("Masukkan angka kedua (n) => "))
if (n > m):
    print("ERROR!\nAngka pertama harus lebih besar dari angka kedua!")
else:
    side1 = (m ** 2) - (n ** 2)
    side2 = 2 * m * n
    hypotenuse =   (m ** 2) + (n ** 2)
    print("Triple pythagoras yang terbenntuk adalah:\nsisi pertama :",side1,"\nsisi kedua:",side2,"\nhipotenusa:",hypotenuse)