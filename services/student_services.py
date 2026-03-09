from typing import List
from models.student import Student
from mixins.jsonmixin import JSONMixin


class StudentService(JSONMixin):

    @staticmethod
    def load_students(file_name: str) -> List[Student]:

        data = JSONMixin.load_json(file_name)

        students = [
            Student(d["name"], d["roll_number"], d["marks"])
            for d in data
        ]

        return students

    @staticmethod
    def save_students(file_name: str, students: List[Student]) -> None:

        data = [s.to_dict() for s in students]

        JSONMixin.save_json(file_name, data)