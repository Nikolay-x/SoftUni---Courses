from project.student import Student
import unittest


class StudentTests(unittest.TestCase):
    NAME = "Name"

    def setUp(self) -> None:
        self.student = Student(self.NAME)

    def test_init_without_courses__expect_empty_dictionary(self):
        self.assertEqual(self.NAME, self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_init_witt_courses__expect_dictionary(self):
        courses = {"course1": ["note1.1", "note1.2"], "course2": ["note2.1", "note2.2"]}
        student = Student("name", courses)
        self.assertEqual("name", student.name)
        self.assertEqual(courses, student.courses)

    def test_enroll_course_in_courses__expect_correct_output(self):
        courses = {"course1": [], "course2": []}
        student = Student(self.NAME, courses)
        course_name = "course1"
        notes = ["note1.1", "note1.2"]
        actual_result = student.enroll(course_name, notes)
        expected_result = "Course already added. Notes have been updated."
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(notes, student.courses[course_name])

    def test_enroll_added_notes_Y__expect_correct_output(self):
        courses = {"course1": [], "course2": []}
        student = Student(self.NAME, courses)
        course_name = "course3"
        notes = ["note1.1", "note1.2"]
        expected_result = "Course and course notes have been added."

        added_course_notes = ""
        actual_result = student.enroll(course_name, notes, added_course_notes)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(notes, student.courses[course_name])

    def test_enroll_added_notes_empty_str__expect_correct_output(self):
        courses = {"course1": [], "course2": []}
        student = Student(self.NAME, courses)
        course_name = "course3"
        notes = ["note1.1", "note1.2"]
        expected_result = "Course and course notes have been added."

        added_course_notes = "Y"
        actual_result = student.enroll(course_name, notes, added_course_notes)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(notes, student.courses[course_name])

    def test_enroll_added_notes_other_input__expect_correct_output(self):
        courses = {"course1": [], "course2": []}
        student = Student(self.NAME, courses)
        course_name = "course3"
        notes = ["note1.1", "note1.2"]
        expected_result = "Course has been added."

        added_course_notes = "N"
        actual_result = student.enroll(course_name, notes, added_course_notes)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual([], student.courses[course_name])

    def test_add_notes_course_name_in_courses__expect_correct_output(self):
        courses = {"course1": [], "course2": []}
        student = Student(self.NAME, courses)
        course_name = "course1"
        notes = "note1.1"
        expected_result = "Notes have been updated"

        actual_result = student.add_notes(course_name, notes)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(["note1.1"], student.courses[course_name])

    def test_add_notes_course_name__not_in_courses__expect_correct_output(self):
        courses = {"course1": [], "course2": []}
        student = Student(self.NAME, courses)
        course_name = "course3"
        notes = "note1.1"
        expected_result = "Cannot add notes. Course not found."
        with self.assertRaises(Exception) as error:
            student.add_notes(course_name, notes)
        self.assertEqual(expected_result, str(error.exception))

    def test_leave_course_course_name_in_courses__expect_correct_output(self):
        courses = {"course1": [], "course2": []}
        student = Student(self.NAME, courses)
        course_name = "course1"
        expected_result = "Course has been removed"

        actual_result = student.leave_course(course_name)
        self.assertEqual(expected_result, actual_result)
        self.assertEqual({"course2": []}, student.courses)

    def test_leave_course_course_name__not_in_courses__expect_correct_output(self):
        courses = {"course1": [], "course2": []}
        student = Student(self.NAME, courses)
        course_name = "course3"
        expected_result = "Cannot remove course. Course not found."
        with self.assertRaises(Exception) as error:
            student.leave_course(course_name)
        self.assertEqual(expected_result, str(error.exception))
        self.assertEqual(courses, student.courses)


if __name__ == "__main__":
    unittest.main()
