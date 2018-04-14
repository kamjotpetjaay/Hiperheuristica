# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 15:45:01 2017

##################################################################################################################################
############################BÚSQUEDA TABÚ#########################################################################################
##################################################################################################################################

"""

import random
import copy
from time import time
from Solucion import solucion
from Evaluacion import evaluar

#Función para generar el vecindario
#Recibe como parámetro una solución
#Recibe como parámetro el número de vecinos
#Recibe como parámetro el porcentaje de modificación de vecinos
#Recibe como parámetro los datos de Bounds y Metabounds
def SNeighborhood(sol, numVecinos, porcModificacion, datos): 
    c = 0                       #contador de vecinos
    bound = datos["bounds"]     #Datos de las asignaciones (espacio de búsqueda)
    vecinos = []                #Arreglo para guardar los vecinos
    size = len(bound)       
    n = size*porcModificacion   #numero de cambios a cada vecino dependiendo del tamanio de la solucion

    for c in range(numVecinos):
        d = 0                                   #contador de cambios en cada vecino
        s1=copy.copy(sol)                       #copia de la solucion para modificarlo 
        while (d <= n):
            d = d + 1
            ndato = random.randrange(size)      #numero de dato (se genera de manera aleatoria)
            #cuando es permutación de días siempre es de tipo array los datos
            if isinstance(s1[ndato],list) :
                sdato = random.sample(bound[ndato],len(bound[ndato]))
            else:
                sdato = random.choice(bound[ndato])
            s1[ndato] = sdato
        vecinos.append(s1)
    return vecinos

#Encuentra la mejor solucion de una lista de soluciones.
def mejorCandidato(lista,datos):
    fEvalAux = 0
    solAux = []
    c = 0
    best = []
    for sol in lista:
        fEval = evaluar(sol,datos)
        if (c < 1):
            fEvalAux = fEval
            solAux = sol
            best = solAux
        else:
            if fEvalAux > fEval:
                best = sol
                fEvalAux = fEval
                solAux = best
            else:
                best = solAux   
        c = c+1
    return best

#Algoritmo de Búsqueda Tabú
#
# datos =                       datos de entrada en formato JSON  que incluye metabounds y bounds.
# iteraciones =                 parametro Tabú.
# tamaño de Memoria =           parametro Tabú.
# vecinos =                     parámetro Tabú.
# porcentaje de modificación =  parámetro Tabú.
#
def busquedaTabu(datos,iteraciones,tamMemoria,vecinos,porcMod):
    t1 = time()                     #Para contabilizar el tiempo
    sol     = solucion(datos)       #Solución inicial S0
    tempS = evaluar(sol,datos)      #Factibilidad de la solución inicial
    c    = 0                        #Contador de iteraciones
    sBest = sol                     #Se asigna como sBest a la solución inicial
    #PARA Verificar si no hay cambios y romper el ciclo tabú
    #cambiosCiclos = 0
    #anterior = 0
    #out  = 15 # parametro para verificar cada ciertas iteraciones si ya se estanco el algoritmo en una solucion
    #noHayCambios = 0

    tabuList = []
    while (c <= iteraciones): #and noHayCambios != 1):
        candidateList = []
        sVecinos = SNeighborhood(sol,vecinos,porcMod,datos)
        for sCand in sVecinos:
            if sCand not in tabuList:
                candidateList.append(sCand)
        sCandidate = mejorCandidato(candidateList,datos)
        sol = sCandidate
        if (evaluar(sCandidate,datos) < evaluar(sBest,datos)):
            tabuList.append(sCandidate)
            sBest = sCandidate
            if len(tabuList) > tamMemoria:
                fin = len(tabuList)
                inicio = fin-tamMemoria
                tabuList = tabuList[inicio:fin]
        fact = evaluar(sBest,datos)
        print "factibilidad: ",fact, " iteración: ",c

# Salirse si no hay cambios en un determinado número de iteraciones         
#        if c > 0:
#            cambiosCiclos = cambiosCiclos + abs(anterior - fact) #Ir sumando los cambios de 5 generaciones
#            if c % out == 0:#Hacerlo cada ciertas iteraciones (cada 15 )
#                if cambiosCiclos != 0:
#                    if abs(cambiosCiclos) == 0: # Si no hay mucho cambio en 5 generaciones salirse del ciclo porque ya no tiene caso buscar mas soluciones
#                        noHayCambios = 1
#                    cambiosCiclos = 0 # Se reinicia el contador para volver a calcular otras 5 generaciones
#        anterior = fact

        c = c+1
    t2 = time()
    tiempo = t2 - t1
    return tiempo,fact,sBest,tempS
    
#################################################################################
#############################################################################################    