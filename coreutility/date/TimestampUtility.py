import time
from datetime import datetime, timezone


class TimestampUtility:

    @staticmethod
    def get_nanoseconds_time():
        return time.clock_gettime_ns(time.CLOCK_REALTIME)

    @staticmethod
    def to_datetime_string(nanoseconds):
        conventional_time = nanoseconds // 1000000000
        nano_intervals = nanoseconds % 1000000000
        conventional_datetime = datetime.utcfromtimestamp(conventional_time)
        return conventional_datetime.strftime('%Y-%m-%dT%H:%M:%S.%f').replace('000000', str(nano_intervals) + 'Z')

    @staticmethod
    def as_datetime_from_nanoseconds(nanoseconds):
        conventional_time = nanoseconds // 1000000000
        nano_intervals = nanoseconds % 1000000000
        microsecond_intervals = nano_intervals // 1000
        # good enough @ microsecond (does not yet handle nanosecond interval)
        # see RFC3339 Nano timestamp
        conventional_datetime = datetime.utcfromtimestamp(conventional_time).replace(microsecond=microsecond_intervals)
        return conventional_datetime

    @staticmethod
    def as_nanoseconds_from_datetime(datetime_value):
        utc_timestamp = datetime_value.replace(tzinfo=timezone.utc).timestamp()
        return int(utc_timestamp * 1000000)
