import unittest
from project.student_report_card import StudentReportCard


class StudentReportCardTests(unittest.TestCase):
    STUDENT_NAME = "SN"
    SCHOOL_YEAR = 6
    GRADES_BY_SUBJECT = {}

    def setUp(self) -> None:
        self.student_report_card = StudentReportCard(self.STUDENT_NAME, self.SCHOOL_YEAR)

    def test_init(self):
        self.assertEqual(self.STUDENT_NAME, self.student_report_card.student_name)
        self.assertEqual(self.SCHOOL_YEAR, self.student_report_card.school_year)
        self.assertEqual({}, self.student_report_card.grades_by_subject)

    def test_student_name_getter_and_setter_valid(self):
        student_name = "new name"
        self.student_report_card.student_name = student_name
        self.assertEqual(student_name, self.student_report_card.student_name)
        self.assertEqual({}, self.student_report_card.grades_by_subject)

    def test_student_name_getter_and_setter_invalid(self):
        student_name = ""
        with self.assertRaises(ValueError) as error:
            self.student_report_card.student_name = student_name
        expected = "Student Name cannot be an empty string!"
        self.assertIsNotNone(error)
        self.assertEqual(expected, str(error.exception))
        self.assertEqual({}, self.student_report_card.grades_by_subject)

        with self.assertRaises(ValueError) as context:
            StudentReportCard(student_name, 12)
        self.assertEqual(expected, str(context.exception))

    def test_school_year_getter_and_setter_valid_1(self):
        school_year = 1
        self.student_report_card.school_year = school_year
        self.assertEqual(school_year, self.student_report_card.school_year)
        self.assertEqual({}, self.student_report_card.grades_by_subject)

    def test_school_year_getter_and_setter_valid_12(self):
        school_year = 12
        self.student_report_card.school_year = school_year
        self.assertEqual(school_year, self.student_report_card.school_year)
        self.assertEqual({}, self.student_report_card.grades_by_subject)

    def test_school_year_getter_and_setter_invalid_gt_12(self):
        school_year = 13
        with self.assertRaises(ValueError) as error:
            self.student_report_card.school_year = school_year
        expected = "School Year must be between 1 and 12!"
        self.assertIsNotNone(error)
        self.assertEqual(expected, str(error.exception))
        self.assertEqual({}, self.student_report_card.grades_by_subject)

    def test_school_year_getter_and_setter_invalid_lt_1(self):
        school_year = 0
        with self.assertRaises(ValueError) as error:
            self.student_report_card.school_year = school_year
        expected = "School Year must be between 1 and 12!"
        self.assertIsNotNone(error)
        self.assertEqual(expected, str(error.exception))
        self.assertEqual({}, self.student_report_card.grades_by_subject)

    def test_add_grade_subject_not_in_grades(self):
        subject = "Subject1"
        grade = 5.5
        self.student_report_card.add_grade(subject, grade)
        actual = self.student_report_card.grades_by_subject
        expected = {'Subject1': [5.5]}
        self.assertEqual(expected, actual)

    def test_add_grade_subject_in_grades(self):
        subject = "Subject1"
        grade = 5.5
        grade1 = 4.5
        self.student_report_card.add_grade(subject, grade)
        self.student_report_card.add_grade(subject, grade1)
        actual = self.student_report_card.grades_by_subject
        expected = {'Subject1': [5.5, 4.5]}
        self.assertEqual(expected, actual)

    def test_average_grade_by_subject(self):
        subject = "Subject1"
        grade = 5.5
        grade1 = 4.5
        self.student_report_card.add_grade(subject, grade)
        self.student_report_card.add_grade(subject, grade1)
        actual = self.student_report_card.average_grade_by_subject()
        expected = "Subject1: 5.00"
        self.assertEqual(expected, actual)
        self.assertEqual({'Subject1': [5.5, 4.5]}, self.student_report_card.grades_by_subject)

    def test_average_grade_by_subject_empty(self):
        actual = self.student_report_card.average_grade_by_subject()
        expected = ""
        self.assertEqual(expected, actual)
        self.assertEqual({}, self.student_report_card.grades_by_subject)

    def test_average_grade_for_all_subjects(self):
        subject1 = "Subject1"
        subject2 = "Subject2"
        grade = 5.5
        grade1 = 4.5
        self.student_report_card.add_grade(subject1, grade)
        self.student_report_card.add_grade(subject1, grade1)
        self.student_report_card.add_grade(subject2, grade1)
        actual = self.student_report_card.average_grade_for_all_subjects()
        expected = "Average Grade: 4.83"
        self.assertEqual(expected, actual)
        self.assertEqual({'Subject1': [5.5, 4.5], 'Subject2': [4.5]}, self.student_report_card.grades_by_subject)

    def test_average_grade_for_all_subjects_empty(self):
        with self.assertRaises(ZeroDivisionError) as error:
            self.student_report_card.average_grade_for_all_subjects()
        self.assertIsNotNone(error)
        self.assertEqual({}, self.student_report_card.grades_by_subject)

    def test_repr(self):
        subject1 = "Subject1"
        subject2 = "Subject2"
        grade = 5.5
        grade1 = 4.5
        self.student_report_card.add_grade(subject1, grade)
        self.student_report_card.add_grade(subject1, grade1)
        self.student_report_card.add_grade(subject2, grade1)
        actual = repr(self.student_report_card)
        expected = f"Name: {self.STUDENT_NAME}\n" \
                 f"Year: {self.SCHOOL_YEAR}\n" \
                 f"----------\n" \
                 f"{self.student_report_card.average_grade_by_subject()}\n" \
                 f"----------\n" \
                 f"{self.student_report_card.average_grade_for_all_subjects()}"
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
