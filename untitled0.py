# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 08:03:26 2021

@author: rdeblaere
"""

def listReadValues(fileName):
    """ 
    Function to read numbers from a file, this functions reads the complete file and returns a list of floats (one float per line)

    Parameters
    ----------
    fileName : str
        The path (full path or relative w.r.t. the working directory) 
        of the file to read.
        
    """
    file = open(fileName, mode = 'r', encoding="utf-8")
    # read file and put values as strings in a list
    value_str_list = file.read().splitlines() 
    file.close()
    value_float_list = []         # list to hold the values as floats
    for value_str in value_str_list:
        value_float_list.append(float(value_str))
    return(value_float_list)

def listRead(fileName):
    """ 
    Function to read tekst from a file, this functions reads the complete file and returns a list of strings (one string per line)

    Parameters
    ----------
    fileName : str
        The path (full path or relative w.r.t. the working directory) 
        of the file to read.
        
    """
    name_file = open(fileName, mode = 'r', encoding="utf-8")
    mylist = name_file.read().splitlines() 
    name_file.close()
    return(mylist)
    
def stringRead(fileName):
    """ 
    Function to read tekst from a file, this functions reads the complete file and returns a single string

    Parameters
    ----------
    fileName : str
        The path (full path or relative w.r.t. the working directory) 
        of the file to read.
        
    """
    name_file = open(fileName, mode = 'r', encoding="utf-8")
    mystring = name_file.read().strip()
    name_file.close()
    return(mystring)    
    
def listWrite(fileName, list_of_strings):
    """ 
    Function to write a list of strings to a text file (one line per string)

    Parameters
    ----------
    fileName : str
        The path (full path or relative w.r.t. the working directory) 
        of the file that is created (if it exists, it will be overwritten)
        
    list_of_strings : list
        A list of strings that is written to "fileName"
        
    """
    name_file = open(fileName, mode = 'w', encoding="utf-8")
    name_file.write('\n'.join(list_of_strings))
    name_file.close()
    return(None) 
    
def stringWrite(fileName, mystring):
    name_file = open(fileName, mode = 'w', encoding="utf-8")
    name_file.write(mystring)
    name_file.close()
    return(None)    

lijst = listRead("APD FULL no_double_names_1.csv")
onbreekt = listRead("lijst_ontbrekend.txt")


def get_names(string, tussenvoegsel = ",", naamkolom = 5):
    string = string + tussenvoegsel
    j = 0
    geg = list()
    for i in range(len(string)):
        if string[i] == tussenvoegsel:
            geg.append(string[j:i])
            j = i + 1
    acceptedname = geg[naamkolom]
    acceptedname = acceptedname.strip()
    if type(acceptedname) == str and " " in acceptedname:
        return acceptedname
    else:
        return ""
        
def check_geography(string, tussenvoegsel = ";"):
    string = string + tussenvoegsel
    j = 0
    geg = list()
    for i in range(len(string)):
        if string[i] == tussenvoegsel:
            geg.append(string[j:i])
            j = i + 1
    if len(geg)<=0:
        return ""
    else:
        acceptedname = geg[0]
        acceptedname = acceptedname.strip()
        country = geg[1]
        if country == "Congo, Dem. Rep.":
            print(acceptedname)
            return acceptedname
        else:
            return ""
    
onbreekt_nieuw = list()
for i in onbreekt:
    onbreekt_nieuw.append(i.strip())

output = list()
for i in lijst:
    for j in onbreekt_nieuw:
        if j in i:
            output.append(get_names(i))
new_output = list()
for i in output:
    if i != "":
        new_output.append(i)

echte_output = list()      
for i in new_output:
    for j in range(len(new_output)):
        if new_output[j] == i:
            if not i in echte_output:
                echte_output.append(i)
print(echte_output)
listWrite("output.txt", echte_output)

#

Tw = listRead("Tw_test.csv")

Uit_DRC = list()
for i in echte_output:
    for j in Tw:
        if i in j:
            Uit_DRC.append(check_geography(j))

new_Uit_DRC = list()
for i in Uit_DRC:
    if i != "":
        new_Uit_DRC.append(i)

echte_DRC = list()      
for i in new_Uit_DRC:
    x = 0
    for j in range(len(new_Uit_DRC)):
        if new_Uit_DRC[j] == i:
            if not i in echte_DRC:
                echte_DRC.append(i)
        
print(echte_DRC)
listWrite("DRC.txt", echte_DRC)

smartwoodID_Lore = listRead("smartwoodID_lore.csv")

fin_list_core_collection = list()
for i in echte_DRC:
    if not i in smartwoodID_Lore:
        fin_list_core_collection.append(i)

listWrite("finale lijst core collectie smartwoodID", fin_list_core_collection)


