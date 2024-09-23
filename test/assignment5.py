import unittest

from python_assignment.src.assignment5.util import datetime
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(datetime("19 05 2002"), "Sunday")  # add assertion here


if __name__ == '__main__':
    unittest.main()
