import unittest

from python_assignment.src.assignment2.util import highest
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(highest(), 80)  # add assertion here


if __name__ == '__main__':
    unittest.main()
