#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:40:20 2019

@author: davidbellobustamante
"""

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
# Tokenizador TokTok (palabras)
toktok = ToktokTokenizer()
# Tokenizador de oracionesa
es_tokenizador_oraciones = nltk.data.load('tokenizers/punkt/spanish.pickle')
# Obtener oraciones de un parrafo
with open ("practica3.txt", 'r') as file: #ass fp:
  parrafo=file.read()
  oraciones = es_tokenizador_oraciones.tokenize(parrafo)
  
  # Obtener tokens de cada oración
  var=[]
  for s in oraciones:
    var=var+[t for t in toktok.tokenize(s)]
  print (var)
file.close()