from Student import Student
import json
import os

class StudentManager:
    def __init__(self):
        self.students = []
        self.FILENAME = "students_db.json"

    def add_student(self, name: str, age: int, course: str) -> None:
        """Processes student insertion. Returns True if successful, False if duplicate."""
        
        for student in self.students:
            if student.name.lower() == name.lower():
                return False
            
        new_student = Student(name, age, course)
        self.students.append(new_student)
        return True
    
    def sort_alphabetically(self):
        """Sorts the tracking list in-place by student name property."""
        self.students.sort(key=lambda s: s.name.lower())

    def view_students(self):
        """Sorts and returns the collection of Student objects."""
        return sorted(self.students, key=lambda s:s.name.lower())
    
    def search_student(self, name):
        """Finds a student by name. Returns the Student object or None."""
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def update_student(self, name, new_age=None, new_course=None):
        """Updates properties on a specific Student object."""
        student = self.search_student(name)
        if student:
            if new_age is not None:
                student.age = new_age
            if new_course is not None:
                student.course = new_course
            return True
        return False
    
    def delete_student(self, name):
        """Removes a Student object from the collection list."""
        student = self.search_student(name)
        if student:
            self.students.remove(student)
            return True
        return False
    
    def save_data(self):
        """Saves the current students list to a JSON file"""
        try:
            with open(self.FILENAME, "w") as file:
                json.dump([s.to_dict() for s in self.students], file, indent=4)
            print("\n[System] Data saved successfully to file.")
        except Exception as e:
            print(f"\n[System] Error saving data: {e}")
   
    def load_data(self):
        """Loads students from JSON file into self.students as Student objects"""
        if not os.path.exists(self.FILENAME):
            print("[System] No previous database file found. Starting fresh.")
            return
        try:
            with open(self.FILENAME, "r") as file:
                data = json.load(file)
            for d in data:
                self.students.append(Student.from_dict(d))
            print("[System] Data loaded successfully from disk.")
        except Exception as e:
            print(f"[System] Error loading data: {e}. Starting with an empty list.")
