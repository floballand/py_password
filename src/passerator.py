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
from parserXML import langParseXML
from generation import tablecaractere,generator
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import ParseError


"""
Password Generate
"""
# --------
# definition
# --------
def main():
    """ Main function
    @brief : read a file XML lang
    @brief : display menu
    @brief : load a table of letters
    @brief : generate
    @param : s.o
    @returns : s.o
    """
    print ('<============PASSERATOR============>')
    dicoLangue={}
    dicoLangue=langParseXML()     
    options=menuOptions(dicoLangue)
    table=tablecaractere(options)
    i=1
    while i<=int(options.split(' ')[7]):
        i+=1
        generator(table,int(options.split(' ')[6])) #this item [6] is a size password
        
    input(dicoLangue.get('13')) #msg : Press enter to quit
    print ('<============END============>')
    exit(0)


# --------
# menu
# --------
def menuOptions(langueDico):
    """
    @brief : Display a menu on the terminal. The user can select a generate mode password
    @param : langueDico : dictionary extract from XML lang
    @return : valueReturn :One list of user options  [y','y','y','y','y','y','9', '5']. options, a password size and number of password
    """
    listeChoixYes=['o','oui','y','yes','si','s']
    listeChoixNo=['non','n','no']

    '----indicate a number of password at generate----'
    nbrPassword=1
    while True:
        try: 
            nbrPassword=int(input(langueDico.get('16')))
            break
        except :
            print(langueDico.get('15'))
            
    print ('\n'+langueDico.get('1'))
    print ('\n'+langueDico.get('2'))
    value=input(langueDico.get('3'))
    if (value in listeChoixYes):
        valueReturn=['y','y','y','y','y','y','9'] #All at YES/OUI ;default value to this mode
    elif(value in listeChoixNo):
        valueReturn=[]
        
        '[0]---Use numbers------------------------'
        value=input ('\n'+langueDico.get('4'))
        if (value in listeChoixYes):
            valueReturn.append('y')
        else:
            valueReturn.append('n')
            
        '[1]---Use Uppercase-----------------------'
        value=input ('\n'+langueDico.get('5'))
        if (value in listeChoixYes):
            valueReturn.append('y')
        else:
            valueReturn.append('n')
            
        '[2]---Use lowercase---------------------- '
        value=input ('\n'+langueDico.get('6'))
        if (value in listeChoixYes):
            valueReturn.append('y')
        else:
            valueReturn.append('n')
            
        '[3]---Use accent------------------ '
        value=input ('\n'+langueDico.get('7'))
        if (value in listeChoixYes):
            valueReturn.append('y')
        else:
            valueReturn.append('n')
            
        '[4]----Use char specific------------------ '
        value=input ('\n'+langueDico.get('8'))
        if (value in listeChoixYes):
            valueReturn.append('y')
        else:
            valueReturn.append('n')
            
        '[5]---Use similar char---------------------- '
        value=input ('\n'+langueDico.get('9'))
        if (value in listeChoixYes):
            valueReturn.append('y')
        else:
            valueReturn.append('n')

        'security: if nothing (char/numbers...) is selected, force to use the defaults values'
        if(valueReturn==['n','n','n','n','n','n']):
            print('\n'+langueDico.get('14'))
            valueReturn=['y','y','y','y','y','y']          
        
        '[6]----Size password--------------------    '
        value=9
        while True:
            try:
                value=int(input('\n'+langueDico.get('10')))
                break
            except :
                print(langueDico.get('15'))
                
        if (value>0):
            value=str(value)
            valueReturn.append(value)#custom size
        else:
            valueReturn.append('9')#default size 9 char
           
    else:
        print (langueDico.get('12'))
        exit(0)
        
    if(nbrPassword<=0):
        nbrPassword=1
    valueReturn.append(str(nbrPassword)) #position [7]

    return ' '.join(valueReturn)#convert a list on string(tupple)


if __name__ == '__main__':
    main()
