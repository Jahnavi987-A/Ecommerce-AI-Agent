from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from utils.generate_sql import generate_sql
from utils.load_to_sql import execute_sql_query  # import this




app = FastAPI()

@app.get("/")
async def serve_index():
    return FileResponse("frontend/index.html")

class Question(BaseModel):
    question: str

@app.post("/generate_sql")
async def generate_sql_query(q: Question):
    sql = generate_sql(q.question)
    
    # Optionally execute the SQL
    result = execute_sql_query(sql)

    return {
        "sql": sql,
        "result": result
    }

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
