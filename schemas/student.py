#schemas helps to serialize & also convert mongodb format Json to our UI needed Json

def studentEntity(db_item) -> dict:
    return {
        "Id": str(db_item["_id"]),
        "Name": db_item["student_name"],
        "Email": db_item["student_email"],
        "Phone": db_item["student_phone"]
    }

def listOfStudentEntity(db_item_list) -> list:
    list_student_entity = []
    for item in db_item_list:
        list_student_entity.append(studentEntity(item))

    return list_student_entity