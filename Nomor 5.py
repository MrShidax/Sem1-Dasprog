VTBI = float(input("Volume to be infused (ml) => "))
Minutes = float(input("Minutes over which to infuse => "))
Rate = VTBI * 60 / Minutes
print("VTBI:",VTBI,"ml")
print("Rate:",Rate,"ml/hr")