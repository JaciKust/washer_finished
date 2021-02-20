class WasherState:
    def __init__(self, id, name):
        self.id = id
        self.name = name

WASHING = WasherState(1, 'Washing')
SPIN = WasherState(2, 'Spin')
DONE = WasherState(3, 'Done')