import unittest
from python_assignment.src.assignment13.util import  min_max

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual( min_max(), 2)  # add assertion here


if __name__ == '__main__':
    unittest.main()
