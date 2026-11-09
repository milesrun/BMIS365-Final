# Grizzly Music Studio - lesson tracker


# Prints every option in the main menu
def show_menu():
    print("\n=== Grizzly Music Studio ===")
    print("1. View students")
    print("2. Add or update a student")
    print("3. Book a lesson")
    print("4. Record a lesson result")
    print("5. Weekly report with charts")
    print("6. Run 52-week simulation")
    print("7. Save and exit")


# Shows the menu over and over until the user chooses to exit
def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "7":
            print("Goodbye!")
            break
        elif choice in ["1", "2", "3", "4", "5", "6"]:
            print("Coming soon")
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


main()