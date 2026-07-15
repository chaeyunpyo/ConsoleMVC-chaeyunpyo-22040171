from datetime import datetime
from enum import Enum


class OrderStatus(Enum):
    RESERVED = "RESERVED"
    REJECTED = "REJECTED"
    PRODUCING = "PRODUCING"
    CONFIRMED = "CONFIRMED"
    RELEASE = "RELEASE"


class Order:
    def __init__(self, order_id: str, sample_id: str, customer_name: str, quantity: int,
                 status: OrderStatus = OrderStatus.RESERVED, created_at: datetime = None):
        self.order_id = order_id
        self.sample_id = sample_id
        self.customer_name = customer_name
        self.quantity = quantity
        self.status = status
        self.created_at = created_at or datetime.now()
