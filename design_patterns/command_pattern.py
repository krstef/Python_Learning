"""
    Demo example: Command line order processing program with three options: create order, update quantity and ship order

    Pattern contains:


    Goal:
    Note -
"""

import abc


class CommandInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self, arg):
        pass


class AdditionCommand(CommandInterface):
    def __init__(self, args):
        self.args = args

    def execute(self, arg):
        self.args.addition(arg)


class DeductionCommand(CommandInterface):

    def __init__(self, args):
        self.args = args

    def execute(self, arg):
        self.args.deduction(arg)


class MultiplicationCommand(CommandInterface):
    def __init__(self, args):
        self.args = args

    def execute(self, arg):
        self.args.multiplication(arg)


class Receiver:
    """ Here you can put handling for each command"""
    const = 10

    def addition(self, arg):
        print(self.const + arg)

    def deduction(self, arg):
        print(self.const - arg)

    def multiplication(self, arg):
        print(self.const*self.const)


class Invoker:

    def __init__(self):
        self.order = []

    def order_handler(self, order, arg):
        self.order.append(order)
        order.execute(arg)


def main():
    # Client
    recv = Receiver()
    # pass recv instance to each command implementation
    add = AdditionCommand(recv)
    ded = DeductionCommand(recv)
    mult = MultiplicationCommand(recv)

    invoker = Invoker()
    invoker.order_handler(add, 5)
    invoker.order_handler(ded, 5)
    invoker.order_handler(mult, None)

if __name__ == '__main__':
    main()
