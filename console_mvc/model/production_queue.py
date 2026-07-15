import math
from datetime import datetime


class ProductionQueueItem:
    def __init__(self, order_id: str, sample_id: str, shortage_qty: int,
                 avg_production_time: float, yield_rate: float, enqueued_at: datetime = None):
        self.order_id = order_id
        self.sample_id = sample_id
        self.shortage_qty = shortage_qty
        self.actual_production_qty = math.ceil(shortage_qty / yield_rate)
        self.total_production_time = avg_production_time * self.actual_production_qty
        self.enqueued_at = enqueued_at or datetime.now()
