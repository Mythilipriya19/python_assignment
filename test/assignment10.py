import unittest

from python_assignment.src.assignment10.util import cnd
class MyTestCase(unittest.TestCase):
    def test_something(self):
        lis_value=["apple","apple","banana"]

        self.assertEqual(cnd(lis_value), [2,1])  # add assertion here


if __name__ == '__main__':
    unittest.main()
