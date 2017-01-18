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


def tablecaractere(liste):
    """
    @brief: One table of caractere is create with a user choice in a menu
    @param : liste : user options
    @return : table : a table of caractere authorized for the a traitment
    """

    if(liste.split(' ')[0]=='y'):
        number=string.digits
    else:
        number=''
        
    if(liste.split(' ')[1]=='y'):
        letterMinus=string.ascii_lowercase
    else:
        letterMinus=''

    if(liste.split(' ')[2]=='y'):
        letterMaxi=string.ascii_uppercase
    else:
        letterMaxi=''

    if(liste.split(' ')[3]=='y'):
        letterAccent='àâäåçéèêëîïôöùûü'
    else:
        letterAccent=''

    if(liste.split(' ')[4]=='y'):
        caractSpe='!@#$%^&*(){}[],.;<>?|'
    else:
        caractSpe=''

    table=number+letterMinus+letterMaxi+caractSpe
    if(liste.split(' ')[5]=='n'):
        caractASup=['O0l1I'] #list of similar characters graphics
        for i in range(0,len(caractASup)):
            table=table.replace(caractASup[i],'')
    return table


def generator(charAutori,size):
    """
    @brief : generate password
    @params : charAutori :table of caractere; size: password size
    @return : s.o
    """
    choice = random.SystemRandom().choice
    print('\n'+'* Password :')
    print (''.join(random.choice(charAutori) for i in range(size)))
