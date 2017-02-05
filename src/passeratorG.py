#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
 @name : PASSERATORG.py
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
from PyQt5 import QtWidgets, uic,QtCore
from PyQt5.QtCore import pyqtSignal
 

"""
Password Generate
"""       
def conversionLangue(langueDico):
    """
    @brief : langue convertisor to label
    @return : s.o
    """
    widget.txtAccent.setText(langueDico.get('7'))
    widget.txtUppercase.setText(langueDico.get('5'))
    widget.txtLowercase.setText(langueDico.get('6'))
    widget.txtSpecial.setText(langueDico.get('8'))
    widget.txtNumPassword.setText(langueDico.get('16'))
    widget.txtSimilar.setText(langueDico.get('9'))
    widget.txtWithNumber.setText(langueDico.get('4'))
    widget.txtSizePassword.setText(langueDico.get('10'))
    
def connector():
    """
    @brief : all connector UI
    @return : s.o
    """
    widget.btGenerate.clicked.connect(actionButtonGenerate)
    
def optionsPassword():
    """
    @brief : Dectect the options select by a user withUI
    @return : valueReturn :One list of user options  [y','y','y','y','y','y','9', '5']. options, a password size and number of password
    """
    valueReturn=[]
    if (widget.chkWithNumber.isChecked()):
       valueReturn.append('y')
    else:
        valueReturn.append('n')
       
    if (widget.chkWithLowercase.isChecked()):
       valueReturn.append('y')
    else:
        valueReturn.append('n')
        
    if (widget.chkWithUppercase.isChecked()):
       valueReturn.append('y')
    else:
        valueReturn.append('n')
        
    if (widget.chkWithAccent.isChecked()):
       valueReturn.append('y')
    else:
        valueReturn.append('n')
        
    if (widget.chkWithSpecial.isChecked()):
       valueReturn.append('y')
    else:
        valueReturn.append('n')
        
    if (widget.chkWithSimilar.isChecked()):
       valueReturn.append('y')
    else:
        valueReturn.append('n')
        
    #security: if nothing (char/numbers...) is selected, force to use the defaults values'
    if(valueReturn==['n','n','n','n','n','n']):
        valueReturn=['y','y','y','y','y','y'] 

    valueReturn.append(str(widget.spSize.value()))
    valueReturn.append(str(widget.spNumber.value()))
    return ' '.join(valueReturn)#convert a list on string(tupple)

def actionButtonGenerate():
    """
    @brief : action's button generate
    @brief : generate dictionnary
    @brief : generate password
    @return : s.o.
    """
    options=optionsPassword()
    table=tablecaractere(options)
    i=1
    allValue=""
    while i<=int(options.split(' ')[7]):
        i+=1
        value=generator(table,int(options.split(' ')[6])) #this item [6] is a size password
        allValue=value+"\n"+allValue        
    widget.teResult.setText(allValue)
    
def main():
    """ Main function
    @brief : read a file XML lang
    @brief : langue conversion
    @brief : load a table of letters
    @param : s.o
    @returns : s.o
    """
    dicoLangue={}
    dicoLangue=langParseXML()
    conversionLangue(dicoLangue)
    connector()        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = uic.loadUi("gui/passeratorgui.ui")
    main()
    widget.show()
    app.exec_()

