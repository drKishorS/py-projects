print("_____Temperature Convertor_____")
# 🎯 Core Conversion Formulas
#Celsius to Fahrenheit: F = (C × 9/5) + 32
#Fahrenheit to Celsius: C = (F - 32) × 5/9
print("""
      1. C° to F 
      2. F to C° 
      """)
option=int(input("Enter the option from the menu :"))
covert=int(input("Enter the Value Need to convert :"))
print(".....................")
if option == 2:
    far = (covert - 32) * 5/9
    print(f"(ツ) {covert}°F to {far:.1f}°C ")
elif option == 1:
    cel = (covert * 9/5 ) + 32
    print(f"(ツ) {covert}°C to {cel:.1f}°F") 
else:
    print("Wrong Options")
print("...Have a nice day...")
