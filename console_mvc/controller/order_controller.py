import itertools
from datetime import datetime

from console_mvc.model.order import Order, OrderStatus
from console_mvc.model.production_queue import ProductionQueueItem
from console_mvc.model.repository import Repository


class OrderController:
    def __init__(self, repository: Repository):
        self.repository = repository
        self._counter = itertools.count(1)

    def create_order(self, sample_id: str, customer_name: str, quantity: int) -> Order:
        if self.repository.get_sample(sample_id) is None:
            raise ValueError(f"존재하지 않는 시료입니다: {sample_id}")
        order = Order(self._generate_order_id(), sample_id, customer_name, quantity)
        self.repository.add_order(order)
        return order

    def list_reserved_orders(self) -> list[Order]:
        return [o for o in self.repository.list_orders() if o.status == OrderStatus.RESERVED]

    def reject_order(self, order_id: str) -> Order:
        order = self._get_reserved_order(order_id)
        order.status = OrderStatus.REJECTED
        return order

    def approve_order(self, order_id: str) -> Order:
        order = self._get_reserved_order(order_id)
        sample = self.repository.get_sample(order.sample_id)

        if sample.stock >= order.quantity:
            sample.stock -= order.quantity
            order.status = OrderStatus.CONFIRMED
        else:
            shortage_qty = order.quantity - sample.stock
            sample.stock = 0
            self.repository.production_queue.append(
                ProductionQueueItem(
                    order.order_id, sample.sample_id, shortage_qty,
                    sample.avg_production_time, sample.yield_rate,
                )
            )
            order.status = OrderStatus.PRODUCING
        return order

    def _get_reserved_order(self, order_id: str) -> Order:
        order = self.repository.get_order(order_id)
        if order is None:
            raise ValueError(f"존재하지 않는 주문입니다: {order_id}")
        if order.status != OrderStatus.RESERVED:
            raise ValueError(f"승인/거절 가능한 상태가 아닙니다: {order.status.value}")
        return order

    def _generate_order_id(self) -> str:
        today = datetime.now().strftime("%Y%m%d")
        seq = next(self._counter)
        return f"ORD-{today}-{seq:04d}"
