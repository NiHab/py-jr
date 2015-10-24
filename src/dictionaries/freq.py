'''
Created on Oct 23, 2015

@author: anon
'''

from collections import defaultdict
class Freq:
    """
    Acts as R/O dictionary containing the frequency of expressions
    Higher = More Common

    Key is the expression
    """

    __freqs = defaultdict(int)
    __raw = []

        
    def load(self, fp):
        print("Loading Frequencies")
        f = open(fp, encoding = 'utf-8')
        Freq.__raw = f.readlines()
        f.close()
        self.__parse()
        Freq.__raw = None

    def __parse(self):
        for line in Freq.__raw:
            expression = line.split()[0].strip()
            freq = line.split('/')[-2].strip()
            freq = int(freq.replace('#', ""))
            if expression in Freq.__freqs:
                if Freq.__freqs[expression] < freq:
                    Freq.__freqs[expression] = freq
            else:    
                Freq.__freqs[expression] = freq
    
    def __getitem__(self, key):
        return Freq.__freqs[key]