import unittest
from datetime import datetime

import washer_state as WASHER_STATE
from washer_data_reader import WasherDataReader

import washer_state_checker
from washer_state_checker import WasherStateChecker


class TestBedding14(unittest.TestCase):

    data_set = []

    def setUp(self):
        r = WasherDataReader()
        self.data_set = r.read_data('washer_test_data/14 - Bedding.csv')

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
            datetime(year=2021, month=2, day=19, hour=18, minute=15),
            datetime(year=2021, month=2, day=19, hour=18, minute=19),
            datetime(year=2021, month=2, day=19, hour=17, minute=20),
        ]

        self._run(points, self.data_set, WASHER_STATE.NOT_RUNNING)

    def test_hand_picked_spinning_normal_13(self):
        points = [
            datetime(year=2021, month=2, day=19, hour=17, minute=50),
            datetime(year=2021, month=2, day=19, hour=17, minute=52),
            datetime(year=2021, month=2, day=19, hour=18, minute=1),
            datetime(year=2021, month=2, day=19, hour=18, minute=5),
            datetime(year=2021, month=2, day=19, hour=18, minute=11),
            datetime(year=2021, month=2, day=19, hour=18, minute=12),
        ]

        self._run(points, self.data_set, WASHER_STATE.SPINNING)

    def test_hand_picked_washing_normal_13_(self):
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

        self._run(points, self.data_set, WASHER_STATE.WASHING)