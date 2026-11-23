
def print_table(number):
    for multiplier in range(1, 11):
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")


def main():
    while True:
        try:
            number = int(input("Enter a number: "))
            break

        except ValueError:
            print("Invalid input. Enter an integer.")

    print_table(number)


if __name__ == "__main__":
    main()
