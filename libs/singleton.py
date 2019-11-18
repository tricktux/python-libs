class Singleton(type):
    """Pythonic implementation of a singleton"""

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(
                *args, **kwargs)

        return cls._instances[cls]
