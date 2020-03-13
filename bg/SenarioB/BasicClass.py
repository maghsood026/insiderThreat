
class Basic:
    def __init__(self):
        pass

    def __iter__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__