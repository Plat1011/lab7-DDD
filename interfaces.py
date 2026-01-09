from abc import ABC, abstractmethod


class OrderRepository(ABC):
    @abstractmethod
    def get_by_id(self, order_id):
        pass

    @abstractmethod
    def save(self, order):
        pass


class PaymentGateway(ABC):
    @abstractmethod
    def charge(self, order_id, money):
        pass
