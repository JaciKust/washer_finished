class AxisReading:
    def __init__(self, time, x, y, z,):
        self.time = time
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return 'time={0}, {1}, {2}, {3}'.format(self.time, self.x, self.y, self.z)

