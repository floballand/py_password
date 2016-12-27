#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# --------
# Name : PASSERATOR.py
# Objectif : Password Generator
# --------
# version : 0.1
# Author : INOPE
# 18/12/2016
# fballand.inope@gmail.com
# --------
# version : 0.2
# Author : INOPE
# 26/12/2016
# fballand.inope@gmail.com
# - use XML to translate
# - add detect langue
# - minima python 3.2
# --------

# --------
# Imports
# --------
import string
import sys,io,random
import locale
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import ParseError

"""
Password Generate
"""
# --------
# definition
# --------
def main():
    """
    Args : s.o
    Returns : s.o
    """
    dicoLangue={}
    dicoLangue=langParseXML()
    options=menuOptions(dicoLangue)
    table=tablecaractere(options)
    generator(table,int(options.split(' ')[6])) #this item [6] is a size password
    input(dicoLangue.get('13'))
    print ('END')
    exit(0)

# --------
# langue detection
# --------
def langParseXML():
    """
    Args : s.o
    Returns : translateTable : langues dictionaries 
    """
    lang=locale.getdefaultlocale()#langue of system
    if (lang[0:1]=="fr"):
        lang="fr"
    elif (lang[0:1]=="es"):
        lang="es"
    else:
        lang="en"
    #print (lang)

    """
    read/PARSER file translate XML
    """
    translateTable={}
    rank=0
    xmlET=ElementTree()
    try:
        treeXML=xmlET.parse('langue.xml')
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

# --------
# menu
# --------
def menuOptions(langueDico):
    """
    Display a menu on the terminal. The user can select a generate mode password
    Args : s.o
    Returns : One list of user options  [ononon9]. the last option is a password size
    """
    listeChoixYes=['o','oui','y','yes']
    listeChoixNo=['non','n','no']

    print (langueDico.get('1'))
    print (langueDico.get('2'))
    value=input(langueDico.get('3'))
    if (value in listeChoixYes):
        valueReturn=['o','o','o','o','o','o','9'] #All at YES/OUI ;default value to this mode
    elif(value in listeChoixNo):
        valueReturn=[]
        
        '[0]---Use numbers------------------------'
        value=input (langueDico.get('4'))
        if (value in listeChoixYes):
            valueReturn.append(value)
        else:
            valueReturn.append('n')
            
        '[1]---Use Uppercase-----------------------'
        value=input (langueDico.get('5'))
        if (value in listeChoixYes):
            valueReturn.append(value)
        else:
            valueReturn.append('n')
            
        '[2]---Use lowercase---------------------- '
        """
        upper&lower is impossible. if uppercase is disabled,
        then lowercase foce the enable.
        """
        if(valueReturn[1]=="o"): 
            value=input (langueDico.get('6'))
            if (value in listeChoixYes):
                valueReturn.append(value)
            else:
                valueReturn.append('n')
        else:
            print(langueDico.get('14')) #force using lowercase
            valueReturn.append('o')
            
        '[3]---Use accent------------------ '
        value=input (langueDico.get('7'))
        if (value in listeChoixYes):
            valueReturn.append(value)
        else:
            valueReturn.append('n')
            
        '[4]----Use char specific------------------ '
        value=input (langueDico.get('8'))
        if (value in listeChoixYes):
            valueReturn.append(value)
        else:
            valueReturn.append('n')
            
        '[5]---Use similar char---------------------- '
        value=input (langueDico.get('9'))
        if (value in listeChoixYes):
            valueReturn.append(value)
        else:
            valueReturn.append('n')
            
        '[6]----Size password--------------------    '
        value=input(langueDico.get('10'))
        if(value==""):
           value='9'#default size 9 char            
        if (int(value)>0):
            valueReturn.append(value)#custom size
        else:
            valueReturn.append('9')#default size 9 char    
    else:
        print (langueDico.get('12'))
        exit(0)
    return ' '.join(valueReturn)#convert a list on string(tupple)

def tablecaractere(liste):
    """
    One table of caractere is create with a user choice in a menu
    Args : options liste
    Returns : a table of caractere authorized for the a traitment
    """

    if(liste[0]=='o'):
       number=string.digits
    else:
       number=''

    if(liste[1]=='o'):
       letterMinus=string.ascii_lowercase
    else:
       letterMinus=''

    if(liste[2]=='o'):
       letterMaxi=string.ascii_uppercase
    else:
       letterMaxi=''

    if(liste[3]=='o'):
       letterAccent='àâäåçéèêëîïôöùûü'
    else:
       letterAccent=''

    if(liste[4]=='o'):
       caractSpe='!@#$%^&*(){}[],.;<>?|'
    else:
       caractSpe=''

    if(liste[5]=='n'):
        caractASup=['O0l1I'] #list of similar characters graphics
        table=number+letterMinus+letterMaxi+caractSpe
        for i in range(0,len(caractASup)):
                       table=table.replace(caractASup[i],'')
        return table
    else:
       return number+letterMinus+letterMaxi+caractSpe


def generator(charAutori,size):
    """
    generate password
    Args : table of caractere, password size
    Returns : s.o
    """
    choice = random.SystemRandom().choice
    print('Password :')
    print (''.join(random.choice(charAutori) for i in range(size)))

if __name__ == '__main__':
    main()
