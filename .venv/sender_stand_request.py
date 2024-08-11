#импортирование данных из файлов
import Configuration
import requests
# функция для создания новго заказа (post запрос по документации API)
def create_order(body):
    return requests.post (Configuration.URL_SERVICE + Configuration.CREATE_ORDER_PATH,
                         json = body)

# функция для получения заказа по номеру трекера (get запрос по документу API)
def get_order(track_number):
#/v1/orders/track?t=123456 - путь для получения заказа по номеру
#t - трекинговый номер заказа
    get_order_url = f"{Configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response
