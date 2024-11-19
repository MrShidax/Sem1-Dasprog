Data = float(input("Masukkan data yang terpakai dalam GB : "))

if (Data < 0):
    print("Error! Data yang digunakan tidak dapat berupa nilai negatif!")
elif (Data == 0):
    Charge = "0"
elif (0 < Data <= 1):
    Charge = "250"
elif (1 < Data <= 2):
    Charge = "500"
elif (2 < Data <= 5):
    Charge = "1000"
elif (5 < Data <= 10):
    Charge = "1500"
else:
    Charge = "2000"

print(f"Data yang anda gunakan adalah sebanyak {Data} GB,\nSehingga harus membayar sebanyak {Charge}")