import unittest

from python_assignment.src.assignment8.util import float_format
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(float_format(1.1,1.2,1.3),"(array([2., 2., 2.]), array([1., 1., 1.]), array([1., 1., 1.]))" )  # add assertion here


if __name__ == '__main__':
    unittest.main()
