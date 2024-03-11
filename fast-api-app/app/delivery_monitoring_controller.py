from fastapi import FastAPI

from models import DeliveryMonitoring
from repo.delivery_monitoring_repo import get_package_by_user_id, create_package

app = FastAPI()


# Создание посылки
@app.post("/package/create")
async def create(package: DeliveryMonitoring):
    return create_package(package)


# Получение посылок пользователя
@app.get("/package/list/{user_id}")
async def list(user_id: str):
    return get_package_by_user_id(user_id)
