"""Student Grade Management System.

This module provides the Student class to manage student records, validate
grades, calculate statistics, and generate academic performance reports
in compliance with PEP 8 coding standards and clean code practices.
"""

from typing import Union

# Constants for grading thresholds, validation, and report layout
MIN_GRADE = 0.0
MAX_GRADE = 100.0
PASSING_GRADE = 60.0
HONOR_ROLL_GRADE = 90.0

GRADE_A_THRESHOLD = 90.0
GRADE_B_THRESHOLD = 80.0
GRADE_C_THRESHOLD = 70.0
GRADE_D_THRESHOLD = 60.0

DEFAULT_FALLBACK_VALUE = "UNKNOWN"
REPORT_WIDTH = 45


class Student:
    """Represents a student and their academic grade records."""

    def __init__(self, student_id: str, name: str) -> None:
        """Initialize a new Student instance with an ID and name.

        Args:
            student_id: Unique identifier for the student.
            name: Full name of the student.
        """
        self.is_valid = True

        if not isinstance(student_id, str) or not student_id.strip():
            print("Error: Student ID cannot be empty.")
            student_id = DEFAULT_FALLBACK_VALUE
            self.is_valid = False

        if not isinstance(name, str) or not name.strip():
            print("Error: Student name cannot be empty.")
            name = DEFAULT_FALLBACK_VALUE
            self.is_valid = False

        self.student_id = student_id.strip()
        self.name = name.strip()
        self.grades: list[float] = []

    def add_grade(self, grade: Union[int, float]) -> bool:
        """Add a numeric grade within allowed range to student records.

        Args:
            grade: Numeric grade to be added.

        Returns:
            bool: True if grade was valid and added, False otherwise.
        """
        if not isinstance(grade, (int, float)) or isinstance(grade, bool):
            print(f"Error: Grade '{grade}' must be a numeric value.")
            return False

        if not MIN_GRADE <= grade <= MAX_GRADE:
            print(
                f"Error: Grade {grade} is out of valid range "
                f"({MIN_GRADE}-{MAX_GRADE})."
            )
            return False

        self.grades.append(float(grade))
        return True

    def calculate_average(self) -> float:
        """Calculate and return arithmetic average of recorded grades.

        Returns:
            float: The average grade, or 0.0 if no grades exist.
        """
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self) -> str:
        """Determine letter grade based on current average score.

        Returns:
            str: Letter grade (A, B, C, D, or F).
        """
        avg = self.calculate_average()
        if avg >= GRADE_A_THRESHOLD:
            return "A"
        if avg >= GRADE_B_THRESHOLD:
            return "B"
        if avg >= GRADE_C_THRESHOLD:
            return "C"
        if avg >= GRADE_D_THRESHOLD:
            return "D"
        return "F"

    def get_pass_status(self) -> str:
        """Check if student has passed based on passing threshold.

        Returns:
            str: 'Passed' or 'Failed'.
        """
        if self.calculate_average() >= PASSING_GRADE:
            return "Passed"
        return "Failed"

    @property
    def honor_roll(self) -> bool:
        """Return boolean flag indicating if student qualifies for honor roll.

        Returns:
            bool: True if average meets or exceeds honor roll threshold.
        """
        return self.calculate_average() >= HONOR_ROLL_GRADE

    def remove_grade_by_index(self, index: int) -> bool:
        """Remove a grade by its zero-based index.

        Args:
            index: Zero-based position of the grade to remove.

        Returns:
            bool: True if successfully removed, False otherwise.
        """
        if not isinstance(index, int) or isinstance(index, bool):
            print("Error: Index must be an integer.")
            return False

        if 0 <= index < len(self.grades):
            removed = self.grades.pop(index)
            print(f"Removed grade {removed} at index {index}.")
            return True

        print(f"Error: Grade index {index} is out of bounds.")
        return False

    def remove_grade_by_value(self, value: Union[int, float]) -> bool:
        """Remove the first occurrence of a grade by its numeric value.

        Args:
            value: Grade value to remove.

        Returns:
            bool: True if found and removed, False otherwise.
        """
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            print(f"Error: Invalid grade value '{value}'.")
            return False

        float_val = float(value)
        if float_val in self.grades:
            self.grades.remove(float_val)
            print(f"Removed grade with value {float_val}.")
            return True

        print(f"Error: Grade value {float_val} not found in student records.")
        return False

    def report(self) -> None:
        """Print a formatted summary report of the student."""
        avg = self.calculate_average()
        letter = self.get_letter_grade()
        status = self.get_pass_status()
        honor = self.honor_roll

        print("=" * REPORT_WIDTH)
        print("          STUDENT SUMMARY REPORT")
        print("=" * REPORT_WIDTH)
        print(f"Student ID       : {self.student_id}")
        print(f"Student Name     : {self.name}")
        print(f"Number of Grades : {len(self.grades)}")
        print(f"Average Grade    : {avg:.2f}")
        print(f"Letter Grade     : {letter}")
        print(f"Pass/Fail Status : {status}")
        print(f"Honor Roll       : {honor}")
        print("=" * REPORT_WIDTH)


def start_run() -> None:
    """Execute demonstration flow validating core and extended features."""
    print("--- 1. Testing Valid Student Record ---")
    student = Student("STU001", "Xavier Camacho")

    # Adding valid grades
    student.add_grade(100.0)
    student.add_grade(95.0)
    student.add_grade(92.5)

    # Adding invalid grades (Requirement 6 validation)
    student.add_grade("Fifty")
    student.add_grade(-10.0)

    # Removing grades (Requirement 8 validation)
    student.remove_grade_by_index(5)
    student.remove_grade_by_value(95.0)

    # Generating summary report (Requirement 9 validation)
    student.report()

    print("\n--- 2. Testing Invalid Student Inputs (Requirement 6) ---")
    invalid_student = Student("", "   ")
    invalid_student.report()


if __name__ == "__main__":
    start_run()
