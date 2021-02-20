import unittest
from datetime import datetime

import washer_state as WASHER_STATE
from washer_data_reader import WasherDataReader

import washer_state_checker
from washer_state_checker import WasherStateChecker


class TestNormal13(unittest.TestCase):

    data_set = []

    def setUp(self):
        r = WasherDataReader()
        self.data_set = r.read_data('washer_test_data/13 - Normal.csv')

    def _run(self, points, readings, expected_outcome):
        w = WasherStateChecker(readings)
        for p in points:
            state = w.get_state(p)

            print('-------------')
            print(str(p))
            print(state.name)
            self.assertEqual(w.get_state(p), expected_outcome)

    def test_hand_picked_not_running_normal_13(self):
        points = [
            datetime(year=2021, month=2, day=19, hour=16, minute=1, second=2),
            datetime(year=2021, month=2, day=19, hour=15, minute=55, second=41),
            datetime(year=2021, month=2, day=19, hour=15, minute=50, second=7)
        ]

        self._run(points, self.data_set, WASHER_STATE.NOT_RUNNING)

    def test_hand_picked_spinning_normal_13(self):
        points = [
            datetime(year=2021, month=2, day=19, hour=16, minute=32, second=20),
            datetime(year=2021, month=2, day=19, hour=16, minute=34, second=36),
            datetime(year=2021, month=2, day=19, hour=16, minute=35, second=28),
            datetime(year=2021, month=2, day=19, hour=16, minute=44, second=4),
            datetime(year=2021, month=2, day=19, hour=16, minute=49, second=23),
            datetime(year=2021, month=2, day=19, hour=16, minute=54, second=35),
        ]

        self._run(points, self.data_set, WASHER_STATE.SPINNING)

    def test_hand_picked_washing_normal_13_(self):
        points = [
            datetime(year=2021, month=2, day=19, hour=16, minute=5, second=1),
            datetime(year=2021, month=2, day=19, hour=16, minute=11, second=9),
            datetime(year=2021, month=2, day=19, hour=16, minute=18, second=36),
            datetime(year=2021, month=2, day=19, hour=16, minute=23, second=37),
            datetime(year=2021, month=2, day=19, hour=16, minute=29, second=24),

        ]

        self._run(points, self.data_set, WASHER_STATE.WASHING)

if __name__ == '__main__':
    unittest.main()
