
import random


def play_game():
    secret_number = random.randint(1, 20)
    attempts = 0

    print("Guess the number between 1 and 20.")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 20:
                print("Choose a number between 1 and 20.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low. Try again.")

            elif guess > secret_number:
                print("Too high. Try again.")

            else:
                print("Correct! You guessed the number.")
                print("Attempts:", attempts)
                break

        except ValueError:
            print("Invalid input. Enter an integer.")


def main():
    play_game()


if __name__ == "__main__":
    main()
