Gallons = float(input("How many gallons? => "))
BTUperGallons = 5800000 / 42
Eff = float(input("House oil furnace efficiency (percent) => "))
BTUreal = round(Eff / 100 * BTUperGallons * Gallons,3)
print("BTUs of heat delivered to the house =",BTUreal,"BTUs")