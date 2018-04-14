# -*- coding: utf-8 -*-
"""
Created on Mon May 29 14:14:49 2017

@author: P@b
"""
import random
import copy
from time import time
from Solucion2 import solucion
from Evaluacion import evaluar
from Seleccion import seleccionar
from RecocidoModificado import recocidoSimulado as recocidoEspaciosHoras
from hillClimbing import descensoColina
from hillClimbing import descensoColinaSimple
from ArmonicaModificado import busquedaArmonica

#Función para generar una población
#Recibe como parámetro el número de Individuos a formar
#Recibe como parámetro los datos de Bounds y Metabounds
#Retorna un elemento que contiene la mejor solución con sus datos fijos y sus datos prioritarios
def poblacionInicial(n,datos):
    contador = 0
    solBest,datosFijosBest,datosPrioritariosBest = solucion(datos)
    while contador < n-1:
        sBest,datosFIJOS,datosPRIORITARIOS = solucion(datos)
        if evaluar(sBest,datos) < evaluar(solBest,datos):
            solBest = sBest
            datosFijosBest = datosFIJOS
            datosPrioritariosBest = datosPRIORITARIOS
        contador = contador +1
    return solBest,datosFijosBest,datosPrioritariosBest
        
    
def sbusquedaArmonica(solucion,datos,posicion):
    solNueva = busquedaArmonica(solucion,datos,posicion,150,20,60,60,25)
    return solNueva
    
def recocidoSimuladoModificado(solucion,datos,posicion):
    solNueva = recocidoEspaciosHoras(solucion,posicion,datos,150,100,0.00001,50,40,0.97)
    return solNueva
    
#Función para generar el vecindario
#Recibe como parámetro una solución
#Recibe como parámetro el número de vecinos
#Recibe como parámetro el porcentaje de modificación de vecinos
#Recibe como parámetro los datos de Bounds y Metabounds
#Recibe como parámetro una lista de datos fijos que no deben ser modificados
def SNeighborhood(sol, numVecinos, porcModificacion, datos,datosFIJOS): 
    c = 0             #contador de vecinos
    bound = datos["bounds"]
    vecinos = []
    size = len(sol)
    listaPosDatos = list (range(size))
    listaPosDatos = list(set(listaPosDatos)-set(datosFIJOS))
    size = len(listaPosDatos)
    porcModificacion = porcModificacion/100.0
    n = size*porcModificacion    #numero de cambios a cada vecino dependiendo del tamanio de la solucion
    n = int(n)
    
    for c in range(numVecinos):
        d = 0 #contador de cambios en cada vecino
        s1=copy.copy(sol)
        while (d < n):
            ndato = random.randrange(size) #numero de dato
            ndato = listaPosDatos[ndato]
            #cuando es permutación de días siempre es de tipo array los datos
            if isinstance(s1[ndato],list) :
                sdato = random.sample(bound[ndato],len(bound[ndato]))
            else:
                sdato = random.choice(bound[ndato])
            s1[ndato] = sdato
            d = d + 1
        vecinos.append(s1)
    return vecinos

#Función para seleccionar el mejor candidato
#Recibe como parámetro la lista de candidatos a evaluar
#Recibe como parámetro los datos de Bounds y Metabounds
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
        else:
            if fEvalAux > fEval:
                best = sol
                fEvalAux = fEval
                solAux = best
            else:
                best = solAux   
        c = c+1
    return best
    
