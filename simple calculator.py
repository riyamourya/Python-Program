import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero."

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def hcf(a, b):
    return math.gcd(a, b)

# Main program loop
while True:
    print("---- Simple Calculator ----")
    print("Select an operation:")
    print("a. Addition")
    print("b. Subtraction")
    print("c. Multiplication")
    print("d. Division")
    print("e. LCM")
    print("f. HCF")
    print("q. Quit")
    choice = input("Enter your choice: ")

    if choice == 'q':
        break

    if choice in ['a', 'b', 'c', 'd', 'e', 'f']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 'a':
            print("Result:", add(num1, num2))
        elif choice == 'b':
            print("Result:", subtract(num1, num2))
        elif choice == 'c':
            print("Result:", multiply(num1, num2))
        elif choice == 'd':
            print("Result:", divide(num1, num2))
        elif choice == 'e':
            print("Result:", lcm(int(num1), int(num2)))
        elif choice == 'f':
            print("Result:", hcf(int(num1), int(num2)))

        print()
    else:
        print("Invalid choice. Please try again.")
