print("(1) First Free Service")
print("(2) Second Free Service")
Nomor = int(input("Enter Free Service Number>> "))
if (Nomor == 1 or Nomor == 2):
    Miles = int(input("Enter number of Miles>> "))

    if (Nomor == 1):
        if (1500 < Miles <= 3000):
            print("Vehicle must be serviced.")
        else:
            print("Service not needed.")

    if (Nomor == 2):
        if (3001 < Miles < 4500):
            print("Vehicle must be serviced.")
        else:
            print("Service not needed.")
else:
    print("ERROR! MASUKKAN ANGKA 1 ATAU 2!")