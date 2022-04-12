#import
from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, listOfStudentEntity
from bson import ObjectId

student_router = APIRouter()

@student_router.get('/hello')
async def hello_world():
    return "Hello World"

#getting all students
@student_router.get('/students')
async def find_all_studs():
    return listOfStudentEntity(connection.local.student.find())

#creating a student
@student_router.post('/students')
async def create_student(Student: Student):
    connection.local.student.insert_one(dict(Student))
    return listOfStudentEntity(connection.local.student.find())

#find one stud with id
@student_router.get('/students/{studentId}')
async def find_student_by_id(studentId):
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))

#update student
@student_router.put('/students/{studentId}')
async def update_student(studentId, student: Student):
    #find stud & update with new data
    connection.local.student.find_one_and_update(
    {"_id": ObjectId(studentId)},
    {"$set": dict(student)}

    )
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))

#delete student
@student_router.delete('/students/{studentId)')
async def delete_student(studentId):
    #finds the student & deletes it and also returns the same stud Object
    return studentEntity(connection.local.student.find_one_and_delete({"_id": ObjectId(studentId)}))
