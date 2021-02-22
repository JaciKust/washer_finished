import unittest
from datetime import datetime

import washer_state as WASHER_STATE
from washer_data_reader import WasherDataReader
import test_constant as TEST_CONTSTANT

from washer_data_set import WasherDataSet


class TestWasherDataSetGetStateNormal15(unittest.TestCase):

    data_set = []

    def setUp(self):
        r = WasherDataReader()
        self.data_set = r.read_data(TEST_CONTSTANT.NORMAL_15_DATA_PATH)

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
            datetime(year=2021, month=2, day=19, hour=18, minute=24),
            datetime(year=2021, month=2, day=19, hour=18, minute=27),
            datetime(year=2021, month=2, day=19, hour=19, minute=27),
            datetime(year=2021, month=2, day=19, hour=19, minute=31),
            datetime(year=2021, month=2, day=19, hour=19, minute=37),
            datetime(year=2021, month=2, day=19, hour=19, minute=43),
        ]

        self._run_check_current_state_of_washer(points, self.data_set, WASHER_STATE.NOT_RUNNING)

    def test_state_is_washing(self):
        points = [
            datetime(year=2021, month=2, day=19, hour=18, minute=32),
            datetime(year=2021, month=2, day=19, hour=18, minute=36),
            datetime(year=2021, month=2, day=19, hour=18, minute=41),
            datetime(year=2021, month=2, day=19, hour=18, minute=45),
            datetime(year=2021, month=2, day=19, hour=18, minute=49),
            datetime(year=2021, month=2, day=19, hour=18, minute=55),
            datetime(year=2021, month=2, day=19, hour=18, minute=58),
            datetime(year=2021, month=2, day=19, hour=19, minute=7),
            datetime(year=2021, month=2, day=19, hour=19, minute=8),
        ]

        self._run_check_current_state_of_washer(points, self.data_set, WASHER_STATE.WASHING)

    def test_state_is_spinning(self):
        points = [
            datetime(year=2021, month=2, day=19, hour=19, minute=2),
            datetime(year=2021, month=2, day=19, hour=19, minute=11),
            datetime(year=2021, month=2, day=19, hour=19, minute=15),
            datetime(year=2021, month=2, day=19, hour=19, minute=20),
            datetime(year=2021, month=2, day=19, hour=19, minute=22),
        ]

        self._run_check_current_state_of_washer(points, self.data_set, WASHER_STATE.SPINNING)


if __name__ == '__main__':
    unittest.main()