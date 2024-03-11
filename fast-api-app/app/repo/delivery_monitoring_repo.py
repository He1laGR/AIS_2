from db_executor import execute
from models import DeliveryMonitoring, Delivery
import httpx


def create_package(package: DeliveryMonitoring):
    delivery = get_delivery_by_id(package.delivery_id)
    return execute("INSERT INTO delivery_service.delivery_monitoring" +
                   "(delivery_status, delivery_id, sender_id, delivery_date) " +
                   "VALUES(%s, %s, %s, %s, %s) RETURNING delivery_id;", (
                       package.delivery_id,
                       package.delivery_status,
                       package.sender_id,
                       delivery.delivery_date
                   ))


def get_delivery_by_id(delivery_id):
    url = "http://fast-api-delivery:82/delivery/get_by_id/" + delivery_id
    response = httpx.post(url)
    if response.status_code == 200:
        response_model = Delivery(**response.json())
        return response_model
    else:
        print(f"Error {response.status_code}: {response.text}")


def get_package_by_user_id(user_id: str):
    packages = []
    for item in execute("SELECT "
                       "delivery_id, "
                       "delivery_status, "
                       "sender_id, "
                       "delivery_date "
                       "FROM delivery_service.delivery_monitoring "
                       "WHERE sender_id = %s;", (user_id,)):
        package = DeliveryMonitoring()
        package.delivery_id = item[0]
        package.delivery_status = item[1]
        package.sender_id = item[2]
        package.delivery_date = item[3]
        packages.append(package)
        
    return packages
