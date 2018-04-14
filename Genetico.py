# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 15:57:08 2017

##################################################################################################################################
############################ALGORITMO GENÉTICO#########################################################################################
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
    c = 0             #contador de vecinos
    bound = datos["bounds"]
    #mBound = datos["metabounds"]
    vecinos = []
    size = len(bound)
    n = size*porcModificacion    #numero de cambios a cada vecino dependiendo del tamanio de la solucion
    for c in range(numVecinos):
        d = 0 #contador de cambios en cada vecino
        s1=copy.copy(sol)
        while (d <= n):
            d = d + 1
            ndato = random.randrange(size) #numero de dato
            #cuando es permutación de días siempre es de tipo array los datos
            if isinstance(s1[ndato],list) :
                sdato = random.sample(bound[ndato],len(bound[ndato]))
            else:
                sdato = random.choice(bound[ndato])
            s1[ndato] = sdato
        vecinos.append(s1)
    return vecinos
    
#Función para hacer la mutación
#Recibe como parámetro la probabilidad de mutación
#Recibe como parámetro el porcentaje de mutación
#Recibe como parámetro la solución a mutar
#Recibe como parámetro los datos de Bounds y Metabounds
def mutar(probabilidad,porcentajeMuta,sol,datos):
    probabilidadA = random.randint(0,100)
    if probabilidadA <= probabilidad:
        #Se utiliza la función que modifica la solución y devuelve un arreglo de vecinos.
        vecinos = SNeighborhood(sol,1,(porcentajeMuta/100.0),datos)
        sol = vecinos[0] # como solo se necesita mutar una solución, se obtiene el único.
    return sol
    
#Función para generar una población
#Recibe como parámetro el número de Individuos a formar
#Recibe como parámetro los datos de Bounds y Metabounds
def generaPoblacion(N,datos):
    poblacion = []
    for i in range(N):
        poblacion.append(solucion(datos))
    return poblacion

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
    
#Función para generar los padres
#Recibe como parámetro el porcentaje de selección
#Recibe como parámetro el tamaño de la población (se genera la mitad)
#Recibe como parámetro una lista de población
#Recibe como parámetro los datos de Bounds y Metabounds
def generaPadres(porcentajeSeleccion,tam,listaPoblacion,datos):
    listaMejores = []
    porcentaje = (porcentajeSeleccion/100.0)*(len(listaPoblacion))
    i = 0
    while i < (tam/2):  
        listaTemp = []
        #Toma un porcentaje de elementos de la población aleatoriamente y busca el mínimo
        for j in range (int(porcentaje)):
            listaTemp.append(random.choice(listaPoblacion))
        temp = minimoP(listaTemp,datos)
        listaMejores.append(temp)
        i= i+1
    return listaMejores

#Función para cruzar dos padres y generar dos hijos
#Recibe como parámetro el padre 1
#Recibe como parámetro el padre 2
#Recibe como parámetro el porcentaje de cruza
#Recibe como parámetro una lista de hijos que va a ir aumentando
def cruzar(padre1,padre2,porcentajeCruza,listaHijos):
    porcentaje = (porcentajeCruza/100.0)*len(padre1)
    listaCambiar = []
    porcentaje = int(porcentaje)
    i = 0
    #Se genera una lista de posiciones para intercambiarlos
    while i < porcentaje:
        num = random.randint(0,(len(padre1)-1))
        if num in listaCambiar:
            while num in listaCambiar:
                num = random.randint(0,(len(padre1)-1))
            listaCambiar.append(num)
        else:
            listaCambiar.append(num)
        i = i+1
    #Se intercambian los elementos de la lista a cambiar en ambos padres
    for x in range(len(listaCambiar)):
        aux = padre1[listaCambiar[x]]
        padre1[listaCambiar[x]] = padre2[listaCambiar[x]]
        padre2[listaCambiar[x]] = aux
    listaHijos.append(padre1)
    listaHijos.append(padre2)


#Función que evalúa el cruzamiento
#Recibe como parámetro el porcentaje de cruzamiento
#Recibe como parámetro una lista de padres
#Recibe como parámetro los datos de Bounds y Metabounds
def cruzarHijos(porcentajeCruza,listaPadres,datos):
    listaHijos = []
    i = 0
    #Se escogen de manera aleatoria dos padres para cruzar
    while i < len(listaPadres):
        padre1 = random.choice(listaPadres)
        padre2 = random.choice(listaPadres)
        cruzar(padre1,padre2,porcentajeCruza,listaHijos)
        i = i+1        
    return listaHijos

#Algoritmo Genético
#
# datos =                       datos de entrada en formato JSON  que incluye metabounds y bounds.
# número de Generaciones =      parametro Genético.
# tamaño de Población =         parametro Genético.
# porcentaje de cruza =         parámetro Genético.
# probabilidad de mutación =    parámetro Genético.
# porcentaje de mutación =      parámetro Genético.
# porcentaje de selección =     parámetro Genético.
#
def algoritmoGenetico(datos,numGeneraciones,tamPoblacion,Pcruza,probabilidadMutacion,porMutacion,porSeleccion):
    t1 = time()
    #GENERAR POBLACION INICIAL
    listaPoblacion = generaPoblacion(tamPoblacion,datos)
    sMax = evaluar(minimoP(listaPoblacion,datos),datos)# factibilidad mínima inicial
    contador = 0
    
    #Para romper ciclo en caso de estancamiento
    #out = 0
    #cambiosMinimos = 0
    #cambiosGeneraciones = 0
    #rangoCambios = 50 #(rango mínimo de cambios), si no se cumple se sale del ciclo. Entra cuando hay tres cambios positivos o negativos
    #anterior = 0
    #GENERACIONES
    while(contador < numGeneraciones):# and cambiosMinimos != 1 and out < 3):  

        #Seleccion (por Torneo)
        listaPadres = generaPadres(porSeleccion,tamPoblacion,listaPoblacion,datos)

        #Cruzamiento
        #N puntos Lineal (al azar)
        listaPoblacion = cruzarHijos(Pcruza,listaPadres,datos)

        #Mutacion
        listaNueva = []
        for elem in listaPoblacion: 
            listaNueva.append(mutar(probabilidadMutacion,porMutacion,elem,datos))    

        listaPoblacion = listaNueva
        fact = evaluar(minimoP(listaPoblacion,datos),datos)
        print "factibilidad: ",fact, " iteración: ",contador
        
        #VERIFICAR que no haya estancamiento en el algoritmo
        #if contador > 0:
        #    cambiosGeneraciones = cambiosGeneraciones + abs(anterior - fact) #Ir sumando los cambios de 5 generaciones
        #    if contador % 5 == 0:#Hacerlo cada ciertas iteraciones (cada 5 generaciones)
        #        if cambiosGeneraciones != 0:
        #            if abs(cambiosGeneraciones) < rangoCambios: # Si no hay mucho cambio en 5 generaciones salirse del ciclo porque ya no tiene caso buscar mas soluciones
        #                cambiosMinimos = 1
        #            cambiosGeneraciones = 0 # Se reinicia el contador para volver a calcular otras 5 generaciones
        #            out = 0
        #        else:
        #            out = out+1 #es igual a 5 ciclos que no tienen cambios   
        #anterior = fact
        contador = contador + 1
    listMinimo = minimoP(listaPoblacion,datos)
    
    t2 = time()
    tiempo = t2-t1
    return tiempo,evaluar(listMinimo,datos),listMinimo,sMax#[tiempo,final,listMinimo]
