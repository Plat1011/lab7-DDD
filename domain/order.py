from domain.status import OrderStatus
from domain.money import Money


class OrderLine:
    def __init__(self, product_id: str, price: Money, qty: int):
        if qty <= 0:
            raise ValueError("qty must be positive")
        self.product_id = product_id
        self.price = price
        self.qty = qty

    def total(self) -> Money:
        return Money(self.price.amount * self.qty, self.price.currency)


class Order:
    def __init__(self, order_id: str):
        self.order_id = order_id
        self.lines: list[OrderLine] = []
        self.status = OrderStatus.CREATED

    def add_line(self, line: OrderLine):
        if self.status == OrderStatus.PAID:
            raise ValueError("Cannot modify paid order")
        self.lines.append(line)

    def total(self) -> Money:
        if not self.lines:
            return Money(0)
        result = Money(0, self.lines[0].price.currency)
        for line in self.lines:
            result += line.total()
        return result

    def pay(self):
        if not self.lines:
            raise ValueError("Cannot pay empty order")
        if self.status == OrderStatus.PAID:
            raise ValueError("Order already paid")
        self.status = OrderStatus.PAID
