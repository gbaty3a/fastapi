from fastapi import FastAPI, Request, HTTPException
import uvicorn 
import pickle
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

# Загрузка модели из файла pickle
with open('model.pkl', 'rb') as fid:
    model = pickle.load(fid)


# Модель для валидации входных данных
class PredictionInput(BaseModel):
    bmi: float
    diastolic_blood_pressure: float
    systolic_blood_pressure: float
    income: float
    exercise_hours_per_week: float
    age: float
    cholesterol: float
    sedentary_hours_per_day: float
    triglycerides: float
    heart_rate: float


@app.get("/status", summary='Статус сервера')
def status():
    return "Все работает!"

@app.post("/predict", summary='Получить предсказание')
def predict_model(input_data: PredictionInput):

    # Создание DataFrame из данных
    data = pd.DataFrame({
        'bmi': [input_data.bmi],
        'diastolic_blood_pressure': [input_data.diastolic_blood_pressure],
        'systolic_blood_pressure': [input_data.systolic_blood_pressure],
        'income': [input_data.income],
        'exercise_hours_per_week': [input_data.exercise_hours_per_week],
        'age': [input_data.age],
        'cholesterol': [input_data.cholesterol],
        'sedentary_hours_per_day': [input_data.sedentary_hours_per_day],
        'triglycerides': [input_data.triglycerides],
        'heart_rate': [input_data.heart_rate]
    })

    # Предсказание
    predictions = model.predict(data)

    # Преобразование результата в человеко-читаемый формат
    result = "Высокая вероятность" if predictions[0] == 1 else "Низкая вероятность"

    return {"Риск сердечного приступа": result}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)