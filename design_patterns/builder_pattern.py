import abc


class AbsBuilder(metaclass=abc.ABCMeta):

    def new_car(self):
        self.car = Car()

    def get_car(self):
        return self.car

    @abc.abstractmethod
    def build_body(self):
        pass

    @abc.abstractmethod
    def build_wheels(self):
        pass


class CarBuilder(AbsBuilder):

    def build_body(self):
        self.car.body = "Body"

    def build_wheels(self):
        self.car.wheels = "Continental"


class Director(object):

    def __init__(self, builder):
        self.builder = builder

    def build_car(self):
        self.builder.new_car()
        self.builder.build_body()
        self.builder.build_wheels()

    def get_car(self):
        return self.builder.get_car()


car_builder = Director(CarBuilder)
car_builder.build_car()
car = car_builder.get_car()
car.display()