'''
Created on Oct 23, 2015

@author: anon
'''
import unittest
from dictionaries.deinflecter import Deinflecter


class Test(unittest.TestCase):
    
    deinflecter = Deinflecter()


    def setUp(self):
        self.deinflecter.load("../data/inflections")

    def tearDown(self):
        pass


    def testDeinflection(self):
        testcases = [("寝ない", [self.deinflecter.Inflection(ending='ない', type='negative (plain)', deinflected='寝る')])] 
        
        testcases+=[("こない", [self.deinflecter.Inflection(ending='こない', type='negative (plain)', deinflected='くる'), 
                            self.deinflecter.Inflection(ending='ない', type='negative (plain)', deinflected='こる')])]
        
        testcases+=[("教えない", [self.deinflecter.Inflection(ending='えない', type='negative', deinflected='教う'), 
                              self.deinflecter.Inflection(ending='ない', type='negative (plain)', deinflected='教える')])]
        
        testcases+=[("食べたくなかった", [self.deinflecter.Inflection(ending='たくなかった', type='negative past desire', deinflected='食べる'), 
                                  self.deinflecter.Inflection(ending='くなかった', type='negative past', deinflected='食べたい'), 
                                  self.deinflecter.Inflection(ending='なかった', type='negative past (plain)', deinflected='食べたくる'), 
                                  self.deinflecter.Inflection(ending='かった', type='past', deinflected='食べたくない'), 
                                  self.deinflecter.Inflection(ending='った', type='past (plain)', deinflected='食べたくなかく'), 
                                  self.deinflecter.Inflection(ending='った', type='past (plain)', deinflected='食べたくなかつ'), 
                                  self.deinflecter.Inflection(ending='った', type='past (plain)', deinflected='食べたくなかる'), 
                                  self.deinflecter.Inflection(ending='った', type='past (plain)', deinflected='食べたくなかう'), 
                                  self.deinflecter.Inflection(ending='た', type='past (plain)', deinflected='食べたくなかっる')])]
        
        testcases+=[("言われます", [self.deinflecter.Inflection(ending='われます', type='passive (polite)', deinflected='言う'), 
                               self.deinflecter.Inflection(ending='れます', type='potential (polite)', deinflected='言わる'), 
                               self.deinflecter.Inflection(ending='れます', type='potential (short, polite)', deinflected='言わる'), 
                               self.deinflecter.Inflection(ending='ます', type='causative (short, plain)', deinflected='言われむ'), 
                               self.deinflecter.Inflection(ending='ます', type='polite', deinflected='言われる')])]
        
        for test in testcases:
            self.assertEqual(test[1], self.deinflecter.deinflectWord(test[0]))
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()