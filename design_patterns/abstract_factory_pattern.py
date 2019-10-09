"""
    For this example - pizza store

    Idea is that client can chose over Factory Pizza store which pizza to choose - italian or american
    Both types of pizzas have same attribute which decides what will be the form of the pizza - vege or not vege
"""

import abc


class PizzaStore(metaclass=abc.ABCMeta):
    """
        Abstract factory class providing two major differences between pizzas - vege or not vege
    """

    @abc.abstractmethod
    def create_vege_pizza(self):
        pass

    @abc.abstractmethod
    def create_non_vege_pizza(self):
        pass


class ItalianPizza(PizzaStore):
    """
        Concrete factory pizza will return concrete product
    """
    def create_non_vege_pizza(self):
        return ClassicItalianPizza()

    def create_vege_pizza(self):
        return ItalianVegePizza()


class AmericanPizza(PizzaStore):
    """
        Concrete factory pizza will return concrete product
    """

    def create_non_vege_pizza(self):
        return ClassicAmericanPizza()

    def create_vege_pizza(self):
        return AmericanVegePizza()


class VegePizza(metaclass=abc.ABCMeta):
    """
        Abstract product
    """
    @abc.abstractmethod
    def prepare(self):
        pass


class NonVegePizza(metaclass=abc.ABCMeta):
    """
        Abstract product
    """
    @abc.abstractmethod
    def prepare(self):
        pass


class ItalianVegePizza(VegePizza):
    """
    Concrete product
    """
    def prepare(self):
        print("Preparing", type(self).__name__)


class AmericanVegePizza(VegePizza):
    """
        Concrete product
    """
    def prepare(self):
        print("Preparing", type(self).__name__)


class ClassicItalianPizza(NonVegePizza):
    """
        Concrete product
    """
    def prepare(self):
        print(type(self).__name__, "is the best pizza")


class ClassicAmericanPizza(NonVegePizza):
    """
        Concrete product
    """
    def prepare(self):
        print("Preparing", type(self).__name__)


class PizzaStore:

    def __init__(self):
        pass

    @staticmethod
    def make_pizza():
        for factory in [ItalianPizza(), AmericanPizza()]:
            non_vege_pizza = factory.create_non_vege_pizza()
            vege_pizza = factory.create_vege_pizza()
            vege_pizza.prepare()
            non_vege_pizza.prepare()

pizza = PizzaStore()
pizza.make_pizza()
