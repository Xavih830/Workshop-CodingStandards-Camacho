"""Student Grade Management System.

This module provides the Student class to manage student records, validate
grades, calculate statistics, and generate academic performance reports
in compliance with PEP 8 coding standards.
"""

from typing import Union


class Student:
    """Represents a student and their academic grade records."""

    def __init__(self, student_id: str, name: str) -> None:
        """Initialize a new Student instance with an ID and name.

        Args:
            student_id: Unique identifier for the student.
            name: Full name of the student.
        """
        if not isinstance(student_id, str) or not student_id.strip():
            print("Error: Student ID cannot be empty.")
            student_id = "UNKNOWN"
        if not isinstance(name, str) or not name.strip():
            print("Error: Student name cannot be empty.")
            name = "UNKNOWN"

        self.student_id = student_id.strip()
        self.name = name.strip()
        self.grades: list[float] = []

    def add_grade(self, grade: Union[int, float]) -> bool:
        """Add a numeric grade between 0 and 100 to the student's records.

        Args:
            grade: Numeric grade to be added.

        Returns:
            bool: True if grade was valid and added, False otherwise.
        """
        if not isinstance(grade, (int, float)) or isinstance(grade, bool):
            print(f"Error: Grade '{grade}' must be a numeric value.")
            return False

        if not 0 <= grade <= 100:
            print(f"Error: Grade {grade} is out of valid range (0-100).")
            return False

        self.grades.append(float(grade))
        return True

    def calculate_average(self) -> float:
        """Calculate and return the average of all recorded grades.

        Returns:
            float: The arithmetic mean of grades, or 0.0 if no grades exist.
        """
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self) -> str:
        """Determine the letter grade based on the current average.

        Returns:
            str: Letter grade (A, B, C, D, or F).
        """
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        if avg >= 80:
            return "B"
        if avg >= 70:
            return "C"
        if avg >= 60:
            return "D"
        return "F"

    def is_passed(self) -> str:
        """Check if the student has passed based on an average of 60 or higher.

        Returns:
            str: 'Passed' or 'Failed'.
        """
        return "Passed" if self.calculate_average() >= 60.0 else "Failed"

    def is_honor_roll(self) -> bool:
        """Determine if student qualifies for Honor Roll (average >= 90).

        Returns:
            bool: True if average is 90 or higher, False otherwise.
        """
        return self.calculate_average() >= 90.0

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
        status = self.is_passed()
        honor = self.is_honor_roll()

        print("=" * 45)
        print("          STUDENT SUMMARY REPORT")
        print("=" * 45)
        print(f"Student ID       : {self.student_id}")
        print(f"Student Name     : {self.name}")
        print(f"Number of Grades : {len(self.grades)}")
        print(f"Average Grade    : {avg:.2f}")
        print(f"Letter Grade     : {letter}")
        print(f"Pass/Fail Status : {status}")
        print(f"Honor Roll       : {honor}")
        print("=" * 45)


def start_run() -> None:
    """Execute the demonstration flow with valid and invalid inputs."""
    student = Student("STU001", "Xavier Camacho")

    student.add_grade(100.0)
    student.add_grade(95.0)
    student.add_grade(92.5)

    student.add_grade("Fifty")  # Non-numeric test
    student.add_grade(-10)      # Out of range test

    student.remove_grade_by_index(5)     # Out of bounds test
    student.remove_grade_by_value(95.0)  # Valid removal

    student.report()


if __name__ == "__main__":
    start_run()
