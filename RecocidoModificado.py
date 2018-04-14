# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 15:52:09 2017

@author: P@b
"""
import random
import copy
import math
from Evaluacion import evaluar

#########################################################################################################################    
############RECOCIDO SIMULADO PARA LA HIPERHEURISTICA#####################################################################
##########################################################################################################################    

#Devuelve un arreglo de posiciones a partir de los sizes del Metabound
def posicion(mBound):
    pos = {}
    ctrl = 0
    for i in range(len(mBound)):
        pos[i] = ctrl
        ctrl = ctrl + mBound[i]["size"]
    return pos
    
#Algoritmo de búsqueda binaria, busca el índice dado la lista de posiciones y el valor a buscar
def busquedaBin(lista,N):
    pos = 0
    inicio  = 0
    final =  len(lista)-1    
    while inicio < final:
        mitad=(final+inicio)/2
        #print lista[mitad]
        if N == lista[mitad] or inicio == final:
            inicio = final = mitad
        if N > lista[mitad]: 
           if inicio == mitad:
               inicio = final = mitad
           inicio = mitad
        else:
            final = mitad            
        pos = mitad
    return pos

#Función para generar el vecindario
#Recibe como parámetro una lista de las posiciones a modificar
#Recibe como parámetro una solución
#Recibe como parámetro el número de vecinos
#Recibe como parámetro el porcentaje de modificación de vecinos
#Recibe como parámetro los datos de Bounds y Metabounds
#Retorna el mínimo de los vecinos
def mejorVecino(posicionPG,sol, numVecinos, porcModificacion, datos):#,modificar): 
    c = 0             #contador de vecinos
    bound = datos["bounds"]
    
    size = len(posicionPG)
    porcModificacion = porcModificacion/100.0
    n = size*porcModificacion    #numero de cambios a cada vecino dependiendo del tamanio de la solucion
    n = int(n)

    ff= evaluar(sol, datos)
    fmin = ff
    smin = copy.copy(sol)
    
    for c in range(numVecinos):
        d = 0 #contador de cambios en cada vecino
        s1=copy.copy(sol)
        while (d < n):
            x = random.randrange(size) #numero de dato
            ndato = posicionPG[x]

            if isinstance(s1[ndato],list) :
                sdato = random.sample(bound[ndato],len(bound[ndato]))
            else:
                sdato = random.choice(bound[ndato])
            s1[ndato] = sdato
            d = d + 1
        ff1 = evaluar(s1,datos)
        if (c == 0 or ff1 < fmin):
            fmin = ff1
            smin = copy.copy(s1)
        c = c + 1
    return fmin,smin

#RECOCIDO SIMULADO PARA LA HIPER-HEURISTICA
#Parámetro adicional -> posicion= posicion de los elementos a modificar (colisiones)
def recocidoSimulado(sol,posicion,datos,iteraciones,tempI,tempMin,vecinos,cambiosPorc,reduccion):

    S     = evaluar(sol,datos)#factibilidad de la solucion inicial
    c    = 0 # contador de iteraciones
    contadorPositivo = 0
    while (c <= iteraciones and tempI >= tempMin):# and noHayCambios != 1):
        Sprima,solAux = mejorVecino(posicion,sol,vecinos,cambiosPorc, datos)
        delta = Sprima-S
        if (delta <= 0):
            S = Sprima
            sol = solAux
            contadorPositivo = 0
        else:
             n = math.exp(-delta/tempI)
             a   = random.random()
             contadorPositivo = contadorPositivo +1
             if(a <= n):
                 S = Sprima
                 sol = solAux
        tempI   = tempI*reduccion
        c   = c + 1
    return sol
