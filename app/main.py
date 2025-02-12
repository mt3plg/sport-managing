from fastapi import FastAPI
from app.routes import participants

app = FastAPI()

# Підключення маршрутів
app.include_router(participants.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Sport Competitions API"}