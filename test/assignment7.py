import unittest

from python_assignment.src.assignment7.util import avg
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(avg(), 85.75)  # add assertion here


if __name__ == '__main__':
    unittest.main()
