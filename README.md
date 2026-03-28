# 🧠 Student Analytics System

A Python-based analytics system designed to process, validate, and analyze student academic data. This project leverages **Object-Oriented Programming (OOP)** principles, data validation, and functional programming to generate meaningful insights from structured datasets.

---

## 🚀 Tech Stack

| Layer                | Technology                              |
| -------------------- | --------------------------------------- |
| Language             | Python                                  |
| Programming Paradigm | OOP + Functional Programming            |
| Data Format          | JSON                                    |
| Validation           | Pydantic                                |
| Concepts Used        | Abstract Classes, Mixins, Encapsulation |

---

## 📁 Project Structure

```
Student_Analytics_System/
├── data/
│   └── student_data.json          # Input dataset
├── src/
│   ├── models/
│   │   └── student.py             # Student class & data model
│   ├── validators/
│   │   └── validator.py           # Data validation logic
│   ├── analytics/
│   │   └── analytics_engine.py    # Core analytics logic
│   ├── utils/
│   │   └── helpers.py             # Utility functions
│   └── mixins/
│       └── report_mixin.py        # Reusable reporting features
├── main.py                        # Entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AmoghShukla/Student_Analytics_System.git
cd Student_Analytics_System
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv

# Windows
venv\\Scripts\\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the Application

```bash
python main.py
```

---

## 📊 Features

* Load and parse student data from JSON
* Validate data using Pydantic schemas
* Perform analytics on:

  * Student performance
  * Subject-wise scores
  * Aggregated statistics
* Generate structured reports
* Modular and scalable architecture

---

## 🔍 Example Use Cases

* Analyze academic performance trends
* Identify top-performing students
* Generate reports for institutions
* Practice real-world data handling & validation

---

## 📦 Dependencies

```
pydantic
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m "Add feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the MIT License.
