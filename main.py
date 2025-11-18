class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = {}  # course_name: grade

    def enroll(self, course_name):
        if course_name not in self.courses:
            self.courses[course_name] = None  # No grade yet
            print(f"{self.name} enrolled in {course_name}.")
        else:
            print(f"{self.name} is already enrolled in {course_name}.")

    def add_grade(self, course_name, grade):
        if course_name in self.courses:
            self.courses[course_name] = grade
            print(f"Grade {grade} added for {self.name} in {course_name}.")
        else:
            print(f"{self.name} is not enrolled in {course_name}.")

    def get_average_grade(self):
        grades = [g for g in self.courses.values() if g is not None]
        return sum(grades) / len(grades) if grades else 0

    def __str__(self):
        return f"Student: {self.name} (ID: {self.student_id})"

class LMS:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, name, student_id):
        if any(s.student_id == student_id for s in self.students):
            print("Student ID already exists.")
            return
        self.students.append(Student(name, student_id))
        print(f"Student {name} added.")

    def add_course(self, course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)
            print(f"Course {course_name} added.")
        else:
            print("Course already exists.")

    def enroll_student(self, student_id, course_name):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student and course_name in self.courses:
            student.enroll(course_name)
        else:
            print("Student or course not found.")

    def add_grade(self, student_id, course_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_grade(course_name, grade)

    def view_student(self, student_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            print(student)
            for course, grade in student.courses.items():
                print(f"  {course}: {grade if grade else 'Not graded'}")
            print(f"  Average Grade: {student.get_average_grade():.2f}")
        else:
            print("Student not found.")

    def generate_report(self):
        print("Student Report:")
        for student in self.students:
            print(f"{student.name} (ID: {student.student_id}) - Average: {student.get_average_grade():.2f}")

# Main menu for interaction
def main():
    lms = LMS()
    while True:
        print("\n1. Add Student\n2. Add Course\n3. Enroll Student\n4. Add Grade\n5. View Student\n6. Generate Report\n7. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Student Name: ")
            sid = input("Student ID: ")
            lms.add_student(name, sid)
        elif choice == '2':
            course = input("Course Name: ")
            lms.add_course(course)
        elif choice == '3':
            sid = input("Student ID: ")
            course = input("Course Name: ")
            lms.enroll_student(sid, course)
        elif choice == '4':
            sid = input("Student ID: ")
            course = input("Course Name: ")
            grade = float(input("Grade: "))
            lms.add_grade(sid, course, grade)
        elif choice == '5':
            sid = input("Student ID: ")
            lms.view_student(sid)
        elif choice == '6':
            lms.generate_report()
        elif choice == '7':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
