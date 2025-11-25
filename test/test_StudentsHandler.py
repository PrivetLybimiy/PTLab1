import pytest
from src.StudentsHandler import StudentsHandler


class TestStudentsHandler:

    @pytest.fixture()
    def students_data(self):
        return {
            "Иванов Иван Иванович": [
                ("математика", 67),
                ("литература", 100),
                ("программирование", 91),
            ],
            "Петров Петр Петрович": [
                ("математика", 90),
                ("химия", 90),
                ("социология", 90),
            ],
            "Сидоров Сидор Сидорович": [
                ("математика", 90),
                ("химия", 89),
                ("русский", 90),
            ],
        }

    def test_find_perfect_student(self, students_data):
        student = StudentsHandler(students_data)
        assert student.find_student(90) == "Петров Петр Петрович"

    def test_no_perfect_student(self):
        data = {
            "Алексей": [("русский", 85)],
            "Борис": [("математика", 70)],
        }

        student = StudentsHandler(data)
        assert student.find_student(90) == 'студенты не найдены'

    def test_multiple_perfect_students(self):
        data = {
            "Константин": [("математика", 90), ("химия", 90)],
            "Сергей": [("математика", 90), ("химия", 90)],
        }

        student = StudentsHandler(data)
        result = student.find_student(90)
        assert result in {"Константин", "Сергей"}

    def test_empty_students(self):
        student = StudentsHandler({})
        assert student.find_student(90) == 'студенты не найдены'

    def test_empty_grades(self):
        data = {
            "Студент": []
        }

        student = StudentsHandler(data)
        assert student.find_student(90) == 'студенты не найдены'

    def test_partial_match(self):
        data = {
            "Семен": [("математика", 90), ("химия", 80)]
        }

        student = StudentsHandler(data)
        assert student.find_student(90) == 'студенты не найдены'
