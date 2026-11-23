
def calculate_sum(number):
    total = 0

    for value in range(1, number + 1):
        total += value

    return total


def main():
    while True:
        try:
            number = int(input("Enter a positive integer: "))

            if number > 0:
                break

            print("Please enter a number greater than zero.")

        except ValueError:
            print("Invalid input. Enter an integer.")

    result = calculate_sum(number)

    print("Sum:", result)


if __name__ == "__main__":
    main()
