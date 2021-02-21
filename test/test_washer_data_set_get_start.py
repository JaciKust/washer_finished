import unittest
from datetime import datetime, timedelta

from washer_data_reader import WasherDataReader
import test_constant as TEST_CONTSTANT

from washer_data_set import WasherDataSet
# These tests were created to make sure that the testing for data points doesn't get worse with an approvement.

class TestWasherDataSetGetStart(unittest.TestCase):

    normal_13_full_set = []
    normal_15_full_set = []
    bedding_14_full_set = []
    darks_16_full_set = []

    def setUp(self):
        r = WasherDataReader()
        self.normal_13_full_set = WasherDataSet(r.read_data(TEST_CONTSTANT.NORMAL_13_DATA_PATH))
        self.normal_15_full_set = WasherDataSet(r.read_data(TEST_CONTSTANT.NORMAL_15_DATA_PATH))
        self.bedding_14_full_set = WasherDataSet(r.read_data(TEST_CONTSTANT.BEDDING_14_DATA_PATH))
        self.darks_16_full_set = WasherDataSet(r.read_data(TEST_CONTSTANT.DARKS_16_DATA_PATH))

    def test_get_start_not_before_start_normal_13(self):
        acceptable_start_time = datetime(year=2021, month=2, day=19, hour=16, minute=2)
        dataset = self.normal_13_full_set
        self._test_start_not_before_start(dataset, acceptable_start_time)

    def test_get_start_not_before_start_normal_15(self):
        acceptable_start_time = datetime(year=2021, month=2, day=19, hour=18, minute=28)
        dataset = self.normal_15_full_set
        self._test_start_not_before_start(dataset, acceptable_start_time)

    def test_get_start_not_before_start_bedding_14(self):
        acceptable_start_time = datetime(year=2021, month=2, day=19, hour=17, minute=20)
        dataset = self.bedding_14_full_set
        self._test_start_not_before_start(dataset, acceptable_start_time)

    def test_get_start_not_before_start_darks_16(self):
        acceptable_start_time = datetime(year=2021, month=2, day=19, hour=19, minute=47)
        dataset = self.darks_16_full_set
        self._test_start_not_before_start(dataset, acceptable_start_time)

    def _test_start_not_before_start(self, washer_dataset, target_after_point):
        max_start_time = target_after_point + timedelta(minutes=2)
        start_time = washer_dataset.get_washer_start()
        print(str(start_time))
        self.assertGreaterEqual(start_time, target_after_point)
        self.assertGreaterEqual(max_start_time, start_time)


if __name__ == '__main__':
    unittest.main()
