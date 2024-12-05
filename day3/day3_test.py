import unittest
from day3 import getmuls, getpairs, getfuncs

class TestGetMuls(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(getmuls("xyz"),[])

    def test_one(self):
        self.assertEqual(getmuls("mul(234,456)"),["mul(234,456)"])

    def test_many(self):
        s = ";(,)<mul(595,110)~ #(select()-?who():mul(732,729)+/;%@mul(924,700) }&when()"
        self.assertEqual(getmuls(s),['mul(595,110)','mul(732,729)','mul(924,700)'])

class TestGetPairs(unittest.TestCase):
    def test_empty(self):
        self.assertRaises(IndexError, getpairs, "")

    def test_goodpair(self):
        self.assertEqual(getpairs("mul(111,222"),[111, 222])

class TestGetFuncs(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(getfuncs("mul(111,222"), None)

    def test_do(self):
        self.assertEqual(getfuncs("xdo()mul(111,222)"),"do()mul(111,222)")

if __name__ == "__main__":
    unittest.main()