from console_mvc.model.order import Order
from console_mvc.model.production_queue import ProductionQueueItem
from console_mvc.model.sample import Sample


class Repository:
    def __init__(self):
        self.samples: dict[str, Sample] = {}
        self.orders: dict[str, Order] = {}
        self.production_queue: list[ProductionQueueItem] = []

    def add_sample(self, sample: Sample) -> None:
        self.samples[sample.sample_id] = sample

    def get_sample(self, sample_id: str) -> Sample | None:
        return self.samples.get(sample_id)

    def list_samples(self) -> list[Sample]:
        return list(self.samples.values())

    def search_samples_by_name(self, keyword: str) -> list[Sample]:
        return [s for s in self.samples.values() if keyword.lower() in s.name.lower()]

    def add_order(self, order: Order) -> None:
        self.orders[order.order_id] = order

    def get_order(self, order_id: str) -> Order | None:
        return self.orders.get(order_id)

    def list_orders(self) -> list[Order]:
        return list(self.orders.values())
