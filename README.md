# Student Management System

A command-line application to manage student records — add, view, search, update, and delete students, with data that persists across sessions using a local JSON file.

Built with Python as a learning project to practice OOP concepts like classes, encapsulation, and separation of concerns.

---

## What it does

You get a simple text menu when you run the app:

```
=========================
Student Management
=========================
1. Add student
2. View student
3. Search student
4. Update student
5. Delete student
6. Exit
```

Each student has three pieces of information: their name, age, and the course they're enrolled in. Every student also gets a unique ID (UUID) automatically assigned when they're added, so records stay distinguishable even if two students share the same name.

When you exit using option 6, everything is saved to a `students_db.json` file. The next time you run the app, it picks right up where you left off.

---

## How to run it

You just need Python 3 — no external libraries required.

```bash
python3 main.py
```

---

## Project structure

```
Student_Management_System/
├── main.py             # Entry point — runs the menu loop
├── StudentManager.py   # Business logic — handles all student operations
├── Student.py          # The Student class — defines what a student looks like
└── students_db.json    # Auto-created on first save — stores your data
```

### How the files relate to each other

- **`Student.py`** is the blueprint for a single student. It knows how to display itself and how to convert itself to/from a dictionary for JSON storage.
- **`StudentManager.py`** holds the list of all students and handles every operation on that list — adding, searching, updating, deleting, saving to disk, loading from disk.
- **`main.py`** is just the interface. It shows the menu, collects input from the user, calls the right method on `StudentManager`, and prints the result.

---

## Features

- **Add a student** — Validates that name and course aren't blank, and that age is a whole number. Won't let you add the same name twice.
- **View all students** — Lists every student alphabetically by name, with their ID, age, and course.
- **Search by name** — Case-insensitive lookup. Finds "aayush" even if stored as "Aayush".
- **Update a student** — Change age, course, or both. Leave a field blank to skip it.
- **Delete a student** — Removes them permanently from the list.
- **Persistent storage** — Data is saved as JSON on exit and loaded back automatically on the next run. Each student's UUID is preserved across saves so IDs never change.

---

## What I learned building this

- How to split a program into focused classes (`Student` vs `StudentManager`) instead of putting everything in one file
- Why `save` and `load` belong on the manager class — it owns the data, so it should own the persistence
- The JSON round-trip: objects → `to_dict()` → JSON on disk → `from_dict()` → objects again
- How `uuid4()` generates a unique ID, and why you need an optional `student_id` parameter to restore existing IDs instead of generating new ones on every load
- The difference between `import Module` and `from Module import Class`, and why calling `Module()` fails
