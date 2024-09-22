import unittest

from python_assignment.src.assignment1.util import average
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(average(), 20.0)  # add assertion here


if __name__ == '__main__':
    unittest.main()
