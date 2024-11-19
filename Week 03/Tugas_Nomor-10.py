import string
listhuruf = string.ascii_lowercase
print("Aturan! : \n 0 <= Panjang teks <= 100 \n 0 <= Kode Ajaib <= 26")
kode = input("Masukkan kode dari Miko : ").lower()
geser = int(input("Masukkan angka ajaib : "))
if ((0 <= len(kode) <= 100) and (0 <= geser <= 26)):
    hasil = ""
    for i in kode:
        if i in listhuruf:
            pos = listhuruf.find(i)
            newpos = (pos - geser) % 26
            newchar = listhuruf[newpos]
            hasil += newchar
        else:
            hasil += i
    print(hasil)
else:
    print("IKUTI ATURAN YANG BERLAKU!") 