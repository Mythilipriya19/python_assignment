import unittest

from python_assignment.src.assignment15.util import count
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(count(),('Total letters', 30) )  # add assertion here


if __name__ == '__main__':
    unittest.main()
