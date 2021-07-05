from datetime import timedelta
from deltat import parse_time, TimeFormatError
from nose.tools import raises


def assertEqual(a, b):
    if type(a) != type(b):
        raise AssertionError(
            "Assertion failed: Type mismatch %r (%s) != %r (%s)"
            % (a, type(a), b, type(b)))
    elif a != b:
        raise AssertionError(
            "Assertion failed: Value mismatch: %r (%s) != %r (%s)"
            % (a, type(a), b, type(b)))


def test_formats():
    for i in [
        ("1s", timedelta(seconds=1)),
        ("1.0s", timedelta(seconds=1)),
        ("1", timedelta(seconds=1)),
        ("1.0", timedelta(seconds=1)),
        ("1.5", timedelta(seconds=1.5)),
        (".5s", timedelta(seconds=0.5)),
        ("3600s", timedelta(seconds=3600)),

        ("2m", timedelta(minutes=2)),
        ("2.5m", timedelta(minutes=2.5)),
        ("2m30s", timedelta(minutes=2.5)),
        ("2m 30s", timedelta(minutes=2.5)),
        ("2m  30s", timedelta(minutes=2.5)),

        ("1h", timedelta(hours=1)),
        ("1h8m5.3s", timedelta(hours=1, minutes=8, seconds=5.3)),
        ("1h 8m 5.3s", timedelta(hours=1, minutes=8, seconds=5.3)),

        ("7d", timedelta(days=7)),
        ("6.5d", timedelta(days=6.5)),
        ("6d 12h", timedelta(days=6.5)),
        ("2w", timedelta(weeks=2)),

        ("3.1w 4.1d 5.9h 26.5m 53.5s", timedelta(weeks=3.1,
         days=4.1, hours=5.9, minutes=26.5, seconds=53.5)),
    ]:
        yield check_delta, *i


def check_delta(s, td):
    assert parse_time(s) == td


@raises(TimeFormatError)
def space_test():
    parse_time(" 1.0s ")


@raises(TimeFormatError)
def order_test():
    parse_time("1s 3m 5d")


@raises(ValueError)
def float_test():
    parse_time("1..3s")
