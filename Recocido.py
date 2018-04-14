# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 15:52:09 2017

#########################################################################################################################    
############RECOCIDO SIMULADO############################################################################################
##########################################################################################################################    
"""

import random
import copy
from time import time
from Solucion import solucion
from Evaluacion import evaluar

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
        mitad = (final+inicio)/2
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

#Busca un mejor vecino utilizando los datos de porcentaje de modificación para alterar una solución.
#Se cambia una asignación completa
#ejemplo si ndato cae un número 6, se busca la asignación que contiene esa posición
#supongamos que tenemos [51,11, 77,14, 91,12,[0,4,2,1,3], 6,22]
#Et,H,  Et,H,  Et,H,D , ....
#la posición 6 está contenido en la asignación 3 por lo que se modifican
# los tres valores de esa asignación Et,H,D. Ésto se hace para que no haya tantas colisiones en las horas y sea
#más variada la solución.
def mejorVecino(solucion, numVecinos, porcModificacion, datos): 
    c = 0             #contador de vecinos
    bound = datos["bounds"]
    mBound = datos["metabounds"]

    size = len(bound)
    n = size*porcModificacion    #numero de cambios a cada vecino dependiendo del tamanio de la solucion
    ff= evaluar(solucion, datos)
    fmin = ff
    smin = copy.copy(solucion)
    posiciones = posicion(mBound)
    for c in range(numVecinos):
        d = 0 #contador de cambios en cada vecino
        s1=copy.copy(solucion)
        while (d <= n):
            d = d + 1
            ndato = random.randrange(size) #numero de dato
            pos = busquedaBin(posiciones.values(),ndato) 
            lenlgs = len(mBound[pos]["lgs"])
            lgs = mBound[pos]["lgs"]
            
            sdato = random.choice(bound[posiciones[pos]]) #Se escoge el espacio t de manera aleatoria.
            s1[posiciones[pos]] = sdato
            
            if mBound[pos]["gpid"]:
                sdato = random.choice(bound[posiciones[pos]+1]) #Se escoge el espacio practica de manera aleatoria.                
                s1[posiciones[pos]+1]
            for j in range(lenlgs):
                if(lgs[j]["hidx"] != -1):
                    sdato = random.choice(bound[posiciones[pos]+lgs[j]["hidx"]]) #Se escoge la hora de manera aleatoria.
                    s1[posiciones[pos]+lgs[j]["hidx"]] = sdato
            
                if(lgs[j]["pidx"] != -1):
                    p = bound[posiciones[pos]+lgs[j]["pidx"]]
                    sdato = random.sample(p,len(p))
                    s1[posiciones[pos]+lgs[j]["pidx"]] = sdato
        ff1 = evaluar(s1,datos)
        if (c == 0 or ff1 < fmin):
            fmin = ff1
            smin = copy.copy(s1)
        c = c + 1
    return fmin,smin

#RECOCIDO SIMULADO
#datos =                    datos de entrada que contienen los metabounds y los bounds
#iteraciones =              parámetro Recocido
#temperatura inicial =      parámetro Recocido
#temperatura mínima =       parámetro Recocido
#número de Vecinos =        parámetro Recocido
#Porcentaje de cambio =     parámetro Recocido
#Reducción de Temperatura = parámetro Recocido
def recocidoSimulado(datos,iteraciones,tempI,tempMin,vecinos,cambiosPorc,reduccion):
    # PARAMETROS
    t1 = time()			
    e = 2.7182818284            #numero de Euler
    sol     = solucion(datos)   #Solución inicial S0
    S     = evaluar(sol,datos)  #factibilidad de la solucion inicial
    c    = 0                    #contador de iteraciones
    tempS = S                   #para retornar la factibilidad de la solución inicial
    #PARA romper ciclo cuando se repitan valores en cierta cantidad de iteraciones
    #out  = 15                   # parametro para verificar cada ciertas iteraciones si ya se estanco el algoritmo en una solucion
    #cambiosCiclos = 0
    #anterior = 0
    #noHayCambios = 0
    
    while (c <= iteraciones and tempI >= tempMin):# and noHayCambios != 1):
        Sprima,solAux = mejorVecino(sol,vecinos,cambiosPorc, datos)
        delta = Sprima-S   
        if (delta <= 0):
            S = Sprima
            sol = solAux
        else:
             exp      = -delta/tempI
             n     = e**exp
             a   = random.uniform(0,1)
             if(a <= n):
                 S = Sprima
                 sol = solAux
        tempI   = tempI*reduccion

        print "factibilidad: ",S, " iteración: ",c

#PARA verificar que no se quede estancado el algoritmo y romper el ciclo
#        if c > 0:
#            cambiosCiclos = cambiosCiclos + abs(anterior - S) #Ir sumando los cambios de 5 generaciones
#            if c % out == 0:#Hacerlo cada ciertas iteraciones (cada 15 )
#                if cambiosCiclos != 0:
#                    if abs(cambiosCiclos) == 0: # Si no hay mucho cambio en 5 generaciones salirse del ciclo porque ya no tiene caso buscar mas soluciones
#                        noHayCambios = 1
#                    cambiosCiclos = 0 # Se reinicia el contador para volver a calcular otras 5 generaciones
#        anterior = S
        c   = c + 1
        
    t2 = time()
    tiempo = t2 - t1
    return tiempo,S,sol,tempS