
def interactive_bmi_calculator():
    """Interactive BMI calculator with user input"""
    print("=== BMI CALCULATOR ===\n")
    
    # Get user input
    try:
        # Choose unit system
        print("Choose unit system:")
        print("1. Metric (kg, meters)")
        print("2. Imperial (pounds, feet/inches)")
        
        choice = input("Enter 1 or 2: ").strip()
        
        if choice == "1":
            # Metric system
            weight = float(input("Enter weight in kilograms: "))
            height = float(input("Enter height in meters: "))
            bmi = weight / (height ** 2)
            
        elif choice == "2":
            # Imperial system
            weight = float(input("Enter weight in pounds: "))
            height_feet = float(input("Enter height in feet: "))
            height_inches = float(input("Enter height in inches: "))
            
            # Convert to metric
            height_total_inches = (height_feet * 12) + height_inches
            height_m = height_total_inches * 0.0254  # inches to meters
            weight_kg = weight * 0.453592  # pounds to kg
            bmi = weight_kg / (height_m ** 2)
            
        else:
            print("Invalid choice!")
            return
        
        # Calculate and display results
        bmi_rounded = round(bmi, 2)
        category = get_bmi_category(bmi_rounded)
        
        print("\n" + "="*30)
        print("BMI CALCULATION RESULTS")
        print("="*30)
        print(f"Your BMI: {bmi_rounded}")
        print(f"Category: {category}")
        print("\n" + "="*30)
        
        # Additional health information
        print("\nBMI Categories (WHO):")
        print("- Underweight: < 18.5")
        print("- Normal weight: 18.5 - 24.9")
        print("- Overweight: 25 - 29.9")
        print("- Obese: ≥ 30")
        
    except ValueError:
        print("Error: Please enter valid numbers!")
    except ZeroDivisionError:
        print("Error: Height cannot be zero!")

def get_bmi_category(bmi):
    """Get detailed BMI category"""
    if bmi < 16:
        return "Severely underweight"
    elif 16 <= bmi < 17:
        return "Moderately underweight"
    elif 17 <= bmi < 18.5:
        return "Mildly underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Obese Class I"
    elif 35 <= bmi < 40:
        return "Obese Class II"
    else:
        return "Obese Class III"

# Run interactive calculator
interactive_bmi_calculator()
