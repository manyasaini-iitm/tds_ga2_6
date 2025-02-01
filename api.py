from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json 

app = FastAPI()
app.add.middleware(
    CORSMiddleware,
    allow_origins =["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers=["*"],
)
with open('q-vercel-python.json') as f:
    student_marks = json.load(f)

@app.get("/api")
async def get_marks():
    marks = [student_marks.get(n,0) for n in name]
    return {"marks":marks}
