print('Welcome to My Calculator')
print('Made By Ayoub')

# Get first number
num1 = float(input('Enter First Number: '))

# Get operation
print("\nChoose operation: + - * / % //")
operation = input("Enter operation: ")

# Get second number  
print(f"\n✅ First number: {int(num1) if num1.is_integer() else num1}")
print(f"✅ Operation: {operation}")
print("⏳ Now enter second number:")
num2 = float(input('Enter Second Number: '))

# Calculate
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero!"
elif operation == "%":
    result = num1 % num2
elif operation == "//":
    result = num1 // num2
else:
    result = "Error: Invalid operation!"

# Display result
if isinstance(result, (int, float)):
    display_num1 = int(num1) if num1.is_integer() else num1
    display_num2 = int(num2) if num2.is_integer() else num2
    display_result = int(result) if result.is_integer() else result
    
    print(f"\n🎯 {display_num1} {operation} {display_num2} = {display_result}")
else:
    print(f"\n❌ {result}")