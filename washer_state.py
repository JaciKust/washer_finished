class WasherState:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.id == other.id
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.name

WASHING = WasherState(1, 'Washing')
SPINNING = WasherState(2, 'Spin')
NOT_RUNNING = WasherState(3, 'Not Running')