import unittest
from python_assignment.src.assignment11.util import validation

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(validation(),['mythili@gmail.com'] )  # add assertion here


if __name__ == '__main__':
    unittest.main()
