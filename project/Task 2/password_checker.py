import random

def main():
    password = input("Enter your password: ")

    # Check password length
    if len(password) < 9:
        print("Password too short.")
        return

    # Ask for three random character positions
    for _ in range(3):
        position = random.randint(1, len(password))
        guess = input(f"Enter letter at position {position}: ")

        if guess == password[position - 1]:
            print("Correct")
        else:
            print("Security check failed.")
            return

    print("Security check passed.")

if __name__ == "__main__":
    main()
