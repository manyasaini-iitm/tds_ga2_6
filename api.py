from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json 

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins =["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers=["*"],
)
with open('q-vercel-python.json') as f:
    student_marks = json.load(f)

@app.get("/api")
async def get_marks(name:list[str]=Query(None)):
    if name:
        result = [student["marks"] for student in student_marks if student["name"] in name]
        return {"marks":result}
    
    return {"marks":[]}
