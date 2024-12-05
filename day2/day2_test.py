import unittest
from day2 import findnumcount

class TestFindNumCount(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(findnumcount(42,[]), 0)

    def test_one(self):
        self.assertEqual(findnumcount(42,[42]),1)
    
    def test_mult(self):
        self.assertEqual(findnumcount(42,[2,3,42]),1)

    def test_mult(self):
        self.assertEqual(findnumcount(42,[2,3,42,42,45,67]),2)


if __name__ == "__main__":
    findnumcount(43,[])
    unittest.main()