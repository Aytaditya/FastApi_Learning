from fastapi import FastAPI # type: ignore
# from fastapi import Path # type: ignore

app=FastAPI()      #const app=express();  its just like express

# GET=get an information
# POST=create new object in database
# PUT=update an object in database
# DELETE=delete an object in database

students={
    1:{
        "name":"john",
        "age":17,
        "class":"11th"
    },
    2:{
        "name":"Aditya",
        "age":18,
        "class":"12th"
    },
    3:{
        "name":"Rohan",
        "age":19,
        "class":"13th"
    
    }

}

# app.get('/',(req,res,next)=>{
#   res.send('Hello World')
# })
@app.get("/")
def index():
    return {"data":"hello world!!"}

@app.get("/about")
def about():
    return {"data":"about page"}


# app.get('/get-student/:student_id',(req,res,next)=>{
#    {student_id}=req.params
#   res.send(students[student_id])
# })
@app.get("/get-student/{student_id}")
# def get_student(student_id:int=Path(None,description="The ID of the student you want to view",le=2)):
def get_student(student_id:int):
  return students[student_id]


@app.get("/get-by-name")
def get_students(name: str):
    for student_id in students:
        if students[student_id]["name"].lower() == name.lower():
            return students[student_id]
    return {"data": "student not found"}
   
# python does not allow optional argument before required argument 
# def get_students(name:Optional[str]=None,test:int) here name is optional and test is required