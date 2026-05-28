from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


stu = []

class Students(BaseModel):
    Course: str
    name:str
    Enrollment:int
    is_deleted : bool

@app.post("/PostStudent/")
def create_student(student: Students):
    stu.append(student.dict())
    return{
        "msg":"student added successfully",
        "data": stu
    }
@app.get("/getStudent/")
def get_student():
    return{
        "msg":"student data retrieved successfully",
        "data": stu
    }


@app.get("/getStudentById/{Enrollment}")
def get_student_by_id(Enrollment : int):
    for student in stu:
        if student["Enrollment"]== Enrollment:
            return {
                "msg": "student data by id",
                "data":student
            }
    return {
        "msg": "student not found"
    }

@app.put("/PutStudent/{Enrollment}")
def update(Enrollment : int , updated_student: Students):
    for student in stu:
        if student["Enrollment"]== Enrollment:
            student["name"]= updated_student.name
            student["Course"]= updated_student.Course
            return{
                "msg":"student data update successfully",
                "data": student
            }
    return{
        "msg":"student not found"
    }


@app.delete("/DeleteStudent/{Enrollment}")
def delete_student(Enrollment: int):
    for student in stu:
        if student["Enrollment"]==Enrollment:
            stu.remove(student)
            return{
                "msg":"student data deleted successfully",
                "data":stu
            }
    return{
        "msg":"student not found"
    }

@app.delete("/deleteAllStudents/")
def delete_all_student():
    stu.clear()
    return {
        "msg": "all students deleted successfully"
    }
    
# SOFT DELETE

@app.delete("/SoftDeleteStudent/{Enrollment}")
def soft_delete_student(Enrollment: int):

    for student in stu:

        if student["Enrollment"] == Enrollment:

            student["is_deleted"] = True

            return {
                "msg": "student soft deleted successfully",
                "data": student
            }

    return {
        "msg": "student not found"
    }