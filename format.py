#!/usr/bin/env python
# -*- coding: utf-8 -*-
arq = open('text2.txt', 'w')
texto = []
texto.append('Lista de Alunos\n')
texto.append('---\n')
texto.append('João da Silva\n')
texto.append('José Lima\n')
texto.append('0Maria das Dores')
arq.writelines(texto)
arq.close()


arq = open('text.txt', 'r')
texto = arq.read()
print(texto)
arq.close()

charprevious=texto[0]
for char in texto:
    if char != ' ':
        print (char)
    else:
   

