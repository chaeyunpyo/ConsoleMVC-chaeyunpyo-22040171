from console_mvc.model.repository import Repository


class ProductionController:
    def __init__(self, repository: Repository):
        self.repository = repository
