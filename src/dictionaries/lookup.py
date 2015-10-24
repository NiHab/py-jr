#@PydevCodeAnalysisIgnore
from lxml import etree as ET
import dictionaries.jmdict
import dictionaries.freq
import dictionaries.deinflecter
from librepo import Result
from copy import deepcopy

class Lookup(object):
    '''
    Combines and abstracts dict, freq and deinflecter
    '''


    def __init__(self):
        self.fr = dictionaries.freq.Freq()
        self.di = dictionaries.jmdict.JMDict()
        self.de = dictionaries.deinflecter.Deinflecter()
        
        self.de.load("../data/inflections")
        self.di.load("../data/JMdict_e", "../data/transform.xml")
        self.fr.load("../data/freq")
        
        
    def lookup(self, word, asHtml = False):
        deinf = self.de.deinflectWord(word, returnWord=True)
        hits = []
        for w in deinf:
            hits += [(w.deinflected, w.type, self.di[w.deinflected])]
            
        
        resultxmlnode = ET.Element('result')
        
        #print(hits)
        
        for (word, type, results) in hits:
            
            if results:
                rootnode = ET.SubElement(resultxmlnode, "group")
                
                if type:
                    conjugationode = ET.SubElement(rootnode, "app_infl")
                    conjugationode.text = type

                #Same node can appear in multiple groups (different inflections)
                #Deepcopy needed because one node can only have one parent
                #Also allows us to modify the nodes without changing the dictionary
                for node in results:
                    cnode = deepcopy(node)
                    rootnode.append(cnode)

                print (word, type, results)
        
        ET.dump(resultxmlnode)
        
        if asHtml:
            return str(self.di.toHTML(resultxmlnode))
        else:
            return resultxmlnode
