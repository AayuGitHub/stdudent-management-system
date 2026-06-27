import uuid

class Student:
    
    def __init__(self, name: str, age: int, course: str, student_id : str = None):
        self.studentId = student_id if student_id else str(uuid.uuid4())
        self.name = name
        self.age = age
        self.course = course

    def __str__(self):
        """Controls how student looks like when you print it"""
        return f"ID: {self.studentId} | Name: {self.name} | Age: {self.age} | Course: {self.course}"
    
    def to_dict(self):
        """Converts object data back to a dictionary layout for easy JSON saving"""
        return {
            "studentId" : self.studentId,
            "name": self.name,
            "age": self.age,
            "course": self.course
        }
    
    def display_info(self):
        """Method to print this student's details"""
        print(self)
    
    @classmethod
    def from_dict(cls, data):
        return cls( data["name"], data["age"], data["course"], data["studentId"])