import random

#Function to create a random number.
def generate_random_number(min_num, max_num):
    return random.randint(min_num, max_num)

#Function to check the user's guess.
def check_guess(random_num, user_guess):
    return random_num == user_guess

#Function for additional hints.
def additional_hint(random_num):
    hints = []
    if random_num % 2 == 0:
        hints.append("Hint: The number is even.")
    else:
        hints.append("Hint: The number is odd.")

    if random_num % 5 == 0:
        hints.append("Hint: The number is a multiple of 5.")

    if random_num ** 2 > 1000:
        hints.append("Hint: The number squared is greater than 1000.")
    else:
        hints.append("Hint: The number squared is less than or equal to 1000.")

    return random.choice(hints)

#Function for main program.
def program():
    print("Welcome to the Guess the Number Game!")
    print("I have selected a random number between 1 and 100. Try to guess it!")

    random_num = generate_random_number(1, 100)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if check_guess(random_num, guess):
                guessed_correctly = True
                print(f"Correct! You guessed the number in {attempts} attempts.")
            else:
                if guess < random_num:
                    print("Incorrect! Try a higher number.")
                else:
                    print("Incorrect! Try a lower number.")

                if attempts == 2:
                    print(additional_hint(random_num))

        except ValueError:
            print("Invalid input. Please enter a whole number.")

#Function for multiple attempts and checking for valid response
def run_again():
    try_again = input("Would you like to try again? Please type Yes or No. ")
    if try_again.lower() == "yes":
        program()
    elif try_again.lower() == "no":
        print("Alright, see you next time!")
    else:
        wrong_response()

#Function for invalid response
def wrong_response():
    print("Invalid Response. Please try again.")
    run_again()

program()
run_again()