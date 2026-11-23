
def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    if second_number == 0:
        return None

    return first_number / second_number


def main():
    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        operator = input("Enter operator (+, -, *, /): ")

        if operator == "+":
            result = add(first_number, second_number)

        elif operator == "-":
            result = subtract(first_number, second_number)

        elif operator == "*":
            result = multiply(first_number, second_number)

        elif operator == "/":
            result = divide(first_number, second_number)

            if result is None:
                print("Error: Cannot divide by zero.")
                return

        else:
            print("Invalid operator.")
            return

        print("Result:", result)

    except ValueError:
        print("Invalid input. Enter numeric values.")


if __name__ == "__main__":
    main()
