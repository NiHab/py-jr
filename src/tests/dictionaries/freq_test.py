'''
Created on Oct 23, 2015

@author: anon
'''
import unittest
from dictionaries.freq import Freq

class Test(unittest.TestCase):

    freq = Freq()

    def testFreq(self):
        self.freq.load("../data/freq")
        self.assertEqual(0, self.freq["×"])
        self.assertEqual(10, self.freq["火山砕屑物"])
        self.assertEqual(688, self.freq["夜明かし"])
        self.assertEqual(293864, self.freq["多数"])
        self.assertEqual(17742, self.freq["と言ってもいい"])
        self.assertEqual(5100, self.freq["踏み絵"])
        self.assertEqual(958826, self.freq["来る"])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()