#Función para seleccionar el mejor candidato
#Recibe como parámetro la lista de candidatos a evaluar
#Recibe como parámetro los datos de Bounds y Metabounds
def verificarProblema(solucion,datos,listaFactAnterior,datosPRIORITARIOS,datosPrioritarios):
    posicion,factibilidad = seleccionar(solucion,datos)
    #datosPrioritarios = 0
    resta = []

    if datosPrioritarios == 0:
        prioritarios = 0
        datosPRIORITARIOSAux = set(datosPRIORITARIOS)
        for i in range(len(posicion)):
            prioritarios = prioritarios+ len(list(set(posicion[i])&datosPRIORITARIOSAux))
        if prioritarios == 0:
            datosPrioritarios = 1
    
    for i in range(len(factibilidad)):
        resta.append(factibilidad[i] - listaFactAnterior[i])
        
    P = max(resta)
    if P == 0:
        resta = factibilidad
        P = max(factibilidad)
    pos = resta.index(P)      
    
    
    
    #print pos
    if pos == 0:
        metaH = "local1"
    if pos == 1:
        metaH = "local2"
    if pos == 2:
        metaH = "local3"
    if pos == 3:
        metaH = "local4"
    if pos == 4:
        metaH = "local5"
    if pos == 5:
        metaH = "local6"
    if pos == 6:
        metaH = "local7"
    if pos == 7:
        metaH = "local8"
    if pos == 8:
        metaH = "local9"
    if pos == 9:
        metaH = "local10"
    if pos == 10:
        metaH = "local11"
    
    return posicion[pos],posicion[11],metaH,factibilidad,datosPrioritarios
    
    
    
    
#HIPERHEURISTICA BASADO EN BUSQUEDA TABU
def hiperheuristica(datos,iteraciones,tamMemoria,vecinos,porcMod):
    t1 = time()
    #Se puede iniciar con la mejor solucion de 100 elementos aleatorios
    sBest,datosFIJOS,datosPRIORITARIOS = poblacionInicial(100,datos) #Solución inicial S0
    #se puede iniciar con un solo elemento aleatorio
    #sBest,datosFIJOS,datosPRIORITARIOS = solucion(datos) #Solución inicial S0

    #sFinal = sBest                          #la solución incial
    datosPrioritarios = 0                   #para ir contabilizando los datos prioritarios restantes
    #evalúa las colisiones de cada restricción y devuelve sus valores y las posiciones de colisiones
    posicion,listaFactibilidad = seleccionar(sBest,datos)
    c    = 0 # contador de iteraciones
    tabuList = []
    valorAuxRepeticiones = 0
    contadorRepeticiones = 0
    
    #5 % de valores repetidos para que se modifique a otro método
    #noRepetir = 20
    #noRepetir = iteraciones*(noRepetir/100.0)
    #noRepetir = int(noRepetir)
    
    while (c < iteraciones):# and noHayCambios != 1):
        candidateList = []
        #Genera vecinos sin tomar en cuenta los datos fijos
        sVecinos = SNeighborhood(sBest,vecinos,porcMod,datos,datosFIJOS)

        for sCand in sVecinos:
            if sCand not in tabuList:
                candidateList.append(sCand)
        sCandidate = mejorCandidato(candidateList,datos)
        
        #En esta parte se identifican los problemas en la solución
        posProblema,posProb2,metaH,fact,datosPrioritarios = verificarProblema(sCandidate,datos,listaFactibilidad,datosPRIORITARIOS,datosPrioritarios)
        #Para verificar que ya se hayan satisfecho los datos prioritarios para convertirlos en fijos
        if (datosPrioritarios == 1):
            datosFIJOS = datosFIJOS+ list(datosPRIORITARIOS)
            datosPRIORITARIOS = []
            datosPrioritarios = -1

        datosFIJOS = set(datosFIJOS)
        posProblema = list(set(posProblema)-datosFIJOS)
        datosFIJOS = list(datosFIJOS)
        
        listaFactibilidad = fact
        
        #clases de teoria y practica no deben ser a la misma
        #hora, el mismo día (MODIFICAR DIA)
        if metaH == "local1":
            solNueva = descensoColinaSimple(sCandidate,datos,posProblema,30,40)
            #print "falta"
    
        #Las clases no deben impartirse fuera del horario de clases
        if metaH == "local2":
            solNueva = descensoColinaSimple(sCandidate,datos,posProblema,30,40)
            #print "falta"
        
        #Un profesor no puede estar en dos lugares distintos a la 
        #misma hora, el mismo día (MODIFICAR HORA)
        if metaH == "local3":
            solNueva = descensoColina(sCandidate,datos,posProblema,80,40)
            #print "falta"
        
        #Dos o mas profesores o grupos no pueden estar en el mismo lugar
        #a la misma hora, el mismo día a menos que sea multiasignacion
        if metaH == "local4":
            
            datosFIJOS = set(datosFIJOS)
            posProb2 = list(set(posProb2)-datosFIJOS)
            datosFIJOS = list(datosFIJOS)
            solNueva = recocidoSimuladoModificado(sCandidate,datos,posProblema)
            solNueva = recocidoSimuladoModificado(solNueva,datos,posProb2)
                
        
        #Un mismo grupo no puede tener asignada otra clase, ya sea en el mismo
        # o diferente lugar a la misma hora, el mismo día. a menos que sean
        #clases de diferentes especialidades de ese grupo (MODIFICAR HORA)
        if metaH == "local5":
            #el algoritmo armónica necesita otros parámetros para mejorar la solución
            solNueva = sbusquedaArmonica(sCandidate,datos,posProblema)
            #solNueva = descensoColina(sCandidate,datos,posProblema,100,2)

        #Si un profesor da clases a la 8, no puede dar clases a la 1 (MODIFICAR HORA)
        if metaH == "local6":
            solNueva = descensoColinaSimple(sCandidate,datos,posProblema,30,40)

        #Un grupo no puede tomar clases obligatorias a la misma hora en la que un alumno de recursamiento toma clases junto a otro grupo
        #(MODIFICAR HORA)
        if metaH == "local7":
            solNueva = descensoColinaSimple(sCandidate,datos,posProblema,30,40)

        #Un grupo debe tener dos horas libres al día (MODIFICAR HORA)
        if metaH == "local8":
            solNueva = descensoColinaSimple(sCandidate,datos,posProblema,30,40)

        #Un espacio solo puede permitir 9 horas al día
        if metaH == "local9":
            solNueva = descensoColinaSimple(sCandidate,datos,posProblema,50,40)

        #Heuristica 1 (restricción débil)
        if metaH == "local10":
            solNueva = descensoColina(sCandidate,datos,posProblema,30,40)

        #Heurística 2 (restricción débil)
        if metaH == "local11":
            solNueva = descensoColina(sCandidate,datos,posProblema,30,40)
        
        if (evaluar(solNueva,datos) < evaluar(sBest,datos)):
            sBest = solNueva
            if len(tabuList) > tamMemoria:
                tabuList.pop(0)
            tabuList.append(solNueva)
            
        fact = evaluar(sBest,datos)

        print "factibilidad: ",fact, " iteración: ",c
