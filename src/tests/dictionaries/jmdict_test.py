'''
Created on Oct 24, 2015

@author: anon
'''
import unittest
from dictionaries.jmdict import JMDict

class Test(unittest.TestCase):
    jmdict = None

    def setUp(self):
        self.jmdict = JMDict()
        self.jmdict.load('../data/JMdict_e', "../data/transform.xml");
        pass


    def tearDown(self):
        pass


    def testDict(self):
        self.assertEqual([], self.jmdict['wafgawgwagwe'])
        self.assertNotEqual([], self.jmdict['くる'])
        self.assertNotEqual([], self.jmdict['來る'])
        self.assertNotEqual([], self.jmdict['行って来る'])
        self.assertNotEqual([], self.jmdict['起きる'])
        self.assertNotEqual([], self.jmdict['死ぬ'])
        self.assertNotEqual([], self.jmdict['高い'])
        self.assertEqual(set(self.jmdict['くる']), set(self.jmdict['くる']))
        self.assertTrue(set(self.jmdict['來る']).issubset(set(self.jmdict['くる'])))

        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()