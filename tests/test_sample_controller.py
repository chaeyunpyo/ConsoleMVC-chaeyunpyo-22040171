from console_mvc.controller.sample_controller import SampleController
from console_mvc.model.repository import Repository


def test_register_and_list_sample():
    controller = SampleController(Repository())

    controller.register_sample("S-001", "Sample A", 10.0, 0.9, 100)

    samples = controller.list_samples()
    assert len(samples) == 1
    assert samples[0].sample_id == "S-001"
    assert samples[0].name == "Sample A"


def test_search_by_name():
    controller = SampleController(Repository())
    controller.register_sample("S-001", "Alpha", 10.0, 0.9, 100)
    controller.register_sample("S-002", "Beta", 5.0, 0.8, 50)

    result = controller.search_by_name("alp")

    assert len(result) == 1
    assert result[0].sample_id == "S-001"
