print("pYthon calculator")
print("""
      1.Add
      2.Subract
      3.Divide
      4.Multiply
      """)
options = input("Enter the Options :")
if options == '1' :
    print("Add")
    num1=float(input("Enter :"))
    num2=float(input("Enter :"))
    print(f"Sum : {num1 + num2}")
elif options == '2' :
    print("Subract")
    num1=float(input("Enter :"))
    num2=float(input("Enter :"))
    print(f"Subract :{num1 - num2}")
elif options == '3' :
    print("Divide")
    num1=float(input("Enter :"))
    num2=float(input("Enter :"))
    print(f"Subract :{num1 / num2}")
elif options == '4' :
    print("Multiply")
    num1=float(input("Enter :"))
    num2=float(input("Enter :"))
    print(f"Subract :{num1 * num2}")
else:
    print("invalid choice")

