# Grizzly Music Studio - lesson tracker

import csv
from pathlib import Path

# CSV files live in the same folder as this script, no matter where it is run from
FOLDER = Path(__file__).parent
STUDENTS_FILE = FOLDER / "students.csv"


# Reads students.csv into a dictionary; rates are converted from text to numbers
def load_students():
    students = {}
    try:
        with open(STUDENTS_FILE, newline="") as file:
            for row in csv.DictReader(file):
                students[row["name"]] = {
                    "instrument": row["instrument"],
                    "level": row["level"],
                    "rate": float(row["rate"]),
                }
    except FileNotFoundError:
        print("students.csv not found. Starting with no students.")
    return students


# Writes the students dictionary back to students.csv
def save_students(students):
    with open(STUDENTS_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "instrument", "level", "rate"])
        for name, info in students.items():
            writer.writerow([name, info["instrument"], info["level"], f"{info['rate']:.2f}"])


# Prints every student with their instrument, level, and lesson rate
def view_students(students):
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
def add_student(students):
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


# Loads the data, runs the menu until the user exits, then saves
def main():
    students = load_students()

    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "7":
            save_students(students)
            print("Data saved. Goodbye!")
            break
        elif choice == "1":
            view_students(students)
        elif choice == "2":
            add_student(students)
        elif choice in ["3", "4", "5", "6"]:
            print("Coming soon")
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


main()