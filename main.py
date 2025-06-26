from fastapi import FastAPI

import uvicorn

app = FastAPI()

@app.get("/", summary='Ручка', tags=['Основные ручки'])
def home():
    return "Привет! Все работает!"

if __name__ == "__main__":
    uvicorn.run("main.app", reload=True)