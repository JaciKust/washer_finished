import unittest
from datetime import datetime

import washer_state as WASHER_STATE
from washer_data_reader import WasherDataReader
import test_constant as TEST_CONTSTANT

from washer_data_set import WasherDataSet


class TestWasherDataSetGetStateDarks16(unittest.TestCase):

    data_set = []

    def setUp(self):
        r = WasherDataReader()
        self.data_set = r.read_data(TEST_CONTSTANT.DARKS_16_DATA_PATH)

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
            datetime(year=2021, month=2, day=19, hour=19, minute=48),
            datetime(year=2021, month=2, day=19, hour=20, minute=55),
            datetime(year=2021, month=2, day=19, hour=21, minute=4),
        ]

        self._run_check_current_state_of_washer(points, self.data_set, WASHER_STATE.NOT_RUNNING)

    def test_state_is_washing(self):
        points = [
            datetime(year=2021, month=2, day=19, hour=19, minute=54),
            datetime(year=2021, month=2, day=19, hour=20, minute=1),
            datetime(year=2021, month=2, day=19, hour=20, minute=6),
            datetime(year=2021, month=2, day=19, hour=20, minute=12),
            datetime(year=2021, month=2, day=19, hour=20, minute=16),
            datetime(year=2021, month=2, day=19, hour=20, minute=20),
            datetime(year=2021, month=2, day=19, hour=20, minute=23),
            datetime(year=2021, month=2, day=19, hour=20, minute=25),
            datetime(year=2021, month=2, day=19, hour=20, minute=27),
            datetime(year=2021, month=2, day=19, hour=20, minute=35),
            datetime(year=2021, month=2, day=19, hour=20, minute=37),
            datetime(year=2021, month=2, day=19, hour=20, minute=40),
            datetime(year=2021, month=2, day=19, hour=20, minute=42),
        ]

        self._run_check_current_state_of_washer(points, self.data_set, WASHER_STATE.WASHING)

    def test_state_is_spinning(self):
        points = [
            datetime(year=2021, month=2, day=19, hour=20, minute=29),
            datetime(year=2021, month=2, day=19, hour=20, minute=30),
            datetime(year=2021, month=2, day=19, hour=20, minute=32),
            datetime(year=2021, month=2, day=19, hour=20, minute=47),
            datetime(year=2021, month=2, day=19, hour=20, minute=48),
            datetime(year=2021, month=2, day=19, hour=20, minute=50),
        ]

        self._run_check_current_state_of_washer(points, self.data_set, WASHER_STATE.SPINNING)


if __name__ == '__main__':
    unittest.main()
