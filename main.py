# Grizzly Music Studio - lesson tracker

import csv
from datetime import datetime
from pathlib import Path

# CSV files live in the same folder as this script, no matter where it is run from
FOLDER = Path(__file__).parent
STUDENTS_FILE = FOLDER / "students.csv"
LESSONS_FILE = FOLDER / "lessons.csv"


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


# Reads lessons.csv into a list of dictionaries; the amount paid is converted to a number
def load_lessons():
    lessons = []
    try:
        with open(LESSONS_FILE, newline="") as file:
            for row in csv.DictReader(file):
                lessons.append({
                    "date": row["date"],
                    "student": row["student"],
                    "status": row["status"],
                    "paid": float(row["paid"]),
                })
    except FileNotFoundError:
        pass  # no lessons recorded yet; the file is created on first save
    return lessons


# Writes the lessons list back to lessons.csv
def save_lessons(lessons):
    with open(LESSONS_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "student", "status", "paid"])
        for lesson in lessons:
            writer.writerow([lesson["date"], lesson["student"],
                             lesson["status"], f"{lesson['paid']:.2f}"])


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


# Asks for a date and keeps asking until it is a real date in YYYY-MM-DD format
def get_date():
    while True:
        text = input("Lesson date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("Please enter a real date, like 2026-11-15.")


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


# Records a completed or cancelled lesson; completed lessons are paid at the student's rate
def record_lesson(students, lessons):
    name = input("Student name: ").strip().title()
    if name not in students:
        print(f"{name} is not a student. Add them with option 2 first.")
        return

    date = get_date()
    status = get_option("Status (completed/cancelled): ", ["completed", "cancelled"])
    paid = students[name]["rate"] if status == "completed" else 0.00

    lessons.append({"date": date, "student": name, "status": status, "paid": paid})
    print(f"Recorded {status} lesson for {name} on {date} (${paid:.2f}).")


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


# Loads the data, runs the menu until the user exits, then saves both files
def main():
    students = load_students()
    lessons = load_lessons()

    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "7":
            save_students(students)
            save_lessons(lessons)
            print("Data saved. Goodbye!")
            break
        elif choice == "1":
            view_students(students)
        elif choice == "2":
            add_student(students)
        elif choice == "4":
            record_lesson(students, lessons)
        elif choice in ["3", "5", "6"]:
            print("Coming soon")
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


main()