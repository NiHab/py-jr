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
        deinfs = self.de.deinflectWord(word, returnWord=True)
        hits = []
        addednodes = {}
        for deinf in deinfs:
            for res in self.di[deinf.deinflected]:
                if not (res in addednodes):
                    #Deep-copy so we can modify
                    copied = deepcopy(res)
                    
                    #Add conjugation info
                    conjugationode = ET.SubElement(copied, "app_infl")
                    conjugationode.text = deinf.type
                    
                    
                    #Add frequency
                    fnode = ET.SubElement(copied, "freq")                    
                    freq = -1        
                                
                    #Get the highest freq of all possible readings / writings for a node
                    for el in copied.findall("k_ele/keb") + copied.findall("r_ele/reb"):
                        nfreq = self.fr[el.text]
                        freq = nfreq if nfreq > freq else freq
                        
                    fnode.text = str(freq)
                    
                    
                    #Done
                    hits += [copied]
                    addednodes[res] = copied
                    
                else:
                    #Node we already added can be reached via different conjugation, add new conjugation info
                    cpy = addednodes[res]
                            
                    conjugationode = ET.SubElement(cpy, "app_infl")
                    conjugationode.text = deinf.type
            

        resultxmlnode = ET.Element('result')

        resultxmlnode.extend(hits)

        
        if asHtml:
            return (str(self.di.toHTML(resultxmlnode)), len(hits))
        else:
            return (resultxmlnode, len(hits))
