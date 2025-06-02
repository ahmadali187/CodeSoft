def calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    print("Choose an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    operation = input("Enter the number corresponding to the operation: ")

    if operation == '1':
        result = num1 + num2
        op_symbol = '+'
    elif operation == '2':
        result = num1 - num2
        op_symbol = '-'
    elif operation == '3':
        result = num1 * num2
        op_symbol = '*'
    elif operation == '4':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2
        op_symbol = '/'
    else:
        print("Invalid operation choice.")
        return

    print(f"{num1} {op_symbol} {num2} = {result}")

if __name__ == "__main__":
    calculator()