#PARA ROMPER CICLO cuando se estanca 
        #if c > 0:
        #    cambiosCiclos = cambiosCiclos + abs(anterior - fact) #Ir sumando los cambios de 5 generaciones
        #    if c % out == 0:#Hacerlo cada ciertas iteraciones (cada 15 )
        #        if cambiosCiclos != 0:
        #            if abs(cambiosCiclos) == 0: # Si no hay mucho cambio en 5 generaciones salirse del ciclo porque ya no tiene caso buscar mas soluciones
        #                noHayCambios = 1
        #            cambiosCiclos = 0 # Se reinicia el contador para volver a calcular otras 5 generaciones
        #sol = sBest
        #anterior = fact
        #if(valorAuxRepeticiones == fact):
        #    contadorRepeticiones = contadorRepeticiones + 1
        #else:
        #    contadorRepeticiones = 0
        #if contadorRepeticiones >= noRepetir:
        #    solucion2,datosFIJOS,datosPRIORITARIOS = solucion(datos)
        #    datosPrioritarios = 0
        #    contadorRepeticiones = 0
        #    if evaluar(solucion2,datos) < evaluar(sBest,datos):
        #        sFinal = solucion2
        #    sBest = solucion2
        #valorAuxRepeticiones = fact
        #if evaluar(sBest,datos) < evaluar(sFinal,datos):
        #    sFinal = sBest

        c = c+1
        
  
    t2 = time()
    tiempo = t2 - t1
    #fact = evaluar(sFinal,datos)
    return tiempo,fact,sBest#,tempS
    
