#@PydevCodeAnalysisIgnore
from lxml import etree as ET
from collections import defaultdict
from operator import __getitem__
import gc


#===============================================================================
# PROTOTYPE
# ENTIRE DICT IS STORED IN MEMORY
# EXPECT FIREFOX-LEVELS OF MEMORY USAGE
#===============================================================================



class JMDict:

    __xmlroot = None
    __hashtbl = defaultdict(list)
    __transform = None
        
    def __getitem__(self, key):
        return JMDict.__hashtbl[key]
        
    
    def load(self, xmlfp, xslfp):
        print('loading xml dict')
        JMDict.__xmlroot = ET.parse(xmlfp).getroot()
        

        #Way faster lookuptimes by using a hashtable to point to xml nodes
        #Keys are Kanjified expressions and readings
        print('creating indeces')        
        for entry in JMDict.__xmlroot:
            keys = []
            #Add readings as well as kanji-fied readings as key
            keys += [keb.text for k_ele in entry.findall('k_ele') for keb in k_ele.findall('keb')]
            keys += [reb.text for r_ele in entry.findall('r_ele') for reb in r_ele.findall('reb')]
        
            for key in keys:
                    JMDict.__hashtbl[key] += [entry]
                    
        print('loading xsl')
        JMDict.__transform = ET.XSLT(ET.parse(xslfp))
        
        

    #Refactor into own class if this takes over too many responsibilities
    def toHTML(self, entry):
        return JMDict.__transform(entry)