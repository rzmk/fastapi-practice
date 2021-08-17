from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {}


class Student(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


# # Example of adding a student object locally
# student_1 = Student(name="John", age=17, year="Year 12")
# students[1] = student_1


@app.get("/")
def index():
    return {"message": "Welcome to a classroom example of FastAPI!"}


# Path parameter (decorator parameter + function parameter)
@app.get("/students/{student_id}")
def get_student_by_path_id(
    student_id: int = Path(
        None, description="The ID of the student you want to view.", gt=0
    )
):
    if student_id not in students:
        return {"Error": f"Student ID {student_id} doesn't exist."}
    return students[student_id]


# Query parameters (solely function parameters)
@app.get("/students")
def get_student_by_name(name: str):
    for student_id in students:
        if students[student_id].name == name:
            return students[student_id]
    return {"Error": f"Student name '{name}' not found."}


# Get student by id
@app.get("/students/get/{student_id}")
def get_student_by_id(student_id: int):
    if student_id not in students:
        return {"Error": f"Student ID {student_id} not found."}
    return students[student_id]


# Post student (create new Student object in students list)
@app.post("/students/post/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists."}
    students[student_id] = student
    return students[student_id]


# Update student
@app.put("/students/put/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students:
        return {"Error": f"Student ID {student_id} does not exist."}

    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]


# Delete student
@app.delete("/students/delete/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": f"Student ID {student_id} does not exist."}
    del students[student_id]
    return {"Message": "Student deleted successfully."}
