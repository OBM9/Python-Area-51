unit = input("Is this temperature in Celsius or Fahrenheit (C/F)? ")
temp = float(input("Enter the temperature: "))

if unit == "C":
        temp = round((9 * temp) / 5 + 32, 2)
elif unit == "F":
    pass
else:
    print(f"{unit} is an invalid unit of measurement")











        


