from datetime import timedelta

import washer_state as WASHER_STATE


TIME_SPAN_MINUTES = 3
WASHING_THRESHOLD = 1
SPINNING_THRESHOLD = 10

class WasherDataSet:

    def __init__(self, dataset):
        self.dataset = dataset

    def _get_data_for_time(self, end_time):
        start_time = end_time - timedelta(minutes=TIME_SPAN_MINUTES)
        return self._get_data_for_time_span(start_time, end_time)

    def _get_data_for_time_span(self, start_time, end_time):
        return list(filter(lambda x: start_time < x.time < end_time, self.dataset))

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
        # print('{0}'.format(largest_range))

        if largest_range >= SPINNING_THRESHOLD:
            return WASHER_STATE.SPINNING

        if largest_range >= WASHING_THRESHOLD:
            return WASHER_STATE.WASHING

        return WASHER_STATE.NOT_RUNNING

    def has_finished(self):
        return False

    def has_started(self):
        return self.get_washer_start() is not None

    def has_complete_run(self):
        return False

    def get_data_start(self):
        return self.dataset[0].time

    def get_data_end(self):
        return self.dataset[len(self.dataset) -1].time

    def get_washer_start(self):
        for e in self.dataset[1:]:
            if self.get_state(e.time).is_running():
                return e.time

        return None
