import unittest


def count_odd(array_of_integer):
    result = 0
    for integer in array_of_integer:
        result += integer % 2
    return result


class TestCountOdd(unittest.TestCase):

    def test_count_odd(self):
        arrayOfIntegers = [1, 4, 5, 9, 0, -1, 5]
        result = count_odd(arrayOfIntegers)

        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
