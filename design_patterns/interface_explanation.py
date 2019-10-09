import abc


class Animal(metaclass=abc.ABCMeta):
    """ This is an interface - abstract class"""
    def __init__(self):
        pass

    # abstract method which must be implemented in interface implementation
    @abc.abstractmethod
    def animal_sound(self) -> str:
        pass


class Dog(Animal):
    """ Dog inherits from Animal, this is concrete interface implementation"""

    def __init__(self):
        super().__init__()

    # Implementation of interface abstract method
    def animal_sound(self):
        return "VAU VAU"


class Cat(Animal):
    """ Cat inherits from Animal, this is concrete interface implementation"""

    def __init__(self):
        super().__init__()

    # Implementation of interface abstract method
    def animal_sound(self):
        return "MIJAU MIJAU"


def print_animal_behaviour(animal_ins: Animal):
    """ Uses Animal interface for printing """
    animal_sound = animal_ins.animal_sound()
    print(animal_sound)


def main():
    """ Execution flow handling
        First create instances of dog and cat
        Pass instances to print_animal_behaviour func
    """
    dog_ins = Dog()
    cat_ins = Cat()
    # Dependency injection
    print_animal_behaviour(dog_ins)
    print_animal_behaviour(cat_ins)


if __name__ == "__main__":
    main()
