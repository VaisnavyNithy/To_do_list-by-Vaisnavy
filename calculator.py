# Author- Vaisnavy Nityanantham
#Date-2024.10.10

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("Welcome to the Simple Calculator!")
    
    # Input the first number
    num1 = float(input("Enter the first number: "))
    
    # Input the second number
    num2 = float(input("Enter the second number: "))
    
    # Display operation choices
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    # Input operation choice
    choice = input("Enter choice (1/2/3/4): ")
    
    # Perform calculation based on choice
    if choice == '1':
        result = add(num1, num2)
        operation = "Addition"
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "Subtraction"
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "Multiplication"
    elif choice == '4':
        result = divide(num1, num2)
        operation = "Division"
    else:
        print("Invalid choice! Please select a valid operation.")
        return
    
    # Display the result
    print(f"The result of {operation} is: {result}")

if __name__ == "__main__":
    main()
