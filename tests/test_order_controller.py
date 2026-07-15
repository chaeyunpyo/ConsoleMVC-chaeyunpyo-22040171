import pytest

from console_mvc.controller.order_controller import OrderController
from console_mvc.controller.sample_controller import SampleController
from console_mvc.model.order import OrderStatus
from console_mvc.model.repository import Repository


def _setup(stock: int):
    repository = Repository()
    SampleController(repository).register_sample("S-001", "Sample A", 10.0, 0.9, stock)
    return OrderController(repository), repository


def test_create_order_is_reserved():
    controller, _ = _setup(stock=100)

    order = controller.create_order("S-001", "customer-1", 10)

    assert order.status == OrderStatus.RESERVED
    assert order.order_id.startswith("ORD-")


def test_reject_order():
    controller, _ = _setup(stock=100)
    order = controller.create_order("S-001", "customer-1", 10)

    rejected = controller.reject_order(order.order_id)

    assert rejected.status == OrderStatus.REJECTED


def test_approve_order_with_sufficient_stock_confirms_and_deducts_stock():
    controller, repository = _setup(stock=100)
    order = controller.create_order("S-001", "customer-1", 10)

    approved = controller.approve_order(order.order_id)

    assert approved.status == OrderStatus.CONFIRMED
    assert repository.get_sample("S-001").stock == 90
    assert repository.production_queue == []


def test_approve_order_with_insufficient_stock_starts_production():
    controller, repository = _setup(stock=5)
    order = controller.create_order("S-001", "customer-1", 20)

    approved = controller.approve_order(order.order_id)

    assert approved.status == OrderStatus.PRODUCING
    assert repository.get_sample("S-001").stock == 0
    assert len(repository.production_queue) == 1

    item = repository.production_queue[0]
    assert item.order_id == order.order_id
    assert item.shortage_qty == 15
    assert item.actual_production_qty == 17  # ceil(15 / 0.9)
    assert item.total_production_time == pytest.approx(170.0)  # 10.0 * 17


def test_approve_non_reserved_order_raises():
    controller, _ = _setup(stock=100)
    order = controller.create_order("S-001", "customer-1", 10)
    controller.reject_order(order.order_id)

    with pytest.raises(ValueError):
        controller.approve_order(order.order_id)
