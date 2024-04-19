class Student:
    def __init__(self, name, major, code_portfolio_score, group_project_score, exam_score):
        self.name = name
        self.major = major
        self.code_portfolio_score = code_portfolio_score
        self.group_project_score = group_project_score
        self.exam_score = exam_score

    def print_details(self):
        print(f"Name: {self.name}, Major: {self.major}, Code Portfolio Score: {self.code_portfolio_score}, Group Project Score: {self.group_project_score}, Exam Score: {self.exam_score}")

# Example of using the Student class
if __name__ == "__main__":
    # Creating an instance of the Student class
    student1 = Student(
        name="jason",
        major="BMI",
        code_portfolio_score=90,
        group_project_score=85,
        exam_score=92
    )
    
    # Printing the details of the student
    student1.print_details()