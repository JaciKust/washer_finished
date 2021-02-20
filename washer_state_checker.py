from datetime import timedelta

import washer_state as WASHER_STATE


TIME_SPAN_MINUTES = 3
WASHING_THRESHOLD = 1
SPINNING_THRESHOLD = 10

class WasherStateChecker:

    def __init__(self, dataset):
        self.dataset = dataset

    def _get_data_for_time(self, time):
        behind_point = time - timedelta(minutes=TIME_SPAN_MINUTES)
        return list(filter(lambda x: behind_point < x.time < time, self.dataset))

    def get_state(self, at_time):
        min_x = min(list(map(lambda s: s.x, self._get_data_for_time(at_time))))
        max_x = max(list(map(lambda s: s.x, self._get_data_for_time(at_time))))
        range_x = abs(min_x - max_x)

        min_y = min(list(map(lambda s: s.y, self._get_data_for_time(at_time))))
        max_y = max(list(map(lambda s: s.y, self._get_data_for_time(at_time))))
        range_y = abs(max_y - min_y)

        min_z = min(list(map(lambda s: s.z, self._get_data_for_time(at_time))))
        max_z = max(list(map(lambda s: s.z, self._get_data_for_time(at_time))))
        range_z = abs(min_z - max_z)

        # print('X: {0} >< {1} || {2} '.format(min_x, max_x, range_x))
        # print('Y: {0} >< {1} || {2} '.format(min_y, max_y, range_y))
        # print('Z: {0} >< {1} || {2} '.format(min_z, max_z, range_z))

        # Want the one with highest range of acceleration. Doesn't matter
        # if more than one is varying. All that matters is at least one is.
        largest_range = max([range_x, range_y, range_z])
        print('{0}'.format(largest_range))

        if largest_range >= SPINNING_THRESHOLD:
            return WASHER_STATE.SPINNING

        if largest_range >= WASHING_THRESHOLD:
            return WASHER_STATE.WASHING

        return WASHER_STATE.NOT_RUNNING
