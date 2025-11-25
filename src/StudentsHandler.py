class StudentsHandler:

    def __init__(self, students):
        self.students = students

    def find_student(self, mark=90):
        for name, grades in self.students.items():
            if grades and all(value == mark for subject, value in grades):
                return name
        return 'студенты не найдены'
