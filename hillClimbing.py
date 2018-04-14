# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 22:51:43 2017

@author: P@b
#########################################################################################################################    
############Descenso de Colina PARA LA HIPERHEURISTICA#####################################################################
##########################################################################################################################    
"""
import random
import copy
from Evaluacion import evaluar

def posicion(mBound):
    pos = {}
    ctrl = 0
    #mBound = datos["metabounds"] #metabounds
    for i in range(len(mBound)):
        pos[i] = ctrl
        ctrl = ctrl + mBound[i]["size"]
    return pos

def descensoColina(sol,datos,posProblema,iteraciones,porcentaje):
    bound = datos["bounds"]
    fact = evaluar(sol,datos)
    i = 0
    s1=copy.copy(sol)
    sol2 = s1
    n = len(posProblema)
    n = porcentaje*n
    n = int(n)
    
    
    while i < iteraciones:
        d = 0
        while (d < n):
            ndato = posProblema[random.randrange(len(posProblema))]
            #Se van a modificar los dias
            if isinstance(s1[ndato],list) :
                sdato = random.sample(bound[ndato],len(bound[ndato]))
            else:
                sdato = random.choice(bound[ndato])
            s1[ndato] = sdato

            d = d + 1
        factNuevo = evaluar(s1,datos)
        if factNuevo < fact:
            sol2 = s1
            fact = factNuevo
        i = i+1
    return sol2

def descensoColinaSimple(sol,datos,posProblema,iteraciones,porcentaje):
    bound = datos["bounds"]
    fact = evaluar(sol,datos)
    i = 0
    s1=copy.copy(sol)
    sol2 = s1
    n = len(posProblema)
    n = porcentaje*n
    n = int(n)
    
    while i < iteraciones:
        d = 0
        while (d < n):
            ndato = posProblema[random.randrange(len(posProblema))]
            #Se van a modificar los dias
            if isinstance(s1[ndato],list) :
                sdato = random.sample(bound[ndato],len(bound[ndato]))
            else:
                sdato = random.choice(bound[ndato])
            s1[ndato] = sdato

            d = d + 1
        if evaluar(s1,datos) < fact:
            sol2 = s1
            i = iteraciones
        i = i+1
    return sol2
    
