
def calculate_factorial(number):
    factorial = 1

    for value in range(1, number + 1):
        factorial *= value

    return factorial


def main():
    while True:
        try:
            number = int(input("Enter a non-negative integer: "))

            if number >= 0:
                break

            print("Number cannot be negative.")

        except ValueError:
            print("Invalid input. Enter an integer.")

    result = calculate_factorial(number)

    print(f"Factorial of {number} is {result}")


if __name__ == "__main__":
    main()
