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


# Asks for a lesson rate and keeps asking until the user types a valid positive number
def get_rate():
    while True:
        text = input("Lesson rate ($): ").strip()
        try:
            rate = float(text)
            if rate > 0:
                return rate
            print("Rate must be greater than 0.")
        except ValueError:
            print("Please enter a number, like 30 or 32.50.")


# Keeps asking until the user types one of the allowed options
def get_option(prompt, options):
    while True:
        answer = input(prompt).strip().lower()
        if answer in options:
            return answer
        print("Please type one of: " + ", ".join(options))


# Adds a new student, or updates the level and rate if the student already exists
def add_student():
    name = input("Student name: ").strip().title()
    if name == "":
        print("Name cannot be blank.")
        return

    level = get_option("Level (beginner/intermediate/advanced): ",
                       ["beginner", "intermediate", "advanced"])
    rate = get_rate()

    if name in students:
        students[name]["level"] = level
        students[name]["rate"] = rate
        print(f"Updated {name}.")
    else:
        instrument = get_option("Instrument (piano/guitar): ", ["piano", "guitar"])
        students[name] = {"instrument": instrument, "level": level, "rate": rate}
        print(f"Added {name}.")


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
        elif choice == "2":
            add_student()
        elif choice in ["3", "4", "5", "6"]:
            print("Coming soon")
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


main()