import unittest
from datetime import datetime

def detect_day_of_week(date: datetime):
    weekend_day_number = {
        0: 'weekend',
        6: 'weekend'
    }
    return weekend_day_number.get(date.weekday(), 'weekday')


class TestDayOfWeek(unittest.TestCase):
    def test_day_of_week(self):
        result = detect_day_of_week(date=datetime(2020, 5, 20))
        self.assertEqual(result, 'weekday')

    def test_day_of_weekend_sunday(self):
        result = detect_day_of_week(date=datetime(2020, 5, 25))
        self.assertEqual(result, 'weekend')

    def test_day_of_weekend_saturday(self):
        result = detect_day_of_week(date=datetime(2020, 5, 24))
        self.assertEqual(result, 'weekend')


if __name__ == "__main__":
    unittest.main()
