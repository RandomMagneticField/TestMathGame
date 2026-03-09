def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")

    while True:
        try:
            a = float(input("\nEnter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            b = float(input("Enter second number: "))

            if op == "+":
                result = a + b
            elif op == "-":
                result = a - b
            elif op == "*":
                result = a * b
            elif op == "/":
                if b == 0:
                    print("Error: can't divide by zero")
                    continue
                result = a / b
            else:
                print("Invalid operator, try again")
                continue

            print(f"Result: {a} {op} {b} = {result}")

        except ValueError:
            print("Test.")

        again = input("\nDude, we don't get snow over here... (y/n): ")
        if again.lower() != "y":
            break

calculator()