import csv
from datetime import datetime

from axis_reading import AxisReading


class WasherDataReader:
    def __init__(self):
        pass


    def read_data(self, path):
        return_list = []
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                return_list.append(self._parse_csv_data(', '.join(row)))
        return return_list

    def _parse_csv_data(self, line):
        DATE_LOCATION = 0
        X_LOCATION = 1
        Y_LOCATION = 2
        Z_LOCATION = 3
        fragments = line.split(', ')

        time = self._string_to_datetime(fragments[DATE_LOCATION])
        x = self._string_to_float(fragments[X_LOCATION])
        y = self._string_to_float(fragments[Y_LOCATION])
        z = self._string_to_float(fragments[Z_LOCATION])

        return AxisReading(
            time,
            x,
            y,
            z,
        )

    def _string_to_datetime(self, s):
        seconds = (float(s) - 25569) * 86400.0
        return datetime.utcfromtimestamp(seconds)
        # date_time_format = '%m/%d/%y %H:%S'
        # return datetime.strptime(s, date_time_format)

    def _string_to_float(self, s):
        return float(s)