#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
 @name : PASSERATOR.py
 @brief : Password Generator
 --------
 @author : INOPE <fballand.inope@gmail.com>
 @license : GPL3
"""


# --------
# Imports
# --------
import string
import sys,io,random
import locale
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import ParseError

# --------
# langue detection
# --------
def langParseXML():
    """
    @brief : read a XML file to load a translate message
    @brief : A without XML make a exit
    @param : s.o
    @return : translateTable : langues dictionaries 
    """
    lang=locale.getdefaultlocale()#langue from system
    if (lang[0:1]=="fr"):
        lang="fr"
    elif (lang[0:1]=="es"):
        lang="es"
    else:
        lang="en"
        
    """
    read/PARSER file translate XML
    """
    translateTable={}
    rank=0
    xmlET=ElementTree()
    try:
        treeXML=xmlET.parse('../langue.xml')
        for childRank in treeXML.iter('rank'):
            rank=childRank.get('rank-id')
            for child in childRank.iter('langue'):
                if(child.get('select-lang')==lang):
                    translateTable[rank]=child.find('label').text                
        #for key,value in translateTable.items():
        #   print(key,value)
    except Exception as msgError:
        print(msgError)
        exit()
    
    return translateTable
