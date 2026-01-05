# Tiny Calculator with Loop
while True:
    try:
        a = float(input("Enter first number (or 'q' to quit): "))
        op = input("Operation (+, -, *, /): ")
        b = float(input("Enter second number: "))
        
        if op == '+': result = a + b
        elif op == '-': result = a - b
        elif op == '*': result = a * b
        elif op == '/': result = a / b if b != 0 else "Error!"
        else: result = "Invalid operation!"
        
        print(f"Result: {result}\n")
    except ValueError:
        print("Calculator closed.")
        break
