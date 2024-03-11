from db_executor import execute
from models import Delivery


def create_delivery(delivery: Delivery):
    return execute("INSERT INTO delivery_service.delivery"
                   "(category, author_id, weight, pay_method, delivery_from, delivery_to) "
                   "VALUES(%s, %s, %s, %s, %s, %s) RETURNING delivery_id;", (
                       delivery.category,
                       delivery.author_id,
                       delivery.weight,
                       delivery.pay_method,
                       delivery.delivery_from,
                       delivery.delivery_to
                   ))


def get_delivery_by_id(delivery_id: str):
    deliveries = []
    for item in execute("SELECT "
                       "delivery_id, "
                       "author_id, "
                       "weight, "
                       "category, "
                       "delivery_from, "
                       "delivery_to, "
                       "pay_method, "
                       "delivery_date "
                       "FROM delivery_service.delivery "
                       "WHERE delivery_id = %s;", (delivery_id,)):
        
        delivery = Delivery()
        delivery.delivery_id = item[0]
        delivery.author_id = item[1]
        delivery.weight = item[2]
        delivery.category = item[3]
        delivery.delivery_from = item[4]
        delivery.delivery_to = item[5]
        delivery.pay_method = item[6]
        delivery.delivery_date = item[7]
        deliveries.append(delivery)

    if len(deliveries) == 1:
        return deliveries[0]
    else:
        return None


def get_delivery_by_sender_id_and_delivery_id(author_id: str, delivery_id: str):
    deliveries = []
    for item in execute("SELECT "
                       "delivery_id, "
                       "author_id, "
                       "weight, "
                       "category, "
                       "delivery_from, "
                       "delivery_to, "
                       "pay_method, "
                       "delivery_date "
                       "FROM delivery_service.delivery "
                       "WHERE sender_id = %s and delivery_id = %s;", (author_id, delivery_id)):

        delivery = Delivery()
        delivery.id = item[0]
        delivery.title = item[1]
        delivery.sender_id = item[2]
        delivery.applier_id = item[3]
        delivery.status = item[4]
        delivery.insert_date = item[5]
        delivery.update_date = item[6]
        deliveries.append(delivery)

    return deliveries
