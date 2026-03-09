from typing import Callable
from models.student import Student


def make_grader(min_pass: int) -> Callable[[Student], str]:

    def grader(student: Student) -> str:
        return "Pass" if student.average() >= min_pass else "Fail"

    return grader