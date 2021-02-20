import unittest
from datetime import datetime

import washer_state as WASHER_STATE
from washer_data_reader import WasherDataReader

import washer_state_checker
from washer_state_checker import WasherStateChecker


class TestNormal15(unittest.TestCase):

    data_set = []

    def setUp(self):
        r = WasherDataReader()
        self.data_set = r.read_data('washer_test_data/15 - Normal.csv')

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
            datetime(year=2021, month=2, day=19, hour=18, minute=24),
            datetime(year=2021, month=2, day=19, hour=18, minute=27),
            datetime(year=2021, month=2, day=19, hour=19, minute=27),
            datetime(year=2021, month=2, day=19, hour=19, minute=31),
            datetime(year=2021, month=2, day=19, hour=19, minute=37),
            datetime(year=2021, month=2, day=19, hour=19, minute=43),
        ]

        self._run(points, self.data_set, WASHER_STATE.NOT_RUNNING)

    def test_hand_picked_spinning_normal_13(self):
        points = [
            datetime(year=2021, month=2, day=19, hour=19, minute=2),
            datetime(year=2021, month=2, day=19, hour=19, minute=11),
            datetime(year=2021, month=2, day=19, hour=19, minute=15),
            datetime(year=2021, month=2, day=19, hour=19, minute=20),
            datetime(year=2021, month=2, day=19, hour=19, minute=22),
        ]

        self._run(points, self.data_set, WASHER_STATE.SPINNING)

    def test_hand_picked_washing_normal_13_(self):
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

        self._run(points, self.data_set, WASHER_STATE.WASHING)