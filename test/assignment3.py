import unittest
from python_assignment.src.assignment3.util import mutation

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(mutation(), "Aplle")  # add assertion here


if __name__ == '__main__':
    unittest.main()
