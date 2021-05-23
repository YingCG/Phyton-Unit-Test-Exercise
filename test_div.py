import unittest
from Methods import divisor

class TestDivisor(unittest.TestCase):
    def testDivisor(self):
        self.assertEqual (divisor (45), 6)

if __name__ == '__main__':
    unittest.main()
