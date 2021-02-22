import unittest
from datetime import datetime

import washer_state as WASHER_STATE
from washer_data_reader import WasherDataReader
from washer_data_set import WasherDataSet
import test_constant as TEST_CONTSTANT

class TestWasherDataSetGetStateHandWash(unittest.TestCase):

    data_set = []

    def setUp(self):
        r = WasherDataReader()
        self.data_set = r.read_data(TEST_CONTSTANT.HAND_WASH_18_DATA_PATH)

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
            datetime(year=2021, month=2, day=21, hour=13, minute=6),
            datetime(year=2021, month=2, day=21, hour=13, minute=10),
            datetime(year=2021, month=2, day=21, hour=13, minute=13),
            datetime(year=2021, month=2, day=21, hour=13, minute=15),
            datetime(year=2021, month=2, day=21, hour=13, minute=53),
            datetime(year=2021, month=2, day=21, hour=13, minute=57),

        ]

        self._run_check_current_state_of_washer(points, self.data_set, WASHER_STATE.NOT_RUNNING)

    def test_state_is_washing(self):
        points = [
            datetime(year=2021, month=2, day=21, hour=13, minute=23),
            datetime(year=2021, month=2, day=21, hour=13, minute=32),
            datetime(year=2021, month=2, day=21, hour=13, minute=39),
            datetime(year=2021, month=2, day=21, hour=13, minute=45),
            datetime(year=2021, month=2, day=21, hour=13, minute=48),
        ]

        self._run_check_current_state_of_washer(points, self.data_set, WASHER_STATE.WASHING)

    def test_state_is_spinning(self):
        points = [
            # None here. This cycle doesn't go super heavy on a spin cycle. Therefore it never reaches
            # what I classify as a spin. It does spin and the data shows that there just isn't too
            # much too it and it doesn't really matter at this point anyways.
        ]

        self._run_check_current_state_of_washer(points, self.data_set, WASHER_STATE.SPINNING)


if __name__ == '__main__':
    unittest.main()