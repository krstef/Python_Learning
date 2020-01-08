import abc

"""
Idea behind example:
Smartphone as client which wants to charge.

To be able to charge, we can use US or EU socket.

AbstractSocketAdapter defines abstract methods which will be used by Smartphone to charge.
Since US and EU sockets have different interfaces (different output voltage and adapter name- EU 230V AC,
US 120V AC), for each socket is needed special adapter to adapt output voltage to proper input voltage.

Using dependency injection we can initialize Smartphone with US or EU socket adapter and smartphone will 
be charge successfully
"""

#####################################
#           Object adapter          #
#####################################

"""
Composition is used in this object adapter example:
Concrete adapter(eg. EUSocketAdapter) implements AbstractSocketAdapter.
Concrete adapter also initializes corresponding Adaptee (eg. EUSocket) and adapts its behaviour to 
abstract adapter. 
"""


class AbstractSocketAdapter(metaclass=abc.ABCMeta):
    """
    This class represents abstract interface used by client
    """

    @abc.abstractmethod
    def get_input_voltage(self) -> int:
        pass

    @abc.abstractmethod
    def get_socket_adapter_name(self) -> str:
        pass


class EUSocketAdapter(AbstractSocketAdapter):
    """
    Adapts EU Socket to AbstractAdapter
    """
    def __init__(self):
        self.eu_socket = EUSocket

    def get_input_voltage(self) -> int:
        # Adapt EU Socket voltage (230V AC) to 5V DC required by smartphone
        return self.eu_socket.output_voltage - 225

    def get_socket_adapter_name(self) -> str:
        return self.eu_socket.socket_name


class USSocketAdapter(AbstractSocketAdapter):
    """
    Adapts US Socket to AbstractAdapter
    """
    def __init__(self):
        self.us_socket = USSocket

    def get_input_voltage(self) -> int:
        # Adapt US Socket voltage (120V AC) to 5V DC required by smartphone
        return self.us_socket.output_voltage - 115

    def get_socket_adapter_name(self) -> str:
        return self.us_socket.socket_name


class EUSocket:
    output_voltage = 230
    socket_name = "EU Socket"


class USSocket:
    output_voltage = 120
    socket_name = "US Socket"


####################################
#           Class adapter          #
####################################

# Empty for now

####################################
#               Client             #
####################################


class Smartphone:
    """
    Smartphone is client class which uses AbstractAdapter instance to start Smartphone charging
    """
    max_input_voltage = 5

    def __init__(self, adapter_ins):
        self.adapter_ins = adapter_ins

    def charge(self):
        if self.adapter_ins.get_input_voltage() > self.max_input_voltage:
            print(f"Input voltage is not properly set: {self.adapter_ins.get_input_voltage()}V instead of "
                  f"{self.max_input_voltage}V - your smartphone will burn :(")
        else:
            print(f"Charging with {self.adapter_ins.get_socket_adapter_name()}, voltage on "
                  f"{self.adapter_ins.get_input_voltage()}V")


####################################
#       Start of the program       #
####################################
def main():
    """
    Client uses methods exposed by abstract interface to be able to do some operations
    :return: void
    """
    eu_socket_ins = EUSocketAdapter()
    us_socket_ins = USSocketAdapter()

    # dependency injection
    Smartphone(eu_socket_ins).charge()
    Smartphone(us_socket_ins).charge()


if __name__ == "__main__":
    main()
