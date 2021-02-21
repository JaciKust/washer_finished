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

    def is_running(self):
        return self.id > 0

NOT_RUNNING = WasherState(0, 'Not Running')
WASHING = WasherState(1, 'Washing')
SPINNING = WasherState(2, 'Spin')
