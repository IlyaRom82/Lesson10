# Автоматизация тестирования (Lesson 10)

Проект содержит автотесты на **Selenium + Pytest + Allure**.  
Тестируются:

- простой калькулятор;
- сайт [SauceDemo](https://www.saucedemo.com/).

## 📂 Структура проекта

Lesson10/
│
├─ pages/ # PageObject классы
│ ├─ calculator_page.py
│ └─ login_page.py
│
├─ lesson_10/ # Тесты
│ ├─ test_calculator.py
│ └─ test_saucedemo.py
│
├─ .venv/ # Виртуальное окружение
├─ requirements.txt
└─ README.md

r
Копировать код

## 🚀 Установка и запуск тестов

1. Активируйте виртуальное окружение:

```bash
.venv\Scripts\activate
Установите зависимости:

bash
Копировать код
pip install -r requirements.txt
Запустите тесты с генерацией результатов для Allure:

bash
Копировать код
python -m pytest lesson_10 --alluredir=allure-results
📊 Просмотр Allure отчёта
Сгенерировать и открыть интерактивный отчёт:

bash
Копировать код
allure serve allure-results
Или с генерацией HTML-отчёта:

bash
Копировать код
allure generate allure-results -o allure-report --clean
allure open allure-report
⚠️ Примечание:

Папки allure-results и allure-report не нужно добавлять в git (можно пушить только пустые).

Для работы Allure необходимо установить Allure Commandline. Подробнее: Allure Framework.