import abc


class AbsTransport(metaclass=abc.ABCMeta):

    def __init__(self, destination):
        self.destination = destination

    # Define template method which defines order of execution

    def take_trip(self):
        self.start_engine()
        self.leave_terminal()
        self.entertainment()
        self.travel_to_destination()
        self.arrive_at_destination()

    @abc.abstractmethod
    def start_engine(self):
        pass

    # Concrete class - might be used in concrete implementation or override
    def leave_terminal(self):
        print("Leaving terminal")

    # Hook
    def entertainment(self):
        pass

    @abc.abstractmethod
    def travel_to_destination(self):
        print("Travelling..")

    def arrive_at_destination(self):
        print("Arriving at " + self.destination)


class Bus(AbsTransport):

    def start_engine(self):
        print("Starting bus engine")

    def travel_to_destination(self):
        print("Ridding...")

    def arrive_at_destination(self):
        print("Arriving at" + self.destination)


route = Bus("Bangladesh")
route.take_trip()
