import unittest
from python_assignment.src.assignment6.util import dt
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(dt(), "The difference in seconds is: 27885 seconds")  # add assertion here

if __name__ == '__main__':
    unittest.main()
