import allure
import requests
from data import Url


class TestOrderList:

    @allure.title('Проверка статуса успешных заказов и добавление их в список заказов')
    def test_check_status_order_list(self):
        response = requests.get(Url.making_order)
        assert response.status_code == 200 and 'orders' in response.text