""" Logging subsystem"""


class Singleton(type):
    # This kind of implementation give us possibility to reuse this Singleton as much as we want

    # dict([class_reference, class_instance)
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # if instance is not instantiated, add instance to _instances dictionary, otherwise return existing instance
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class MonoState(object):
    """
    Maintains the single state for all instances

    No matter how much instances of MonoState are created, they all share the one state
    """
    state = {}

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        self.__dict__ = cls.state
        return self


class Logger(MonoState):
    log_file = None

    def __init__(self, path):
        if self.log_file is None:
            self.log_file = open(path, mode='w')

    def write_log(self, log_record):
        self.log_file.writelines(log_record)

    def close_log(self):
        self.log_file.close()
        self.log_file = None


logger = Logger('mylog.log')
logger.write_log('Logging with classic Singleton\n')

logger2 = Logger('***ignored***')
logger2.write_log('Another log')

logger.close_log()

with open ('mylog.log', 'r') as f:
    for line in f:
        print(line)
