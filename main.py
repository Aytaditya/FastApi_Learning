from fastapi import FastAPI # type: ignore

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
        "name":"doe",
        "age":18,
        "class":"12th"
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
def get_student(student_id:int):
    return students[student_id]