from console_mvc.model.repository import Repository


class ShippingController:
    def __init__(self, repository: Repository):
        self.repository = repository
