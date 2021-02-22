import unittest
from datetime import datetime

import washer_state as WASHER_STATE
from washer_data_reader import WasherDataReader
from washer_data_set import WasherDataSet
import test_constant as TEST_CONTSTANT

class TestWasherDataSetGetStateBedding14(unittest.TestCase):

    data_set = []

    def setUp(self):
        r = WasherDataReader()
        self.data_set = r.read_data(TEST_CONTSTANT.BEDDING_14_DATA_PATH)

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
            datetime(year=2021, month=2, day=19, hour=18, minute=15),
            datetime(year=2021, month=2, day=19, hour=18, minute=19),
            datetime(year=2021, month=2, day=19, hour=17, minute=20),
        ]

        self._run_check_current_state_of_washer(points, self.data_set, WASHER_STATE.NOT_RUNNING)

    def test_state_is_washing(self):
        points = [
            datetime(year=2021, month=2, day=19, hour=17, minute=23),
            datetime(year=2021, month=2, day=19, hour=17, minute=30),
            datetime(year=2021, month=2, day=19, hour=17, minute=34),
            datetime(year=2021, month=2, day=19, hour=17, minute=35),
            datetime(year=2021, month=2, day=19, hour=17, minute=43),
            datetime(year=2021, month=2, day=19, hour=17, minute=45),
            datetime(year=2021, month=2, day=19, hour=17, minute=47),
            datetime(year=2021, month=2, day=19, hour=17, minute=57),
        ]

        self._run_check_current_state_of_washer(points, self.data_set, WASHER_STATE.WASHING)

    def test_state_is_spinning(self):
        points = [
            datetime(year=2021, month=2, day=19, hour=17, minute=50),
            datetime(year=2021, month=2, day=19, hour=17, minute=52),
            datetime(year=2021, month=2, day=19, hour=18, minute=1),
            datetime(year=2021, month=2, day=19, hour=18, minute=5),
            datetime(year=2021, month=2, day=19, hour=18, minute=11),
            datetime(year=2021, month=2, day=19, hour=18, minute=12),
        ]

        self._run_check_current_state_of_washer(points, self.data_set, WASHER_STATE.SPINNING)


if __name__ == '__main__':
    unittest.main()