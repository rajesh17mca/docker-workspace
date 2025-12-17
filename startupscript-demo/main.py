import os
from datetime import datetime
from fastapi import FastAPI
import logging

app = FastAPI()

logging.basicConfig(
    filename='/app/data/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@app.get("/")
async def root():
    logging.info("Root API Executed")
    return {"message": "Welcome to FastAPI with Rajesh" }

@app.get("/api/greet/{username}")
async def greet_name(username: str):
     logging.info("API /api/greet/" + username + " has been called")
     return {"message": "Welcome to FastAPI, Dear " + username }

@app.get("/api/status/{task}")
async def task_status(task: str):
     logging.info("Task status for the " + task + " has been called")
     return {"message": "Task " + task + " Completed" }