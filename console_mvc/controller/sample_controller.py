from console_mvc.model.repository import Repository
from console_mvc.model.sample import Sample


class SampleController:
    def __init__(self, repository: Repository):
        self.repository = repository

    def register_sample(self, sample_id: str, name: str, avg_production_time: float,
                         yield_rate: float, stock: int) -> Sample:
        sample = Sample(sample_id, name, avg_production_time, yield_rate, stock)
        self.repository.add_sample(sample)
        return sample

    def list_samples(self) -> list[Sample]:
        return self.repository.list_samples()

    def search_by_name(self, keyword: str) -> list[Sample]:
        return self.repository.search_samples_by_name(keyword)
