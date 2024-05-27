class Order:
    data_for_order = {
        "firstName": "Test",
        "lastName": "Testov",
        "address": "Testovaya ulitsa",
        "metroStation": 10,
        "phone": "+7 902 808 42 95",
        "rentTime": 4,
        "deliveryDate": "2024-05-30",
        "comment": "Good Luck",
        "color": []
    }


class Url:
    create_courier = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
    authorization_courier = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    making_order = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'

class ResponseWithError:
    LOGIN_IS_BUSY = 'Этот логин уже используется. Попробуйте другой.'
    AUTH_BAD_REQUEST = 'Недостаточно данных для создания учетной записи'
    BAD_REQUEST = 'Недостаточно данных для входа'
    ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'