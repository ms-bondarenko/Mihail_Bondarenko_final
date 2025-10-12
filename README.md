# Diplome_Mihail_Bondarenko

## Автотесты для расписание школы SkyEng в рамках ui теста произведен смоук-тест Авторизаия , создание и удаление личного события с проверками выполненных шагов

### Для UI тестов применено Page Object
   

### Шаги
1. Склонировать проект 'git clone https://github.com/ms-bondarenko/Mihail_Bondarenko_final.git'
2. Установить все зависимости
3. 1)Создать виртуальное окружение и 2)активировать его: 1)python -m venv venv 2)venv\Scripts\activate # Windows
4. Если pytest не запускает проект то установите переменную окружения
- "$env:PYTHONPATH = "путь к корневой директории проекта"
- например ($env:PYTHONPATH="C:\Users\SMART\Desktop\diplom\Mihail_Bondarenko_final")
5. Установить зависимости: pip install -r requirements.txt

### Запуск тестов
- UI тесты: pytest tests/test_ui.py --alluredir=allure-results
- API тесты: pytest test_api.py --alluredir=allure-results
- Все тесты: pytest --alluredir=allure-results
- Просмотр Allure отчёта
- Сформировать результаты: pytest --alluredir=allure-results
- Запустить сервер Allure: allure serve allure-results

### Стек:
- pytest
- selenium
- requests
- _sqlalchemy_
- allure
- config

### Структура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хэлперы для работы с api
- ./db - хэлперы для работы с БД

### Полезные ссылки
- [Подсказка по Markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore/)

### Библиотеки
- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install requests

### Если pytest не запускает проект то установите переменную окружения
- "$env:PYTHONPATH = "путь к корневой директории проекта"
- например ($env:PYTHONPATH="C:\Users\SMART\Desktop\diplom\Mihail_Bondarenko_final")


 Периодически при старте теста подвисает страница авторизации что дает сбой по всем тестам т.к. не произведена авторизация при следующем запуске все проходит нормально
