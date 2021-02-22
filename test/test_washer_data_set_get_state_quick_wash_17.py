import unittest
from datetime import datetime

import washer_state as WASHER_STATE
from washer_data_reader import WasherDataReader
from washer_data_set import WasherDataSet
import test_constant as TEST_CONTSTANT

class TestWasherDataSetGetStateQuickWash17(unittest.TestCase):

    data_set = []

    def setUp(self):
        r = WasherDataReader()
        self.data_set = r.read_data(TEST_CONTSTANT.QUICK_WASH_17_DATA_PATH)

    def _run_check_current_state_of_washer(self, points, readings, expected_outcome):
        w = WasherDataSet(readings)
        for p in points:
            state = w.get_state(p)

            print('-------------')
            print(str(p))
            print(state.name)
            self.assertEqual(w.get_state(p), expected_outcome)

    def test_state_is_not_running(self):
        points = [
            datetime(year=2021, month=2, day=21, hour=12, minute=16),
            datetime(year=2021, month=2, day=21, hour=12, minute=18),
            datetime(year=2021, month=2, day=21, hour=12, minute=26),
            datetime(year=2021, month=2, day=21, hour=13, minute=2),
            datetime(year=2021, month=2, day=21, hour=13, minute=4),
        ]

        self._run_check_current_state_of_washer(points, self.data_set, WASHER_STATE.NOT_RUNNING)

    def test_state_is_washing(self):
        points = [
            datetime(year=2021, month=2, day=21, hour=12, minute=27),
            datetime(year=2021, month=2, day=21, hour=12, minute=30),
            datetime(year=2021, month=2, day=21, hour=12, minute=33),
            datetime(year=2021, month=2, day=21, hour=12, minute=37),
            datetime(year=2021, month=2, day=21, hour=12, minute=46),
            datetime(year=2021, month=2, day=21, hour=12, minute=49),
            datetime(year=2021, month=2, day=21, hour=12, minute=52),
        ]

        self._run_check_current_state_of_washer(points, self.data_set, WASHER_STATE.WASHING)

    def test_state_is_spinning(self):
        points = [
            datetime(year=2021, month=2, day=21, hour=12, minute=40),
            datetime(year=2021, month=2, day=21, hour=12, minute=54),
            datetime(year=2021, month=2, day=21, hour=12, minute=57),
            datetime(year=2021, month=2, day=21, hour=12, minute=58),
        ]

        self._run_check_current_state_of_washer(points, self.data_set, WASHER_STATE.SPINNING)


if __name__ == '__main__':
    unittest.main()