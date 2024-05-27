import json
import allure
import pytest
import requests
from data import Url, Order


class TestMakeOrder:

    @allure.title('Проверка создания заказа с разными значениями для поля "Цвет самоката"')
    @pytest.mark.parametrize('choose_color', [[], ['BLACK'], ['GREY'], ['BLACK', 'GREY']])
    def test_make_order(self, choose_color):
        payload = Order.data_for_order
        payload['color'] = choose_color
        payload = json.dumps(payload)
        response = requests.post(Url.making_order, payload)
        assert response.status_code == 201 and 'track' in response.text