# Предсказание рисков сердечного приступа

1. Исследовательский анализ данных, модель МО, выводы можно посмотреть в [ноутбуке](heart_attack_risk.ipynb)
2. Предсказания на тестовых данных в формате [csv-файла](heart_test_pred.csv), содержат id пациента и предсказанную вероятность сердечного приступа в бинарном виде.
3. Код [приложения](main.py) для локального запуска.
### Инструкция для запуска:
Файл [main.py](main.py) содержит простое API-приложение с двумя ручками: одна для проверки работы API сервиса, другая для получения предсказания по введенным данным.

1. Перед запуском необходимо создать рабочее окружение и установить необходимые библиотеки. Файл [requirements.txt](fastapi\requirements.txt) содержит библиотеки с указанными версиями. Установить зависимости можно командой `pip install -r requirements.txt`
2. Запустить приложение из командной строки  - `python main.py`
3. Проверить работу API приложения можно с помощью утилиты **curl**
- `curl -X GET http://127.0.0.1:8000/status` проверить работу ручки *status*
- `curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d "{\"bmi\": 0.28, \"diastolic_blood_pressure\": 0.37, \"systolic_blood_pressure\": 0.28, \"income\": 0.59, \"exercise_hours_per_week\": 0.36, \"age\": 0.49, \"cholesterol\": 0.26, \"sedentary_hours_per_day\": 0.19, \"triglycerides\": 0.31, \"heart_rate\": 0.06}"` - для получения предсказания *высокая вероятность*
- `curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d "{\"bmi\": 0.91, \"diastolic_blood_pressure\": 0.26, \"systolic_blood_pressure\": 0.74, \"income\": 0.37, \"exercise_hours_per_week\": 0.44, \"age\": 0.46, \"cholesterol\": 0.57, \"sedentary_hours_per_day\": 0.79, \"triglycerides\": 0.16, \"heart_rate\": 0.05}"` - для получения предсказания *низкая вероятность*