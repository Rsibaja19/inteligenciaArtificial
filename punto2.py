# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 21:09:10 2022

@author: rsibaja
"""

p1 = int(input("Digite el valor de su inversion"))
p2 = int(input("Digite el valor de su inversion"))
p3 = int(input("Digite el valor de su inversion"))
total = p1 + p2 + p3
porcentajep1 = p1 / total * 100
porcentajep2 = p2 / total * 100
porcentajep3 = p3 / total * 100
print(f' el porcentaje de la inversion de la primera persona es:  {porcentajep1:,}')
print(f' el porcentaje de la inversion de la segunda persona es:  {porcentajep2:,}')
print(f' el porcentaje de la inversion de la tercera persona es:  {porcentajep3:,}')
