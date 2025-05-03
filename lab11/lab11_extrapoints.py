"""
Paula Rice
Lab 11, classes Python (extra points)
"""

class Student:
    def __init__(self, name, age):
        
        # Initialize the Student class with name, age, dictionary
    
        self.name = name
        self.age = age
        self.grade = {}
    
    def add_grade(self, subject, grade):
        # add a grade for a subject
        self.grade[subject] = float(grade)
    
    def get_average_grade(self):
        # Calculate and return the average grade of the student using float
        
        if not self.grade:
            return 0.0
        
        total = sum(self.grade.values())
        count = len(self.grade)
        return total / count


# CALLING THE CLASS

if __name__ == "__main__":
    # Create first student
    student1 = Student("Mary", 18)
    
    # Add grades for class subjects
    student1.add_grade("Math", 85.5)
    student1.add_grade("Science", 92.0)
    student1.add_grade("French", 78.5)
    student1.add_grade("Spanish", 88.0)
    student1.add_grade("Intro to Business", 95.5)
    
    # Print student information
    print(f"Student: {student1.name}, Age: {student1.age}")
    print(f"Grades: {student1.grade}")
    print("Average Grade:", round(student1.get_average_grade(), 2))
    
    # Create second student
    student2 = Student("John", 19)
    
    # Add grades for class subjects
    student2.add_grade("Math", 90.0)
    student2.add_grade("Science", 88.5)
    student2.add_grade("French", 95.0)
    
    # Print student information
    print(f"\nStudent: {student2.name}, Age: {student2.age}")
    print(f"Grades: {student2.grade}")
    print("Average Grade:", round(student2.get_average_grade(), 2))