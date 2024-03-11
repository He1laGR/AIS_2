from fastapi import FastAPI

from models import Delivery
from repo.delivery_repo import create_delivery, get_delivery_by_sender_id_and_delivery_id, get_delivery_by_id

app = FastAPI()


# Создание доставки
@app.post("/delivery/create")
async def create(delivery: Delivery):
    return create_delivery(delivery)


# Получение информации о доставке по отправителю
@app.post("/delivery/sender/{sender_id}/{delivery_id}")
async def info_by_sender(sender_id, delivery_id):
    return get_delivery_by_sender_id_and_delivery_id(sender_id, delivery_id)


# Получение информации о доставке по id доставки
@app.post("/delivery/get_by_id/{delivery_id}")
async def info_by_sender(delivery_id):
    return get_delivery_by_id(delivery_id)
