import allure
import pytest
import requests
from data import Url, ResponseWithError
from helpers import Delivery


class TestCreateCourier:

    @allure.title('Проверка создания курьера с корректными данными')
    def test_create_courier_correct_data_ok_true(self):
        payload = Delivery.generation_data_for_registration()
        response = requests.post(Url.create_courier, data=payload)
        assert response.status_code == 201 and response.json().get('ok') == True

    @allure.title('Проверка, что нельзя создать двух курьеров с одинаковыми данными')
    def test_create_two_similar_couriers(self):
        payload = Delivery.generation_data_for_registration()
        requests.post(Url.create_courier, data=payload)
        response = requests.post(Url.create_courier, data=payload)
        assert response.status_code == 409 and response.json()['message'] == ResponseWithError.LOGIN_IS_BUSY

    @allure.title('Проверка создания курьера без одного поля.')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_create_courier_without_one_field(self, field):
        payload = Delivery.register_courier()
        del payload[field]
        response = requests.post(Url.create_courier, data=payload)
        assert response.status_code == 400 and response.json()['message'] == ResponseWithError.AUTH_BAD_REQUEST