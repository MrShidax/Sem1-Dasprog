warna = str(input("Masukkan huruf pertama dari warna silinder : ")).lower()
List_gas = {
    "o" : "ammonia",
    "b" : "carbon monoxide",
    "y" : "hydrogen",
    "g" : "oxygen"
}

if warna in List_gas:
    print(f"Isi dari silinder adalah gas {List_gas[warna]}")

else:
    print("Contents unknown")