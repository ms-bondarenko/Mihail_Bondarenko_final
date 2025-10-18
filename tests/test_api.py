import allure
import requests
import json
from config import base_url_api, Cookie, Cookie_err
import pytest

headers = {
    "Cookie": Cookie,
    "Content-Type": "application/json"
}
headers_err = {
    "Cookie": Cookie_err,
    "Content-Type": "application/json"
}


@allure.title('Запрос расписания')
def test_get_schedule():
    with allure.step('с корректным токеном'):
        url = f"{base_url_api}/schedule/events"
        payload = {
            "from": "2025-10-13T00:00:00+03:00",''
            "till": "2025-10-20T00:00:00+03:00",
            "onlyTypes": []
        }
        response = requests.post(url, headers=headers, json=payload)
    with allure.step('проверка статус кода'):
        assert response.status_code == 200
        print(response)

def test_auth_tokenError():
    with allure.step('с кривым токеном'):
        url = f"{base_url_api}/schedule/events"
        payload = {
            "from": "2025-10-13T00:00:00+03:00",
            "till": "2025-10-20T00:00:00+03:00",
            "onlyTypes": []
        }
        response = requests.post(url, headers=headers_err, json=payload)
    with allure.step('проверка статус кода'):
        assert response.status_code == 401
        print(response)


@allure.title('Создание личного события')
def test_create_event():
    with allure.step('создание личного события'):
        url = f"{base_url_api}/schedule/createPersonal"
        body = {"backgroundColor": "#F4F5F6",
         "color": "#81888D",
         "description": "Тестовое Событие",
         "title": "Тестовое Событие Бондаренко",
         "startAt": "2025-10-19T20:00:00+03:00",
         "endAt": "2025-10-19T20:30:00+03:00"
         }
        resp = requests.post(url, headers=headers, json=body)
    with allure.step('получение переменной id и вывод её в консоль для проверки'):
        data = resp.json()
        id = data['data']['payload']['id']
        print(id)
    with allure.step('проверка статус кода'):
        assert resp.status_code == 200

    with allure.step('удаление события для очистки тестового пространства'):
        url = f"{base_url_api}/schedule/removePersonal"
        body = {
            "startAt": "2025-10-19T20:00:00+03:00",
            "id": id
        }
        requests.post(url, headers=headers, json=body)

@allure.story('Редактирование личного события')
def test_update_title_event():
    with allure.step('Создание личного события для последующего редактирования'):
        url = f"{base_url_api}/schedule/createPersonal"
        body = {"backgroundColor": "#F4F5F6",
                "color": "#81888D",
                "description": "Тестовое Событие",
                "title": "Тестовое Событие Бондаренко",
                "startAt": "2025-10-19T20:00:00+03:00",
                "endAt": "2025-10-19T20:30:00+03:00"
                }
        resp = requests.post(url, headers=headers, json=body)
    with allure.step('получение id'):
        data = resp.json()
        id = data['data']['payload']['id']

    with allure.step('редактирование личного события'):
        url = f'{base_url_api}/schedule/updatePersonal'
        body ={
            "color": "#81888D",
            "id": id,
            "title": "ТTTTестовое Событие Бондаренко",
            "endAt": "2025-10-19T20:30:00+03:00",
            "startAt": "2025-10-19T20:00:00+03:00",
            "oldStartAt": "2025-10-19T20:00:00+03:00",
            "parentId": None,
            "description": "Тестовое Событие",
            "backgroundColor": "#F4F5F6"
        }
        resp = requests.post(url, headers=headers, json=body)
    with allure.step('получение значение ключа title'):
        data= resp.json()
        title = data['data']['payload']['payload']['title']
    with allure.step('сравнение полученного значения ключа "title" ожидаемым знначением'):
        assert title == "ТTTTестовое Событие Бондаренко"

    with allure.step('удаление события для очистки тестового пространства'):
        url = f"{base_url_api}/schedule/removePersonal"
        body = {
            "startAt": "2025-10-19T20:00:00+03:00",
            "id": id
        }
        requests.post(url, headers=headers, json=body)
@allure.title('удаление личного события')
def test_delete_event():
    with allure.step('создание личного события для последующего удаления'):
        url = f"{base_url_api}/schedule/createPersonal"
        body = {"backgroundColor": "#F4F5F6",
                "color": "#81888D",
                "description": "Тестовое Событие",
                "title": "Тестовое Событие Бондаренко",
                "startAt": "2025-10-19T20:00:00+03:00",
                "endAt": "2025-10-19T20:30:00+03:00"
                }
        resp = requests.post(url, headers=headers, json=body)
    with allure.step('получение id'):
        data = resp.json()
        id = data['data']['payload']['id']

    with allure.step('удаление личного события'):
        url = f"{base_url_api}/schedule/removePersonal"
        body = {
            "startAt": "2025-10-19T20:00:00+03:00",
            "id": id
        }
        resp = requests.post(url, headers=headers, json=body)
    with allure.step('извлечение  ответа от сервера о выполнении'):
        data = resp.json()
        event = data['data']
        print(event)
    with allure.step('сравнение ответа от сервера с ожидаемым результатом'):
        assert event == True
