print("TAXI FARE CALCULATOR")
Awal = float(input("Enter beginning odometer reading=> "))
Akhir = float(input("Enter ending odometer reading=> "))
Jarak = round(Akhir - Awal,3)
Harga = round(Jarak * 1.50,3)
print("You Traveled a distance of",Jarak, "miles. At $1.50 per mile, \nyour fare is $", Harga)