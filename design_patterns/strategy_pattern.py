"""
    Contains:
     Context - uses interface to execute various concrete strategies
     Interface - an abstract class
     Concrete Strategies - inherits from interface to ensure the same input
     and generate the same type of output, allowing to have specific strategy implementation

    Demo example: System that processes customer orders and it should calculate shipping cost
    for each shipper

    Goal: Easier adding of new shipper, meaning only new concrete strategy will be added and
    rest of the logic/implementation remains the same
    Note - concrete strategy implementation might be classes, methods, lambdas
"""
import abc


class ShippingCost(object):

    def __init__(self, shipper):
        self.shipper = shipper

    def shipping_cost(self):
        return self.shipper.calculate_costs()


class ShipperInterface(metaclass=abc.ABCMeta):

    def __init__(self):
        pass

    @abc.abstractmethod
    def calculate_costs(self):
        pass


class Fedex(ShipperInterface):

    def __init__(self):
        super().__init__()

    def calculate_costs(self):
        return 7.50


class Ups(ShipperInterface):
    def __init__(self):
        super().__init__()

    def calculate_costs(self):
        return 7.00


def main():
    """ Execution flow handling
        First create instances of dog and cat
        Pass instances to print_animal_behaviour func
    """
    fedex_strategy = Fedex()
    cost = ShippingCost(fedex_strategy)
    print(cost.shipping_cost())

    ups_strategy = Ups()
    cost = ShippingCost(ups_strategy)
    print(cost.shipping_cost())


if __name__ == "__main__":
    main()
