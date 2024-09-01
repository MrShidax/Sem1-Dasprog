Gallons = float(input("How many gallons? => "))
BTUperGallons = 5800000 / 42
Eff = float(input("House oil furnace efficiency (percent) => "))
BTUreal = Eff / 100 * BTUperGallons * Gallons
print("BTUs of heat delivered to the house =",BTUreal,"BTUs")