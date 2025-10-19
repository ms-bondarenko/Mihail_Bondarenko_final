# Diplome_Mihail_Bondarenko

## Автотесты для расписание школы SkyEng, протестированной в курсовых по ручному тестированию и API(https://sky-1.yonote.ru/doc/kursovaya-rabota-1-2-kurs-3ITw9Y6XMj), в рамках ui теста произведен смоук-тест Авторизаия , создание и удаление личного события с проверками выполненных шагов

### Для UI тестов применено Page Object
   

### Шаги
1. Склонировать проект 'git clone https://github.com/ms-bondarenko/Mihail_Bondarenko_final.git'
2. Установить все зависимости
3. 1)Создать виртуальное окружение и 2)активировать его: 1)python -m venv venv, 2)venv\scripts\activate # Windows
4. Если pytest не запускает проект то установите переменную окружения
- "$env:PYTHONPATH = "путь к корневой директории проекта"
- например ($env:PYTHONPATH="C:\Users\SMART\Desktop\diplom\Mihail_Bondarenko_final")
5. Установить зависимости: pip install -r requirements.txt
6. Зайти на страницу https://teachers.skyeng.ru/schedule предварительно авторизовавшись (login, pass текущий token в допах), открыть
   DevTool перейти на вкладку Application выбрать Cookies затем https://teachers.skyeng.ru найти token_global скопировать
   и вставить в config.py in Cookie = 'token_global=скопированный токен'(токен протухает каждый день)
7. Вставить значения в допах в соответствующие ключи в config.py

### Запуск тестов
- UI тесты: pytest tests/test_ui.py --alluredir=allure-results
- API тесты: pytest tests/test_api.py --alluredir=allure-results
- Все тесты: pytest --alluredir=allure-results
### Просмотр Allure отчёта
- Сформировать результаты: pytest --alluredir=allure-results
- Запустить сервер Allure: allure serve allure-results

### Стек:
- pytest
- selenium
- requests
- allure
- config

### Структура:
- ./test - тесты
- ./pages - описание страниц

### Полезные ссылки
- [Подсказка по Markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore/)

### Библиотеки
- allure-pytest==2.15.0
- pytest==8.4.1
- requests==2.32.4
- selenium==4.34.2
- webdriver-manager==4.0.2
- allure-python-commons~=2.15.0

### P.S.
- Периодически при старте теста подвисает страница авторизации в test_ui.py что дает сбой по всем тестам т.к. не произведена авторизация при следующем запуске все проходит нормально
- подождать до наступления следующих суток при проверке test_ui.py в воскресение после 23.00 (так как сервер создает событие на след день)