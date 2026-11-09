# Grizzly Music Studio - lesson tracker

# Main data: each student's name maps to their instrument, level, and rate
students = {
    "Maya Lopez": {"instrument": "piano", "level": "beginner", "rate": 30.00},
    "Eli Carter": {"instrument": "guitar", "level": "intermediate", "rate": 35.00},
    "Ava Nguyen": {"instrument": "piano", "level": "advanced", "rate": 40.00},
}


# Prints every student with their instrument, level, and lesson rate
def view_students():
    if not students:
        print("No students yet.")
        return
    print("\n--- Students ---")
    for name, info in students.items():
        print(f"{name}: {info['instrument']}, {info['level']}, ${info['rate']:.2f}/lesson")


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
        elif choice == "1":
            view_students()
        elif choice in ["2", "3", "4", "5", "6"]:
            print("Coming soon")
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


main()