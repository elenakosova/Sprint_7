import allure
import pytest
import requests
from data import Url, ResponseWithError
from helpers import Delivery


class TestAuthCourier:

    @allure.title('Проверка успешной авторизации курьера')
    def test_courier_authorization(self):
        payload = Delivery.register_courier()
        response = requests.post(Url.authorization_courier, data=payload)
        assert response.status_code == 200 and 'id' in response.text

    @pytest.mark.parametrize('field', ['login', 'password'])
    @allure.title('Проверка авторизации с неверным значением поля пароля или логина')
    def test_auth_with_wrong_one_values_field(self, field):
        payload = Delivery.register_courier()
        payload[field] = ''
        response = requests.post(Url.authorization_courier, data=payload)
        assert response.status_code == 400 and response.json()['message'] == ResponseWithError.BAD_REQUEST

    @pytest.mark.parametrize('field', ['login', 'password'])
    @allure.title('Проверка авторизации без поля пароля или логина')
    def test_auth_without_one_field(self, field):
        payload = Delivery.register_courier()
        del payload[field]
        response = requests.post(Url.authorization_courier, data=payload)
        assert response.status_code == 400 and response.json()['message'] == ResponseWithError.BAD_REQUEST

    @allure.title('Проверка авторизации с несуществующим курьером')
    def test_auth_with_unexist_courier(self):
        payload = Delivery.register_courier()
        payload['login'] = payload['login'] + '1'
        response = requests.post(Url.authorization_courier, data=payload)
        assert response.status_code == 404 and response.json()['message'] == ResponseWithError.ACCOUNT_NOT_FOUND