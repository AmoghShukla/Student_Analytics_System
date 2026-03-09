from functools import partial
from models.student import Student
from utils.graders import make_grader


def power(base: int, exponent: int) -> int:
    return base ** exponent


make_square = partial(power, exponent=2)


def main():

    s1 = Student("Alice", 1, {"Math": 80, "Physics": 90})
    s2 = Student("Bob", 2, {"Math": 70, "Physics": 60})

    print(s1.get_details())
    print("Average:", s1.average())

    print("Subjects:", s1 + s2)

    grader = make_grader(50)
    print("Result:", grader(s1))

    print("Square:", make_square(5))


if __name__ == "__main__":
    main()