# -*- coding: utf-8 -*-
"""
Created on Wed Jun 07 15:25:03 2017

@author: P@b
"""
import random

#FUNCIÓN PARA GENERAR UNA representación de una SOLUCIÓN (NO FACTIBLE AÚN)
#Retorna una solución con sus datos fijos y prioritarios
def solucion(datos):
    ctrl = 0 #variable para controlar la posición de datos
    mBound = datos["metabounds"] #metabounds
    bound = datos["bounds"] #bounds
    sol = [] #vector solucion
    datosPRIORITARIOS = [] #Vector para obtener los datos con pocos datos de entrada (Bounds de tamaño >1 y menor o igual a 3)
    datosFIJOS = [] #Vector para obtener los metabounds con una sola opción 
    #Empieza a recorrer los metabounds.
    for i in range(len(mBound)):
        size = mBound[i]["size"]
        #Agrega a la solución el primer espacio de teoría(Siempre hay un Et)
        sol.append(random.choice(bound[ctrl]))
        if len(bound[ctrl]) == 1:
            datosFIJOS.append(ctrl)
        if len(bound[ctrl]) > 1 and len(bound[ctrl]) <= 3:
            datosPRIORITARIOS.append(ctrl)
        #Agrega a la solución el espacio de práctica (si es que hay)
        if mBound[i]["gpid"]: #Verifica que haya práctica
            sol.append(random.choice(bound[ctrl+1]))
            if len(bound[ctrl+1]) == 1:
                datosFIJOS.append(ctrl+1)
            if len(bound[ctrl+1]) > 1 and len(bound[ctrl+1]) <=3:
                datosPRIORITARIOS.append(ctrl+1)
        lenlgs = len(mBound[i]["lgs"])
        lgs = mBound[i]["lgs"]
        for j in range(lenlgs):
            if(lgs[j]["hidx"] != -1):
                h = random.choice(bound[ctrl+lgs[j]["hidx"]]) #Se escoge la hora de manera aleatoria.
                if len(bound[ctrl+lgs[j]["hidx"]]) == 1:
                    datosFIJOS.append(ctrl+lgs[j]["hidx"])
                if len(bound[ctrl+lgs[j]["hidx"]]) > 1 and len(bound[ctrl+lgs[j]["hidx"]]) <= 3:
                    datosPRIORITARIOS.append(ctrl+lgs[j]["hidx"])
                sol.append(h)
            if(lgs[j]["pidx"] != -1):
                p = bound[ctrl+lgs[j]["pidx"]]
                if len(p) == 1:
                    datosFIJOS.append(ctrl+lgs[j]["pidx"])
                if len(p) > 1 and len(p) <= 3:
                    datosPRIORITARIOS.append(ctrl+lgs[j]["pidx"])
                sol.append(random.sample(p,len(p)))
        ctrl = ctrl + size  
    return sol,datosFIJOS,datosPRIORITARIOS