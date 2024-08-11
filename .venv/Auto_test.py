#Хоменко Ирина, 19-я когорта — Финальный проект. Инженер по тестированию плюс
import Configuration
import sender_stand_request
import Data


# объявление автотеста через test_
def test_order_creation():
# Создать заказ, для этого взять данные из data и путь из файла sender
    response = sender_stand_request.create_order(Data.order_body)

# Получение трека заказа
    track_number = response.json()["track"]

# Запрос по получению заказа через его номер трека
    response_order = sender_stand_request.get_order(track_number)

# Проверка кода 200 - запрос успешно обработан
    assert response_order.status_code == 200