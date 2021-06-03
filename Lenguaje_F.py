#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:28:56 2019

@author: davidbellobustamante
"""

frase = input("Escribe una frase: ")       
largo = len(frase)                                    
inicio = 0                                                    
frase_final = ""                                                       
lenguaje = ""                                               
while inicio < largo:                                    
    if frase[inicio] in "a":                                                                                   
        lenguaje="afa"                                 
    elif frase[inicio] in "e":                    
        lenguaje="efe"                                      
    elif frase[inicio] in "i":
        lenguaje="ifi"
    elif frase[inicio] in "o":
        lenguaje="ofo"
    elif frase[inicio] in "u":
        lenguaje="ufu"
    elif frase[inicio] in "y":
        lenguaje="yfi"
    elif frase[inicio] in "á":
        lenguaje="áfa"
    elif frase[inicio] in "í":
        lenguaje="ífi"
    elif frase[inicio] in "é":
        lenguaje="éfe"
    elif frase[inicio] in "ú":
        lenguaje="úfu"
    elif frase[inicio] in "ü":
        lenguaje="üfu"        
    else:                                                  
        lenguaje = frase[inicio]                 
    frase_final += lenguaje                                 
    inicio += 1                                            
                                        
print(frase_final)                                             
input()