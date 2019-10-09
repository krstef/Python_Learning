import abc


class AbsAuto(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def drive(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass


class Vw(AbsAuto):

    def drive(self):
        print("VW started, driving")

    def stop(self):
        print("Stop Vw")


class Opel(AbsAuto):

    def drive(self):
        print("Opel started, driving")

    def stop(self):
        print("Stop Opel")


class CarFactory(object):
    cars = {}  # key = car model, value= class for the car

    def start_and_drive(self, object_type):
        return eval(object_type)().drive()

    def stop(self, object_type):
        return eval(object_type)().stop()

# Client code

factory = CarFactory()

factory.start_and_drive("Vw")
factory.start_and_drive("Opel")

factory.stop("Vw")
factory.stop("Opel")

