from typing import Dict
from .person import Person


class Student(Person):

    def __init__(self, name: str, roll_number: int, marks: Dict[str, int]) -> None:
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
        self.__marks: Dict[str, int] = {}

    @property
    def marks(self) -> Dict[str, int]:
        return self.__marks

    @marks.setter
    def marks(self, value: Dict[str, int]) -> None:
        if not all(0 <= score <= 100 for score in value.values()):
            raise ValueError("Marks must be between 0 and 100")
        self.__marks = value

    def average(self) -> float:
        if not self.__marks:
            return 0.0
        return sum(self.__marks.values()) / len(self.__marks)

    def get_details(self) -> str:
        return f"Student: {self.name} (Roll: {self.roll_number})"

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "roll_number": self.roll_number,
            "marks": self.__marks
        }



    def __len__(self) -> int:
        return len(self.__marks)

    def __getitem__(self, subject: str) -> int:
        return self.__marks[subject]

    def __gt__(self, other: "Student") -> bool:
        return self.average() > other.average()

    def __add__(self, other: "Student") -> set:
        return set(self.__marks) | set(other.__marks)

    def __str__(self) -> str:
        return f"{self.name} (Roll: {self.roll_number})"

    def __repr__(self) -> str:
        return f"Student(name={self.name}, roll={self.roll_number}, marks={self.__marks})"