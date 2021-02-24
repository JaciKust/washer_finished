import unittest
from datetime import datetime, timedelta

from washer_data_reader import WasherDataReader

from axis_reading import AxisReading
from washer_data_set import WasherDataSet
# These tests were created to make sure that the testing for data points doesn't get worse with an approvement.

class TestWasherDataSetGetStart(unittest.TestCase):

    time_0 = datetime(year=2021, month=2, day=1, hour=5, minute=1)
    time_1 = datetime(year=2021, month=2, day=1, hour=5, minute=2)
    time_2 = datetime(year=2021, month=2, day=1, hour=5, minute=3)
    time_3 = datetime(year=2021, month=2, day=1, hour=5, minute=4)
    time_4 = datetime(year=2021, month=2, day=1, hour=5, minute=5)
    time_5 = datetime(year=2021, month=2, day=1, hour=5, minute=6)
    time_6 = datetime(year=2021, month=2, day=1, hour=5, minute=7)
    time_7 = datetime(year=2021, month=2, day=1, hour=5, minute=8)
    time_8 = datetime(year=2021, month=2, day=1, hour=5, minute=9)
    time_9 = datetime(year=2021, month=2, day=1, hour=5, minute=10)
    time_10 = datetime(year=2021, month=2, day=1, hour=5, minute=11)

    def get_full_array(self):
        return WasherDataSet([
            self._to_axis_reading(self.time_0),
            self._to_axis_reading(self.time_1),
            self._to_axis_reading(self.time_2),
            self._to_axis_reading(self.time_3),
            self._to_axis_reading(self.time_4),
            self._to_axis_reading(self.time_5),
            self._to_axis_reading(self.time_6),
            self._to_axis_reading(self.time_7),
            self._to_axis_reading(self.time_8),
            self._to_axis_reading(self.time_9),
            self._to_axis_reading(self.time_10)
        ])

    def get_empty_array(self):
        return WasherDataSet([])

    def _to_axis_reading(self, time):
        return AxisReading(time, 1, 2, 3)

    def _test_sub_set(self, data_set, expected, start_time, end_time):
        sub_set = data_set.sub_set(start_time, end_time)
        self.assertListEqual(sub_set, expected)
