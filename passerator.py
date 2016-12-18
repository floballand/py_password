#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# --------
# Name : PASSERATOR.py
# Objectif : Password Generator
# version : 0.1
# Author : INOPE
# 18/12/2016
# fballand.inope@gmail.com
# --------

# --------
# Imports
# --------
import string
import sys,io,random
import locale
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
    options=menuOptions()
    table=tablecaractere(options)
    generator(table,int(options.split(' ')[6])) #this items [6] is a password size
    input('Press ENTER to quit !')
    print ('END')
    exit(0)

# --------
# langue detection
# --------
def lang():
    lang=locale.getdefaultlocale()
    if (lang[0:1]=="fr"):
        lang="fr"
    else:
        lang="en"
    return lang

# --------
# menu
# --------
def menuOptions():
    """
    Display a menu on the terminal. The user can select a generate mode password
    Args : s.o
    Returns : One list of user options  [ononon9]. the last option is a password size
    """
    listeChoixYes=['o','oui','y','yes']
    listeChoixNo=['non','n','no']

    print ('Choisir les options de generation : ')
    print ('Options par defaut (9 caracteres, ex : O%kYlJ<5S ) ')
    value=input('Votre choix (O/N): ')
    if (value in listeChoixYes):
        valueReturn=['o','o','o','o','o','o','9']
    elif(value in listeChoixNo):
        valueReturn=[]
        '[0]-----------------------------------'
        value=input ('Utilisation de numbers (O/N ) ? Saisir son choix :')
        if (value in listeChoixYes):
            valueReturn.append(value)
        else:
            valueReturn.append('n')
        '[1]-----------------------------------'
        value=input ('Utilisation de majuscules (O/N ) ? Saisir son choix :')
        if (value in listeChoixYes):
            valueReturn.append(value)
        else:
            valueReturn.append('n')
        '[2]----------------------------------- '
        value=input ('Utilisation de minuscule (O/N ) ? Saisir son choix :')
        if (value in listeChoixYes):
            valueReturn.append(value)
        else:
            valueReturn.append('n')
        '[3]----------------------------------- '
        value=input ('Utilisation d\'accent (O/N ) ? Saisir son choix :')
        if (value in listeChoixYes):
            valueReturn.append(value)
        else:
            valueReturn.append('n')
        '[4]----------------------------------- '
        value=input ('Utilisation de caracteres speciaux (O/N ) ? Saisir son choix :')
        if (value in listeChoixYes):
            valueReturn.append(value)
        else:
            valueReturn.append('n')
        '[5]----------------------------------- '
        print ('Utilisation de caracteres similaires (I-l-1,0-O) (O/N ) ? Saisir son choix :')
        if (value in listeChoixYes):
            valueReturn.append(value)
        else:
            valueReturn.append('n')
        '[6]-----------------------------------    '
        print ('Indiquer le taille du mot de passe :')
        value=input('Votre choix: ')
        if (int(value)>0):
            valueReturn.append(value)
        else:
            valueReturn.append('9')
    else:
        print ('No selected Y/O/N. Close program. Please reload program. ')
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
