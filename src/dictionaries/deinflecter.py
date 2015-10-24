'''
Created on Oct 23, 2015

@author: anon
'''

import collections

class Deinflecter:
    """
    Replaces verb / adv / adj endings with the dictionary form
    """

    #[(inflection, name, dictionary form), ...]
    inflection = []
    
    #[index] = name
    __inflection_index = {}
    
    Inflection = collections.namedtuple("Inflection", "ending type deinflected")

    def rreplace(self, s, old, new, occurrence):
        li = s.rsplit(old, occurrence)
        return new.join(li)

    
    def load(self, fp):
        print("Loading Deinflections")
        f = open(fp, encoding = 'euc-jp')
        built_index = False
        dictForm = ""
        
        for line in f.readlines():
            if line.startswith("#") or line.startswith("\n"):
                continue
                
            if not built_index and line.startswith('$'):
                built_index = True
                continue
            
            if not built_index:
                Deinflecter.__inflection_index[line.split("  ")[0]] = line.split("  ")[1].strip()
                continue
                            
            if built_index and line.startswith('$'):
                dictForm = line[1:].strip()
                continue
            else:
                index = line.split("  ")[0]
                ending = line.split("  ")[1].strip()
                Deinflecter.inflection += [(ending, Deinflecter.__inflection_index[index], dictForm)]

            
                
            
        f.close()

        

    def deinflectWord(self, word, returnWord = False):
        """
        Returns all possible deinflections for all possible endings of an expression
        if returnWord set, First element is the unmodified word in .deinflected
        """
        res = []
        if returnWord:
            res += [Deinflecter.Inflection(ending=None, type=None, deinflected=word)]
        for n in range(0, len(word)):
            for inf in Deinflecter.inflection:
                if inf[0] == word[n:]:
                    dictform = self.rreplace(word, word[n:], inf[2], 1)
                    
                    res += [Deinflecter.Inflection(ending=word[n:], type=inf[1], deinflected=dictform)]

        return res
        