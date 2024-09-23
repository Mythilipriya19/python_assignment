import unittest

from python_assignment.src.assignment9.util import split_remove_duplicates
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(split_remove_duplicates("appllleee",2),['ap', 'lp', 'l', 'e', 'e'])  # add assertion here


if __name__ == '__main__':
    unittest.main()
