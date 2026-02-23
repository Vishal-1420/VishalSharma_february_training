class User:
    def __init__(self, user_id, name, email):
        self.__user_id = user_id
        self.__name = name
        self.__email = email

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def display_details(self):
        print(f"ID: {self.__user_id}")
        print(f"Name: {self.__name}")
        print(f"Email: {self.__email}")


class Student(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.__courses = []

    def enroll_course(self, course_name):
        self.__courses.append(course_name)
        print(f"{self.get_name()} enrolled in {course_name}")

    def get_courses(self):
        return self.__courses

    def display_details(self):
        super().display_details()
        print("Role: Student")
        print("Enrolled Courses:", self.__courses if self.__courses else "None")
        print("-" * 30)


class Mentor(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)
        self.__assigned_students = []

    def assign_student(self, student):
        self.__assigned_students.append(student)

    def view_assigned_students(self):
        if not self.__assigned_students:
            print("No students assigned.")
        else:
            print("Assigned Students:")
            for student in self.__assigned_students:
                print("-", student.get_name())

    def display_details(self):
        super().display_details()
        print("Role: Mentor")
        print("Total Assigned Students:", len(self.__assigned_students))
        print("-" * 30)


class Admin(User):
    def __init__(self, user_id, name, email):
        super().__init__(user_id, name, email)

    def view_all_users(self, students, mentors):
        print("\n---- All Students ----")
        for student in students:
            student.display_details()

        print("\n---- All Mentors ----")
        for mentor in mentors:
            mentor.display_details()

    def display_details(self):
        super().display_details()
        print("Role: Admin")
        print("-" * 30)


students = []
mentors = []
admin = Admin(0, "System Admin", "admin@edtech.com")


def main_menu():
    while True:
        print("\n===== EDTECH MANAGEMENT SYSTEM =====")
        print("1. Create Student")
        print("2. Create Mentor")
        print("3. Enroll Student in Course")
        print("4. Assign Student to Mentor")
        print("5. Mentor View Assigned Students")
        print("6. Admin View All Users")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = int(input("Enter Student ID: "))
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            student = Student(user_id, name, email)
            students.append(student)
            print("Student Created Successfully!")

        elif choice == "2":
            user_id = int(input("Enter Mentor ID: "))
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            mentor = Mentor(user_id, name, email)
            mentors.append(mentor)
            print("Mentor Created Successfully!")

        elif choice == "3":
            if not students:
                print("No students available.")
                continue

            for i, student in enumerate(students):
                print(i, student.get_name())

            index = int(input("Select student index: "))
            course = input("Enter course name: ")
            students[index].enroll_course(course)

        elif choice == "4":
            if not students or not mentors:
                print("Students or Mentors not available.")
                continue

            print("Students:")
            for i, student in enumerate(students):
                print(i, student.get_name())

            s_index = int(input("Select student index: "))

            print("Mentors:")
            for i, mentor in enumerate(mentors):
                print(i, mentor.get_name())

            m_index = int(input("Select mentor index: "))
            mentors[m_index].assign_student(students[s_index])
            print("Student assigned successfully!")

        elif choice == "5":
            if not mentors:
                print("No mentors available.")
                continue

            for i, mentor in enumerate(mentors):
                print(i, mentor.get_name())

            index = int(input("Select mentor index: "))
            mentors[index].view_assigned_students()

        elif choice == "6":
            admin.view_all_users(students, mentors)

        elif choice == "7":
            print("Exiting System...")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main_menu()