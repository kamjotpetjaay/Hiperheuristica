# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 15:56:06 2017

@author: P@b
"""
import copy
import random
from time import time
from Solucion import solucion
from Evaluacion import evaluar

##################################################################################################################################
############################BÚSQUEDA ARMÓNICA PARA LA HIPER-HEURISTICA#########################################################################################
##################################################################################################################################


#Función para generar el vecindario
#Recibe como parámetro una solución
#Recibe como parámetro el número de vecinos
#Recibe como parámetro el porcentaje de modificación de vecinos
#Recibe como parámetro los datos de Bounds y Metabounds
#Recibe como parámetro una lista de las posiciones a modificar
#Retorna los vecinos
def SNeighborhood(sol, numVecinos, porcModificacion, datos,posicion): 
    c = 0             #contador de vecinos
    bound = datos["bounds"]
    vecinos = []
    n = len(posicion)*porcModificacion    #numero de cambios a cada vecino dependiendo del tamanio de la solucion
    cont = 0
    cambios = []

    while(cont < n):
        val = random.choice(posicion)
        if val not in cambios:
            cont = cont +1
            cambios.append(val)      
    for c in range(numVecinos):
        s1=copy.copy(sol)
        for c in cambios:
            #cuando es permutación de días siempre es de tipo array los datos
            if isinstance(s1[c],list) :
                sdato = random.sample(bound[c],len(bound[c]))
            else:
                sdato = random.choice(bound[c])
            s1[c] = sdato
        vecinos.append(s1)
    return vecinos
    
#Función para generar una población
#Recibe como parámetro el número de Individuos a formar
#Recibe como parámetro la solucion que viene de la hiper-heuristica
def generaPoblacion(N,sol):
    poblacion = []
    for i in range(N):
        poblacion.append(sol)
    return poblacion
    
#Función que devuelve un elemento aleatorio de una lista
def getRandomHM(vectorHM):
    N = len(vectorHM)
    return vectorHM[random.randint(0,N-1)]

#Función que evalúa la modificación de una solución
#Recibe como parámetro la probabilidad de modificación
#Recibe como parámetro el porcentaje de modificación
#Recibe como parámetro la solución a modificar
#Recibe como parámetro los datos de Bounds y Metabounds
#Recibe como parámetro una lista de las posiciones a modificar
def modificar(probabilidad,porcentajeMuta,sol,datos,posicion):
    probabilidadA = random.randint(0,100)
    if probabilidadA <= probabilidad:
        vecinos = SNeighborhood(sol,1,(porcentajeMuta/100.0),datos,posicion)
        sol = vecinos[0]
    return sol
    
#Función que encuentra la peor solución de una lista
#Recibe como parámetro la lista de soluciones
#Recibe como parámetro los datos de Bounds y Metabounds
def peorS(lista,datos):
    maxLista = []
    for i in range (len(lista)):
        maxLista.append(evaluar(lista[i],datos))
    maximo = max(maxLista)
    for i in range (len(lista)):
        if(maxLista[i] == maximo):
            indice = i 
    return [indice,maximo]
    
#Función para encontrar el mínimo en una población
#Recibe como parámetro la lista de donde se va a buscar el mínimo
#Recibe como parámetro los datos de Bounds y Metabounds
def minimoP(lista,datos):
    minLista = []
    for i in range (len(lista)):
        minLista.append(evaluar(lista[i],datos))
    minimo = min(minLista)
    for i in range (len(lista)):
        if(minLista[i] == minimo):
            indice = i 
    return lista[indice]

#Algoritmo de Búsqueda Armónica utilizado por la hiper-heurística
#
# solución =                    solución inicial a modificar
# datos =                       datos de entrada en formato JSON  que incluye metabounds y bounds.
# posicion =                    lista de las posiciones a modificar
# número de Iteraciones =       parametro Armónica.
# tamaño de Memoria Armónica =  parametro Armónica.
# Razón de exploración =        parámetro Armónica.
# Ancho de desplazamiento =     parámetro Armónica.
# Razón de ajuste de tono =     parámetro Armónica.
#    
def busquedaArmonica(sol,datos,posicion,iteraciones,HMS,HMCR,BW,PAR):
    HM = generaPoblacion(HMS,sol)
    #HM.append(sol)

    #out  = 15 # parametro para decidir si ya se estancó el algoritmo en una solucion
    c    = 0 # contador de iteraciones
    #noHayCambios = 0
    #anterior = 0
    #cambiosCiclos = 0
    while (c <= iteraciones):# and noHayCambios != 1):
        obtenerMemoria = random.random()
        if(obtenerMemoria < (HMCR/100.00)):
            elem = getRandomHM(HM)
            #modificar la armonía en un porcentaje
            copia = elem[:]
            modificar(PAR,BW,copia,datos,posicion)
        else:
            copia = solucion(datos)
        #ESCOJER LA PEOR DE LA MEMORIA ARMÓNICA PARA SUSTITUIRLA CON EL NUEVO SI ES MEJOR
        [indice,maximo] = peorS(HM,datos)
        nuevo = evaluar(copia,datos)
        if nuevo < maximo:
            HM[indice] = copia

        vecMin = minimoP(HM,datos)

        #PARA romper ciclo en caso de que se quede estancado
        #fact = evaluar(vecMin,datos)
        #if c > 0:
        #    cambiosCiclos = cambiosCiclos + abs(anterior - fact) #Ir sumando los cambios de 5 generaciones
        #    if c % out == 0:#Hacerlo cada ciertas iteraciones (cada 15 )
        #        if cambiosCiclos != 0:
        #            if abs(cambiosCiclos) == 0: # Si no hay mucho cambio en 5 generaciones salirse del ciclo porque ya no tiene caso buscar mas soluciones
        #                noHayCambios = 1
        #            cambiosCiclos = 0 # Se reinicia el contador para volver a calcular otras 5 generaciones
        #anterior = fact
        c = c + 1
        
    return vecMin 
#################################################################################
#############################################################################################    
