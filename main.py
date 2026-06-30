from fastapi import FastAPI

app = FastAPI()

# Temporary database
students = []


# CREATE
@app.post("/add")
def add_student(id: int, name: str):

    student = {
        "id": id,
        "name": name
    }

    students.append(student)

    return {
        "message": "Student Added Successfully",
        "students": students
    }


# READ
@app.get("/view")
def view_students():
    return {
        "students": students
    }


# UPDATE
@app.put("/update")
def update_student(id: int, name: str):

    for student in students:
        if student["id"] == id:
            student["name"] = name
            return {
                "message": "Student Updated Successfully",
                "students": students
            }

    return {"message": "Student ID Not Found"}


# DELETE
@app.delete("/delete")
def delete_student(id: int):

    for student in students:
        if student["id"] == id:
            students.remove(student)
            return {
                "message": "Student Deleted Successfully",
                "students": students
            }

    return {"message": "Student ID Not Found"}