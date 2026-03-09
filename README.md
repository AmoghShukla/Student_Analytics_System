# Student Analytics System

## Overview

The Student Analytics System is a modular Python project designed to load, validate, analyze, and manage academic records stored in JSON datasets. The project demonstrates advanced Python concepts including object‑oriented programming, abstract base classes, mixins, context managers, functional programming techniques, and strong type hinting.

The system provides a clean architecture that separates models, utilities, mixins, and services to make the code maintainable, reusable, and scalable.

## Features

* Object‑oriented design with abstract base classes
* Encapsulation using property getters and setters
* Validation of student marks (0–100)
* Custom dunder methods for enhanced class behavior
* JSON persistence layer for loading and saving datasets
* Context‑managed file operations
* Functional programming concepts using closures and functools.partial
* Modular project structure
* Full type hints for improved readability and maintainability

## Project Structure

```
student_analytics/
│
├── main.py
│
├── models/
│   ├── __init__.py
│   ├── person.py
│   └── student.py
│
├── mixins/
│   ├── __init__.py
│   └── json_mixin.py
│
├── utils/
│   ├── __init__.py
│   └── graders.py
│
├── services/
│   ├── __init__.py
│   └── student_service.py
│
└── data/
    └── students.json
```

## Core Concepts Demonstrated

### Abstract Base Classes

The `Person` class defines a contract that all derived classes must follow by implementing:

* `get_details()`
* `to_dict()`

### Encapsulation and Property Validation

The `Student` class protects internal data using private attributes and property setters that validate marks before assignment.

### Custom Dunder Methods

The `Student` class implements several special methods:

* `__len__` – number of subjects
* `__getitem__` – access marks by subject
* `__gt__` – compare students by average marks
* `__add__` – combine subject sets
* `__str__` and `__repr__` – readable object representations

### Mixins

The `JSONMixin` provides reusable JSON persistence functionality including:

* Safe file handling with context managers
* Loading JSON datasets
* Saving JSON datasets

### Context Managers

File operations are handled using a custom context manager to ensure files are safely opened and closed.

### Functional Programming

The project demonstrates:

* Closures using a dynamic grader generator
* `functools.partial` for function specialization

Example:

```
make_square = partial(power, exponent=2)
```

## Example Usage

```
from models import Student
from utils import make_grader

student = Student("Alice", 1, {"Math": 85, "Physics": 90})

print(student.get_details())
print("Average:", student.average())

grader = make_grader(50)
print("Result:", grader(student))
```

## JSON Data Format

Example dataset:

```
[
  {
    "name": "Alice",
    "roll_number": 1,
    "marks": {
      "Math": 85,
      "Physics": 90
    }
  }
]
```

## Running the Project

1. Clone the repository

```
git clone <repository-url>
```

2. Navigate into the project

```
cd student_analytics
```

3. Run the main script

```
python main.py
```

## Potential Extensions

* Student ranking and leaderboard generation
* Statistical analysis of class performance
* Command line interface for dataset operations
* Integration with a database
* REST API using FastAPI
* Unit testing using pytest

## License

This project is intended for educational and demonstration purposes.
