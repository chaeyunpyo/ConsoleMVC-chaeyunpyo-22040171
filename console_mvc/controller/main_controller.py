from console_mvc.controller.monitoring_controller import MonitoringController
from console_mvc.controller.order_controller import OrderController
from console_mvc.controller.production_controller import ProductionController
from console_mvc.controller.sample_controller import SampleController
from console_mvc.controller.shipping_controller import ShippingController
from console_mvc.model.repository import Repository


class MainController:
    def __init__(self):
        self.repository = Repository()
        self.sample_controller = SampleController(self.repository)
        self.order_controller = OrderController(self.repository)
        self.monitoring_controller = MonitoringController(self.repository)
        self.production_controller = ProductionController(self.repository)
        self.shipping_controller = ShippingController(self.repository)

    def get_summary(self) -> dict:
        samples = self.repository.list_samples()
        return {
            "sample_count": len(samples),
            "total_stock": sum(s.stock for s in samples),
            "order_count": len(self.repository.list_orders()),
            "production_queue_count": len(self.repository.production_queue),
        }
