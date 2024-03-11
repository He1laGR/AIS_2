from datetime import datetime
from pydantic import BaseModel, Field


class User(BaseModel):
    user_id: str | None = None
    login: str = Field(default=None)
    password: str = Field(default=None)
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    email: str = Field(default=None)
    phone_number: str = Field(default=None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Delivery(BaseModel):
    delivery_id: str | None = None
    author_id: str | None = None
    weight: str | None = None
    category: str | None = None
    delivery_from: str | None = None
    delivery_to: str | None = None
    pay_method: datetime | None = None
    delivery_date: datetime | None = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class DeliveryMonitoring(BaseModel):
    delivery_id: str | None = None
    delivery_status: str | None = None
    sender_id: str | None = None
    delivery_date: datetime | None = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
