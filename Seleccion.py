# -*- coding: utf-8 -*-

"""
##########################################################################
#######################        seleccion y problemas hiperheurística     #################
##########################################################################
##############detecta los problemas para ejecutar la metaheuristica que solucione el problema################
"""

import random
import collections

#Profesor,Espacio,{dia,hora},id, especialidad, lgs 
#   0      1         2       3       4          5
def buscarPosProfesorGrupos(datos,indice):
    contador = 0
    indiceDatos = 0
    for i in datos:
        if i[3] == indice:
            indiceDatos = contador
        contador = contador+1
    return indiceDatos
    


#Función que devuelve un arreglo con la posición de los metabounds
#igualado al tamaño de los bounds
#Por ejemplo: si posicion de Metabound = 3
#encuentra la posición de acuerdo al size de las asignaciones antes de esa posicion
#entonces la posición sería [1,2,3]
#                           [2,4,9] Supongamos que los bounds son de tamaño 2,2,5
def posicion(mBound):
    pos = {}
    ctrl = 0
    for i in range(len(mBound)):
        pos[i] = ctrl
        ctrl = ctrl + mBound[i]["size"]
    return pos

############################################################################################
############################################################################################
############################                               #################################
############################    FUNCION HEURISTICA    #################################
############################                               #################################
############################################################################################
############################################################################################
#Heuristica 1
#Que los profesores tengan un horario continuo de clases. A menos que
#el profesor especifique lo contrario. Y que tengan su horario en las
#horas que ellos prefieran.

def horasContinuasP(profesores):
    listaProfe = []
    listaDias = []
    c10 = []
    idGlobal = []
    #juntamos los días y horas de clase de cada profesor
    for profe in profesores:
        idProfe = profe[0]
        dias = profe[2]
        #Si el profesor aún no está en la lista
        if idProfe not in listaProfe:
            listaProfe.append(idProfe)
            listaDias.append(dias)
            idGlobal.append([profe[3]])
        else:
            #Buscar la posicion e ingresar los dias en la misma posicion
            dictNueva = {}
            dictAux = {}
            horas = []
            indice = listaProfe.index(idProfe)
            dia2 = listaDias[indice]
            for dia in dias:
                if dia2.has_key(dia):
                    horas = dias[dia]+dia2[dia]
                    dictAux[dia] = horas
            for dia in dias:
                dictNueva[dia] = dias[dia]
            for dia in dia2:
                dictNueva[dia] = dia2[dia]
            for dia in dictAux:
                dictNueva[dia] = dictAux[dia]
            
            listaDias[indice] = dictNueva
        
    sumaHorasInvalidas = 0
    for dict1 in listaDias:
        lunes = dict1.get(0)
        martes = dict1.get(1)
        miercoles = dict1.get(2)
        jueves = dict1.get(3)
        viernes = dict1.get(4)     
      
        #SE TOMA EN CUENTA QUE LAS HORAS DISCONTINUAS AFECTAN AL PROFESOR, A EXCEPCIÓN
        #DE QUE TENGAN MAS DE TRES HORAS DE DIFERENCIA ENTRE CADA CLASE
        #POR EJEMPLO SI TIENE CLASE A LAS 8 Y TIENE CLASE HASTA LAS 12, NO HABRÁ PENALIZACIÓN
        #SE PUEDE MODIFICAR ESTOS VALORES EN LA CONDICIÓN if val > 1 and val < 4
        if(lunes):
            lunesOrdenado = sorted(lunes)
            for h in range(len(lunesOrdenado)):
                if h > 0:
                    val = lunesOrdenado[h] - lunesOrdenado[h-1]
                    if val > 1 and val < 4:
                        if lunesOrdenado[h-1] < 14 and lunesOrdenado[h] >= 16:
                            val = val-3
                        sumaHorasInvalidas = sumaHorasInvalidas + val
                        if val > 0:
                            if idGlobal[listaDias.index(dict1)] not in c10:
                                c10.append(idGlobal[listaDias.index(dict1)])
        if(martes):
            martesOrdenado = sorted(martes)
            for h in range(len(martesOrdenado)):
                if h > 0:
                    val = martesOrdenado[h] - martesOrdenado[h-1]
                    if val > 1 and val < 4:
                        if martesOrdenado[h-1] < 14 and martesOrdenado[h] >= 16:
                            val = val-3
                        sumaHorasInvalidas = sumaHorasInvalidas + val
                        if val > 0:
                            if idGlobal[listaDias.index(dict1)] not in c10:
                                c10.append(idGlobal[listaDias.index(dict1)])
        if(miercoles):
            miercolesOrdenado = sorted(miercoles)
            for h in range(len(miercolesOrdenado)):
                if h > 0:
                    val = miercolesOrdenado[h] - miercolesOrdenado[h-1]
                    if val > 1 and val < 4:
                        if miercolesOrdenado[h-1] < 14 and miercolesOrdenado[h] >= 16:
                            val = val-3
                        sumaHorasInvalidas = sumaHorasInvalidas + val
                        if val > 0:
                            if idGlobal[listaDias.index(dict1)] not in c10:
                                c10.append(idGlobal[listaDias.index(dict1)])
        if(jueves):
            juevesOrdenado = sorted(jueves)
            for h in range(len(juevesOrdenado)):
                if h > 0:
                    val = juevesOrdenado[h] - juevesOrdenado[h-1]
                    if val > 1 and val < 4:
                        if juevesOrdenado[h-1] < 14 and juevesOrdenado[h] >= 16:
                            val = val-3
                        sumaHorasInvalidas = sumaHorasInvalidas + val
                        if val > 0:
                            if idGlobal[listaDias.index(dict1)] not in c10:
                                c10.append(idGlobal[listaDias.index(dict1)])
        if(viernes):
            viernesOrdenado = sorted(viernes)
            for h in range(len(viernesOrdenado)):
                if h > 0:
                    val = viernesOrdenado[h] - viernesOrdenado[h-1]
                    if val > 1 and val < 4:
                        if viernesOrdenado[h-1] < 14 and viernesOrdenado[h] >= 16:
                            val = val-3
                        sumaHorasInvalidas = sumaHorasInvalidas + val
                        if val > 0:
                            if idGlobal[listaDias.index(dict1)] not in c10:
                                c10.append(idGlobal[listaDias.index(dict1)])
    return c10,sumaHorasInvalidas
 
#H2   
#Que los alumnos tengan un horario continuo de clases. Pero siempre
#con horas en la tarde y en la mañana.
def horasContinuasA(grupos):
    listaGrupo = []
    listaDias = []
    c11 = []
    idGlobal = []
    #juntamos los días y horas de clase de cada profesor
    for grupo in grupos:
        idGrupo = grupo[0]
        dias = grupo[2]
        #Si el profesor aún no está en la lista
        if idGrupo not in listaGrupo:
            listaGrupo.append(idGrupo)
            listaDias.append(dias)
            idGlobal.append(grupo[3])
        else:
            #Buscar la posicion e ingresar los dias en la misma posicion
            dictNueva = {}
            dictAux = {}
            horas = []
            indice = listaGrupo.index(idGrupo)
            dia2 = listaDias[indice]
            for dia in dias:
                if dia2.has_key(dia):
                    horas = dias[dia]+dia2[dia]
                    dictAux[dia] = horas
            for dia in dias:
                dictNueva[dia] = dias[dia]
            for dia in dia2:
                dictNueva[dia] = dia2[dia]
            for dia in dictAux:
                dictNueva[dia] = dictAux[dia]
            
            listaDias[indice] = dictNueva
        
    sumaHorasInvalidas = 0
    for dict1 in listaDias:
        lunes = dict1.get(0)
        martes = dict1.get(1)
        miercoles = dict1.get(2)
        jueves = dict1.get(3)
        viernes = dict1.get(4)    

        if(lunes):
            if 14 in lunes:
                lunes.remove(14)
            if 15 in lunes:
                lunes.remove(15)
            lunesOrdenado = sorted(lunes)
            for h in range(len(lunesOrdenado)):
                if h > 0:
                    val = lunesOrdenado[h] - lunesOrdenado[h-1]
                      
                    if val > 1 and val < 4:
                        if lunesOrdenado[h-1] < 14 and lunesOrdenado[h] >= 16:
                            val = val-3
                    else:
                        val = 0
                    if h == (len(lunesOrdenado)-1):
                        if lunesOrdenado[h] >= 16:
                            if lunesOrdenado[0] < 14:
                                val
                            else:
                                val = val+1
                        else:
                            val = val+1
                    sumaHorasInvalidas = sumaHorasInvalidas + val
                    if val > 0:
                        if idGlobal[listaDias.index(dict1)] not in c11:
                            c11.append(idGlobal[listaDias.index(dict1)])
            #Se considera que solo se asigna una hora
            if len(lunesOrdenado) == 1:
                sumaHorasInvalidas = sumaHorasInvalidas + 1
                if idGlobal[listaDias.index(dict1)] not in c11:
                    c11.append(idGlobal[listaDias.index(dict1)])

        if(martes):
            if 14 in martes:
                martes.remove(14)
            if 15 in martes:
                martes.remove(15)
            martesOrdenado = sorted(martes)
            for h in range(len(martesOrdenado)):
                if h > 0:
                    val = martesOrdenado[h] - martesOrdenado[h-1]
  
                    if val > 1 and val < 4:
                        if martesOrdenado[h-1] < 14 and martesOrdenado[h] >= 16:
                            val = val-3
                    else:
                        val = 0
                        
                    if h == (len(martesOrdenado)-1):
                        if martesOrdenado[h] >= 16:
                            if martesOrdenado[0] < 14:
                                val
                            else:
                                val = val+1
                        else:
                            val = val+1
                    sumaHorasInvalidas = sumaHorasInvalidas + val
                    if val > 0:
                        if idGlobal[listaDias.index(dict1)] not in c11:
                            c11.append(idGlobal[listaDias.index(dict1)])
            #Se considera que solo se asigna una hora
            if len(martesOrdenado) == 1:
                sumaHorasInvalidas = sumaHorasInvalidas + 1
                if idGlobal[listaDias.index(dict1)] not in c11:
                    c11.append(idGlobal[listaDias.index(dict1)])

        if(miercoles):
            if 14 in miercoles:
                miercoles.remove(14)
            if 15 in miercoles:
                miercoles.remove(15)
            miercolesOrdenado = sorted(miercoles)
            for h in range(len(miercolesOrdenado)):
                if h > 0:
                    val = miercolesOrdenado[h] - miercolesOrdenado[h-1]
                    
                    if val > 1 and val < 4:
                        if miercolesOrdenado[h-1] < 14 and miercolesOrdenado[h] >= 16:
                            val = val-3
                    else:
                        val = 0
                        
                    if h == (len(miercolesOrdenado)-1):
                        if miercolesOrdenado[h] >= 16:
                            if miercolesOrdenado[0] < 14:
                                val
                            else:
                                val = val+1
                        else:
                            val = val+1
                    sumaHorasInvalidas = sumaHorasInvalidas + val
                    if val > 0:
                        if idGlobal[listaDias.index(dict1)] not in c11:
                            c11.append(idGlobal[listaDias.index(dict1)])
            #Se considera que solo se asigna una hora
            if len(miercolesOrdenado) == 1:
                sumaHorasInvalidas = sumaHorasInvalidas + 1
                if idGlobal[listaDias.index(dict1)] not in c11:
                    c11.append(idGlobal[listaDias.index(dict1)])

        if(jueves):
            if 14 in jueves:
                jueves.remove(14)
            if 15 in jueves:
                jueves.remove(15)
            juevesOrdenado = sorted(jueves)
            for h in range(len(juevesOrdenado)):
                if h > 0:
                    val = juevesOrdenado[h] - juevesOrdenado[h-1]
                    
                    if val > 1 and val < 4:
                        if juevesOrdenado[h-1] < 14 and juevesOrdenado[h] >= 16:
                            val = val-3
                    else:
                        val = 0
                        
                    if h == (len(juevesOrdenado)-1):
                        if juevesOrdenado[h] >= 16:
                            if juevesOrdenado[0] < 14:
                                val
                            else:
                                val = val+1
                        else:
                            val = val+1
                    sumaHorasInvalidas = sumaHorasInvalidas + val
                    if val > 0:
                        if idGlobal[listaDias.index(dict1)] not in c11:
                            c11.append(idGlobal[listaDias.index(dict1)])
            #Se considera que solo se asigna una hora
            if len(juevesOrdenado) == 1:
                sumaHorasInvalidas = sumaHorasInvalidas + 1
                if idGlobal[listaDias.index(dict1)] not in c11:
                    c11.append(idGlobal[listaDias.index(dict1)])
        if(viernes):
            if 14 in viernes:
                viernes.remove(14)
            if 15 in viernes:
                viernes.remove(15)
            viernesOrdenado = sorted(viernes)
            for h in range(len(viernesOrdenado)):
                if h > 0:
                    val = viernesOrdenado[h] - viernesOrdenado[h-1]
                    if val > 1 and val < 4:
                        if viernesOrdenado[h-1] < 14 and viernesOrdenado[h] >= 16:
                            val = val-3
                    else:
                        val = 0
                        
                    if h == (len(viernesOrdenado)-1):
                        if viernesOrdenado[h] >= 16:
                            if viernesOrdenado[0] < 14:
                                val
                            else:
                                val = val+1
                        else:
                            val = val+1
                    sumaHorasInvalidas = sumaHorasInvalidas + val
                    if val > 0:
                        if idGlobal[listaDias.index(dict1)] not in c11:
                            c11.append(idGlobal[listaDias.index(dict1)])
            #Se considera que solo se asigna una hora
            if len(viernesOrdenado) == 1:
                sumaHorasInvalidas = sumaHorasInvalidas + 1
                if idGlobal[listaDias.index(dict1)] not in c11:
                    c11.append(idGlobal[listaDias.index(dict1)])
    return c11,sumaHorasInvalidas

#H3
#Que no existan clases de práctica fuera del horario habitual de clases,
#a menos que se especifique directamente en los datos de entrada.


#H4
#Que los profesores impartan las mismas materias que en semestres
#anteriores afines.


#H5
# Que los profesores tengan horarios muy similares, si no es que el
#mismo que en semestres anteriores afines.

#H6
#Que los grupos no tomen clases continuas en lugares demasiado alejados.

#H7
#Que los grupos de diferentes carreras tomen clases en grupos de aulas
#"interdisciplinarios”.

############################################################################################
############################################################################################
############################                               #################################
############################    FUNCION DE FACTIBILIDAD    #################################
############################                               #################################
############################################################################################
############################################################################################

#Factibilidad Global 3
#Un mismo profesor no puede estar en dos lugares diferentes a la vez 
#Profesor,Espacio,{dia,hora},id, especialidad,lgs
#   0      1         2       3        4        5
def compararProfesor3(profesor1,profesor2,datos):   
    sumaRepetidos = 0
    posicionHora  = -1
    mBound = datos["metabounds"]
    #mismo profesor
    if(profesor1[0] == profesor2[0]):
        #diferene espacio
        if(profesor1[1] != profesor2[1]):
            dict1 = profesor1[2]
            dict2 = profesor2[2]
            lunes1 = dict1.get(0)
            lunes2 = dict2.get(0)
            martes1 = dict1.get(1)
            martes2 = dict2.get(1)
            miercoles1 = dict1.get(2)
            miercoles2 = dict2.get(2)
            jueves1 = dict1.get(3)
            jueves2 = dict2.get(3)
            viernes1 = dict1.get(4)
            viernes2 = dict2.get(4)
            if lunes1 and lunes2:
                l = list(set(lunes1))+list(set(lunes2))
                contador = collections.Counter(l)
                for x in contador:
                    sumaRepetidos = sumaRepetidos + (contador[x]-1)
            if martes1 and martes2:
                l = list(set(martes1))+list(set(martes2))
                contador = collections.Counter(l)
                for x in contador:
                    sumaRepetidos = sumaRepetidos + (contador[x]-1)
            if miercoles1 and miercoles2:
                l = list(set(miercoles1))+list(set(miercoles2))
                contador = collections.Counter(l)
                for x in contador:
                    sumaRepetidos = sumaRepetidos + (contador[x]-1)
            if jueves1 and jueves2:
                l = list(set(jueves1))+list(set(jueves2))
                contador = collections.Counter(l)
                for x in contador:
                    sumaRepetidos = sumaRepetidos + (contador[x]-1)
            if viernes1 and viernes2:
                l = list(set(viernes1))+list(set(viernes2))
                contador = collections.Counter(l)
                for x in contador:
                    sumaRepetidos = sumaRepetidos + (contador[x]-1)
    if sumaRepetidos > 0:
        valRandom = random.random()
        if valRandom > 0.5:
            posiciones = posicion(mBound)
            profesorId = profesor1[3]
            lgs = mBound[profesorId]["lgs"] #Se obtiene los lecturers de la asignación n (n = profesorID = posicionMetabounds)
            posicionHora = posiciones[profesorId]+lgs[profesor1[5]]["hidx"] #profesor1[5] es el lecturer actual(la que se envía a comparar)
        else:
            posiciones = posicion(mBound)
            profesorId = profesor2[3] 
            lgs = mBound[profesorId]["lgs"]#Se obtiene los lecturers de la asignación n (n = profesorID = posicionMetabounds)
            posicionHora = posiciones[profesorId]+lgs[profesor2[5]]["hidx"] #profesor1[5] es el lecturer actual(la que se envía a comparar)
    return posicionHora,sumaRepetidos
        

#Factibilidad Global 4
#Dos o mas profesores o grupos no pueden estar en el mismo lugar a la misma
#hora, el mismo día (a menos que sea una multiasignacion)
#Profesor,Espacio,{dia,hora},id, especialidad,lgs
#   0      1         2       3        4        5
#Grupo,Espacio,{dia,hora},id, especialidad,recursamientio,lgs
#   0      1         2       3        4        5            6
def compararProfesorGrupo4(profesor1,profesor2,grupo1,grupo2,datos):  
    sumaRepetidos = 0
    p = -1
    g = -1
    posicionEspacioP = -1 #Espacios profesor
    posicionHoraP  = -1 #Horas profesor
    posicionEspacioG = -1 #Espacios Grupo
    posicionHoraG  = -1 #Horas Grupo
    
    mBound = datos["metabounds"]
    #Verifica que no sea multiasignacion para comparar
    if(profesor1[3] != profesor2[3]):
        #mismo espacio
        if(profesor1[1] == profesor2[1]):
            #diferente profesor
            if(profesor1[0] != profesor2[0]):
                dict1 = profesor1[2]
                dict2 = profesor2[2]
                lunes1 = dict1.get(0)
                lunes2 = dict2.get(0)
                martes1 = dict1.get(1)
                martes2 = dict2.get(1)
                miercoles1 = dict1.get(2)
                miercoles2 = dict2.get(2)
                jueves1 = dict1.get(3)
                jueves2 = dict2.get(3)
                viernes1 = dict1.get(4)
                viernes2 = dict2.get(4)
                if lunes1 and lunes2:
                    l = list(set(lunes1))+list(set(lunes2))
                    contador = collections.Counter(l)
                    for x in contador:
                        sumaRepetidos = sumaRepetidos + (contador[x]-1)
                if martes1 and martes2:
                    l = list(set(martes1))+list(set(martes2))
                    contador = collections.Counter(l)
                    for x in contador:
                        sumaRepetidos = sumaRepetidos + (contador[x]-1)
                if miercoles1 and miercoles2:
                    l = list(set(miercoles1))+list(set(miercoles2))
                    contador = collections.Counter(l)
                    for x in contador:
                        sumaRepetidos = sumaRepetidos + (contador[x]-1)
                if jueves1 and jueves2:
                    l = list(set(jueves1))+list(set(jueves2))
                    contador = collections.Counter(l)
                    for x in contador:
                        sumaRepetidos = sumaRepetidos + (contador[x]-1)
                if viernes1 and viernes2:
                    l = list(set(viernes1))+list(set(viernes2))
                    contador = collections.Counter(l)
                    for x in contador:
                        sumaRepetidos = sumaRepetidos + (contador[x]-1)
    if sumaRepetidos > 0:
        valRandom = random.random() #Random para modificar PROFESOR1 o PROFESOR 2
        valRandom2 = random.random() #Random para modificar ESPACIO u HORA
        #Modificar profesor 1
        if valRandom > 0.5:
            #Modificar espacio
            if valRandom2 > 0.5:
                posiciones = posicion(mBound)
                profesorId = profesor1[3]
                lgs = mBound[profesorId]["lgs"] #Se obtiene los lecturers de la asignación n (n = profesorID = posicionMetabounds)
                #La posicion del espacio depende de la posicion de lgs (numero de lecturer)
                #Por ejemplo si lecturer = 0 entonces la posicion del espacio = 0
                #Si leturer = 1 entonces la posicion del espacio = 1 ....
                posicionEspacioP = posiciones[profesorId]+profesor1[5] #profesor1[5] es el lecturer actual(la que se envía a comparar)
            #Modificar Hora
            else:
                posiciones = posicion(mBound)
                profesorId = profesor1[3]
                lgs = mBound[profesorId]["lgs"] #Se obtiene los lecturers de la asignación n (n = profesorID = posicionMetabounds)
                posicionHoraP = posiciones[profesorId]+lgs[profesor1[5]]["hidx"] #profesor1[5] es el lecturer actual(la que se envía a comparar)
        #Modificar profesor 2
        else:
            #Modificar espacio
            if valRandom2 > 0.5:
                posiciones = posicion(mBound)
                profesorId = profesor2[3] 
                lgs = mBound[profesorId]["lgs"]#Se obtiene los lecturers de la asignación n (n = profesorID = posicionMetabounds)
                #La posicion del espacio depende de la posicion de lgs (numero de lecturer)
                #Por ejemplo si lecturer = 0 entonces la posicion del espacio = 0
                #Si leturer = 1 entonces la posicion del espacio = 1 ....
                posicionEspacioP = posiciones[profesorId]+profesor2[5] #profesor1[5] es el lecturer actual(la que se envía a comparar)
            #Modificar Hora
            else:
                posiciones = posicion(mBound)
                profesorId = profesor2[3] 
                lgs = mBound[profesorId]["lgs"]#Se obtiene los lecturers de la asignación n (n = profesorID = posicionMetabounds)
                posicionHoraP = posiciones[profesorId]+lgs[profesor2[5]]["hidx"] #profesor1[5] es el lecturer actual(la que se envía a comparar)
            
    #Verifica que no sea multiasignacion para comparar
    sumaRepetidosG = 0
    if(grupo1[3] != grupo2[3]):
        #mismo espacio
        if(grupo1[1] == grupo2[1]):
            #diferente grupo
            if(grupo1[0] != grupo2[0]):
                dict1 = grupo1[2]
                dict2 = grupo2[2]
                lunes1 = dict1.get(0)
                lunes2 = dict2.get(0)
                martes1 = dict1.get(1)
                martes2 = dict2.get(1)
                miercoles1 = dict1.get(2)
                miercoles2 = dict2.get(2)
                jueves1 = dict1.get(3)
                jueves2 = dict2.get(3)
                viernes1 = dict1.get(4)
                viernes2 = dict2.get(4)
                if lunes1 and lunes2:
                    l = list(set(lunes1))+list(set(lunes2))
                    contador = collections.Counter(l)
                    for x in contador:
                        sumaRepetidosG = sumaRepetidosG + (contador[x]-1)
                if martes1 and martes2:
                    l = list(set(martes1))+list(set(martes2))
                    contador = collections.Counter(l)
                    for x in contador:
                        sumaRepetidosG = sumaRepetidosG + (contador[x]-1)
                if miercoles1 and miercoles2:
                    l = list(set(miercoles1))+list(set(miercoles2))
                    contador = collections.Counter(l)
                    for x in contador:
                        sumaRepetidosG = sumaRepetidosG + (contador[x]-1)
                if jueves1 and jueves2:
                    l = list(set(jueves1))+list(set(jueves2))
                    contador = collections.Counter(l)
                    for x in contador:
                        sumaRepetidosG = sumaRepetidosG + (contador[x]-1)
                if viernes1 and viernes2:
                    l = list(set(viernes1))+list(set(viernes2))
                    contador = collections.Counter(l)
                    for x in contador:
                        sumaRepetidosG = sumaRepetidosG + (contador[x]-1)
    if sumaRepetidosG > 0:
        valRandom = random.random()
        valRandom2 = random.random() #Random para modificar ESPACIO u HORA
        #Modificar profesor 1
        if valRandom > 0.5:
            #Modificar espacio
            if valRandom2 > 0.5:
                posiciones = posicion(mBound)
                grupoId = grupo1[3]
                #lgs = mBound[grupoId]["lgs"] #Se obtiene los lecturers de la asignación n (n = profesorID = posicionMetabounds)
                #La posicion del espacio depende de la posicion de lgs (numero de lecturer)
                #Por ejemplo si lecturer = 0 entonces la posicion del espacio = 0
                #Si leturer = 1 entonces la posicion del espacio = 1 ....
                posicionEspacioG = posiciones[grupoId]+grupo1[6] #profesor1[5] es el lecturer actual(la que se envía a comparar)
            #Modificar Hora
            else:
                posiciones = posicion(mBound)
                grupoId = grupo1[3]
                lgs = mBound[grupoId]["lgs"] #Se obtiene los lecturers de la asignación n (n = profesorID = posicionMetabounds)
                posicionHoraG = posiciones[grupoId]+lgs[grupo1[6]]["hidx"] #profesor1[5] es el lecturer actual(la que se envía a comparar)
        #Modificar profesor 2
        else:
            #Modificar espacio
            if valRandom2 > 0.5:
                posiciones = posicion(mBound)
                grupoId = grupo2[3] 
                #lgs = mBound[grupoId]["lgs"]#Se obtiene los lecturers de la asignación n (n = profesorID = posicionMetabounds)
                posicionEspacioG = posiciones[grupoId]+grupo2[6] #profesor1[5] es el lecturer actual(la que se envía a comparar)
            #Modificar Hora
            else:
                posiciones = posicion(mBound)
                grupoId = grupo2[3] 
                lgs = mBound[grupoId]["lgs"]#Se obtiene los lecturers de la asignación n (n = profesorID = posicionMetabounds)
                posicionHoraG = posiciones[grupoId]+lgs[grupo2[6]]["hidx"] #profesor1[5] es el lecturer actual(la que se envía a comparar)
    if posicionEspacioP >0:
        p = posicionEspacioP
    if posicionHoraP > 0:
        p = posicionHoraP
    if posicionEspacioG >0:
        g = posicionEspacioG
    if posicionHoraG > 0:
        g = posicionHoraG
    sumaRepetidos = sumaRepetidos + sumaRepetidosG
    return p,g,sumaRepetidos
                        
#Factibilidad global 5
#Un grupo no puede tener asignada otra clase, ya sea en el mismo
#o diferente lugar a la misma hora, el mismo día, a menos que sean
#clases de diferentes especialidades de ese grupo.
#Grupo, Espacio, {dia,hora},id, especialidad
#   0      1         2       3        4
def compararGrupos5(grupo1,grupo2,datos):   
    sumaRepetidos = 0
    posicionHoraG  = -1 #Horas Grupo
    mBound = datos["metabounds"]
    #mismo grupo
    if(grupo1[0] == grupo2[0] and grupo1[3] != grupo2[3]):
        
        #Si no tiene -1 = NULL entonces se pueden comparar ya que tienen una especialidad asignada
        if (grupo1[4] != -1 and grupo2[4] != -1):
            
            #Si son de diferentes especialidades los dos grupos iguales
            if (grupo1[4] != grupo2[4]):
                sumaRepetidos = 0
            else:
            #Si son de la misma especialidad, ver que no se solapen las horas
                dict1 = grupo1[2]
                dict2 = grupo2[2]
                lunes1 = dict1.get(0)
                lunes2 = dict2.get(0)
                martes1 = dict1.get(1)
                martes2 = dict2.get(1)
                miercoles1 = dict1.get(2)
                miercoles2 = dict2.get(2)
                jueves1 = dict1.get(3)
                jueves2 = dict2.get(3)
                viernes1 = dict1.get(4)
                viernes2 = dict2.get(4)
                if lunes1 and lunes2:
                    l = list(set(lunes1))+list(set(lunes2))
                    contador = collections.Counter(l)
                    for x in contador:
                        sumaRepetidos = sumaRepetidos + (contador[x]-1)
                if martes1 and martes2:
                    l = list(set(martes1))+list(set(martes2))
                    contador = collections.Counter(l)
                    for x in contador:
                        sumaRepetidos = sumaRepetidos + (contador[x]-1)
                if miercoles1 and miercoles2:
                    l = list(set(miercoles1))+list(set(miercoles2))
                    contador = collections.Counter(l)
                    for x in contador:
                        sumaRepetidos = sumaRepetidos + (contador[x]-1)
                if jueves1 and jueves2:
                    l = list(set(jueves1))+list(set(jueves2))
                    contador = collections.Counter(l)
                    for x in contador:
                        sumaRepetidos = sumaRepetidos + (contador[x]-1)
                if viernes1 and viernes2:
                    l = list(set(viernes1))+list(set(viernes2))
                    contador = collections.Counter(l)
                    for x in contador:
                        sumaRepetidos = sumaRepetidos + (contador[x]-1)
        else:
            dict1 = grupo1[2]
            dict2 = grupo2[2]
            lunes1 = dict1.get(0)
            lunes2 = dict2.get(0)
            martes1 = dict1.get(1)
            martes2 = dict2.get(1)
            miercoles1 = dict1.get(2)
            miercoles2 = dict2.get(2)
            jueves1 = dict1.get(3)
            jueves2 = dict2.get(3)
            viernes1 = dict1.get(4)
            viernes2 = dict2.get(4)
            if lunes1 and lunes2:
                l = list(set(lunes1))+list(set(lunes2))
                contador = collections.Counter(l)
                for x in contador:
                    sumaRepetidos = sumaRepetidos + (contador[x]-1)
            if martes1 and martes2:
                l = list(set(martes1))+list(set(martes2))
                contador = collections.Counter(l)
                for x in contador:
                    sumaRepetidos = sumaRepetidos + (contador[x]-1)
            if miercoles1 and miercoles2:
                l = list(set(miercoles1))+list(set(miercoles2))
                contador = collections.Counter(l)
                for x in contador:
                    sumaRepetidos = sumaRepetidos + (contador[x]-1)
            if jueves1 and jueves2:
                l = list(set(jueves1))+list(set(jueves2))
                contador = collections.Counter(l)
                for x in contador:
                    sumaRepetidos = sumaRepetidos + (contador[x]-1)
            if viernes1 and viernes2:
                l = list(set(viernes1))+list(set(viernes2))
                contador = collections.Counter(l)
                for x in contador:
                    sumaRepetidos = sumaRepetidos + (contador[x]-1)
    if sumaRepetidos > 0:
        valRandom = random.random()
        if valRandom > 0.5:
            posiciones = posicion(mBound)
            grupoId = grupo1[3]
            lgs = mBound[grupoId]["lgs"] #Se obtiene los lecturers de la asignación n (n = profesorID = posicionMetabounds)
            posicionHoraG = posiciones[grupoId]+lgs[grupo1[6]]["hidx"] #profesor1[5] es el lecturer actual(la que se envía a comparar)
        else:
            posiciones = posicion(mBound)
            grupoId = grupo2[3]
            lgs = mBound[grupoId]["lgs"] #Se obtiene los lecturers de la asignación n (n = profesorID = posicionMetabounds)
            posicionHoraG = posiciones[grupoId]+lgs[grupo2[6]]["hidx"]
    return posicionHoraG,sumaRepetidos
 
                    
#Factibilidad global 6
#Si un profesor da clases a las 8, no puede dar clases a la 1
#Profesor,Espacio,{dia,hora},id, especialidad, lgs 
#   0      1         2       3       4          5
def revisarHoraClase(profesor):   
    listaProfe = []
    listaDias = []
    idGlobal = []
    c6 = []
    
    #juntamos los días y horas de clase de cada profesor
    for profe in profesor:
        idProfe = profe[0]
        dias = profe[2]
        #Si el profesor aún no está en la lista
        if idProfe not in listaProfe:
            listaProfe.append(idProfe)
            listaDias.append(dias)
            idGlobal.append([profe[3]])
        else:
            #Buscar la posicion e ingresar los dias en la misma posicion
            dictNueva = {}
            dictAux = {}
            horas = []
            indice = listaProfe.index(idProfe)
            dia2 = listaDias[indice]
            for dia in dias:
                if dia2.has_key(dia):
                    horas = dias[dia]+dia2[dia]
                    dictAux[dia] = horas
            for dia in dias:
                dictNueva[dia] = dias[dia]
            for dia in dia2:
                dictNueva[dia] = dia2[dia]
            for dia in dictAux:
                dictNueva[dia] = dictAux[dia]
            listaDias[indice] = dictNueva
            
            if type(idGlobal[indice]) is list:
                listaId = set(idGlobal[indice])
            else: 
                listaId = set([idGlobal[indice]])
            if type(profe[3]) is list:
                set2 = set(profe[3])
            else: 
                set2 = set([profe[3]])
            setAux = listaId | set2
            idGlobal[indice] = list(setAux)
    sumaHorasInvalidas = 0
    for dict1 in listaDias:
        lunes = dict1.get(0)
        martes = dict1.get(1)
        miercoles = dict1.get(2)
        jueves = dict1.get(3)
        viernes = dict1.get(4)            
        if(lunes):
            if 8 in lunes and 13 in lunes:
                sumaHorasInvalidas = sumaHorasInvalidas + 1
                if idGlobal[listaDias.index(dict1)] not in c6:
                    c6.append(idGlobal[listaDias.index(dict1)])
        if(martes):
            if 8 in martes and 13 in martes:
                sumaHorasInvalidas = sumaHorasInvalidas + 1
                if idGlobal[listaDias.index(dict1)] not in c6:
                    c6.append(idGlobal[listaDias.index(dict1)])
        if(miercoles):
            if 8 in miercoles and 13 in miercoles:
                sumaHorasInvalidas = sumaHorasInvalidas + 1
                if idGlobal[listaDias.index(dict1)] not in c6:
                    c6.append(idGlobal[listaDias.index(dict1)])
        if(jueves):
            if 8 in jueves and 13 in jueves:
                sumaHorasInvalidas = sumaHorasInvalidas + 1
                if idGlobal[listaDias.index(dict1)] not in c6:
                    c6.append(idGlobal[listaDias.index(dict1)])
        if(viernes):
            if 8 in viernes and 13 in viernes:
                sumaHorasInvalidas = sumaHorasInvalidas + 1
                if idGlobal[listaDias.index(dict1)] not in c6:
                    c6.append(idGlobal[listaDias.index(dict1)])
    return c6,sumaHorasInvalidas
    
#Factibilidad 7
#Un grupo no puede tomar clases obligatorias a la hora en la que un alumno que pertenece
# al mismo grupo deba tomar clases de recursamiento junto a otro grupo.

def recursamiento(grupos):
    sumaRepetidos = 0
    listaGrupos = []
    listaDias = []
    c7 = []
    for grupo in grupos:
        idGrupo = grupo[0]
        dias = grupo[2]
        recursamientos = grupo[5]
        
        
        #Si el grupo aún no está en la lista 
        if idGrupo not in listaGrupos:
            listaGrupos.append(idGrupo)
            listaDias.append(dias)
        else:
            #Buscar la posicion e ingresar los dias en la misma posicion
            dictNueva = {}
            dictAux = {}
            horas = []
            indice = listaGrupos.index(idGrupo)
            dia2 = listaDias[indice]
            for dia in dias:
                if dia2.has_key(dia):
                    horas = dias[dia]+dia2[dia]
                    dictAux[dia] = horas
            for dia in dias:
                dictNueva[dia] = dias[dia]
            for dia in dia2:
                dictNueva[dia] = dia2[dia]
            for dia in dictAux:
                dictNueva[dia] = dictAux[dia]
            listaDias[indice] = dictNueva
            
            
        #RECURSAMIENTOS
        # En esta parte se agregan los mismos días y las mismas horas a los grupos
        #que tengan recursamiento que los días y las horas del grupo con el que van a
        #tener clases, esto para ser comparado que no sea el mismo día y hora de cada grupo
        #NOTA: Solo se compararán a los grupos de recursamiento
        #para no volver a comparar horas y días iguales de la restricción 5
        gruposRecursamientos = []
        if recursamientos != -1:
            for i in range(len(recursamientos)):
                idGrupoRec = recursamientos[i]["grupo_id"]
                gruposRecursamientos.append(idGrupoRec) #lista para compararativa
                #Si el grupo aún no está en la lista 
                if idGrupoRec not in listaGrupos:
                    listaGrupos.append(idGrupoRec)
                    listaDias.append(dias)
                else:
                    #Buscar la posicion e ingresar los dias en la misma posicion
                    dictNueva = {}
                    dictAux = {}
                    horas = []
                    indice = listaGrupos.index(idGrupoRec)
                    dia2 = listaDias[indice]
                    for dia in dias:
                        if dia2.has_key(dia):
                            horas = dias[dia]+dia2[dia]
                            dictAux[dia] = horas
                    for dia in dias:
                        dictNueva[dia] = dias[dia]
                    for dia in dia2:
                        dictNueva[dia] = dia2[dia]
                    for dia in dictAux:
                        dictNueva[dia] = dictAux[dia]
                    
                    listaDias[indice] = dictNueva
        #En esta parte se obtiene el grupo de recursamiento y se compara con la
        #lista de grupos para verificar si existe en esta lista, si existe entonces
        #se obtiene el índice para obtener los días y horas repetidas
        #Esto se hace porque solo se desea comparar grupos con recursamiento.
        for idGrupoRecursamiento in gruposRecursamientos:
            if idGrupoRecursamiento in listaGrupos:
                indice = listaGrupos.index(idGrupoRecursamiento)
                dict1 = listaDias[indice]
                lunes = dict1.get(0)
                martes = dict1.get(1)
                miercoles = dict1.get(2)
                jueves = dict1.get(3)
                viernes = dict1.get(4)
                if lunes:
                    contador = collections.Counter(lunes)
                    for x in contador:
                        sumaRepetidos = sumaRepetidos + (contador[x]-1)
                if martes:
                    contador = collections.Counter(martes)
                    for x in contador:
                        sumaRepetidos = sumaRepetidos + (contador[x]-1)
                if miercoles:
                    contador = collections.Counter(miercoles)
                    for x in contador:
                        sumaRepetidos = sumaRepetidos + (contador[x]-1)
                if jueves:
                    contador = collections.Counter(jueves)
                    for x in contador:
                        sumaRepetidos = sumaRepetidos + (contador[x]-1)
                if viernes:
                    contador = collections.Counter(viernes)
                    for x in contador:
                        sumaRepetidos = sumaRepetidos + (contador[x]-1)
    return sumaRepetidos

#Factibilidad Global 8
#Un grupo debe tener dos horas libres al día para que en alguna de ellas 
#se le pueda asignar clases de inglés.
def horaLibre(grupos):
    listaGrupos = []
    listaDias = []
    idGlobal = []
    c8 = []
    #juntamos los días y horas de clase de cada grupo
    for grupo in grupos:
        idGrupo = grupo[0]
        dias = grupo[2]
        #Si el grupo aún no está en la lista
        if idGrupo not in listaGrupos:
            listaGrupos.append(idGrupo)
            listaDias.append(dias)
            idGlobal.append(grupo[3])
        else:
            #Buscar la posicion e ingresar los dias en la misma posicion
            dictNueva = {}
            dictAux = {}
            horas = []
            indice = listaGrupos.index(idGrupo)
            dia2 = listaDias[indice]
            for dia in dias:
                if dia2.has_key(dia):
                    horas = dias[dia]+dia2[dia]
                    dictAux[dia] = horas
            for dia in dias:
                dictNueva[dia] = dias[dia]
            for dia in dia2:
                dictNueva[dia] = dia2[dia]
            for dia in dictAux:
                dictNueva[dia] = dictAux[dia]
            
            listaDias[indice] = dictNueva
            
            if type(idGlobal[indice]) is list:
                listaId = set(idGlobal[indice])
            else: 
                listaId = set([idGlobal[indice]])
            if type(grupo[3]) is list:
                set2 = set(grupo[3])
            else: 
                set2 = set([grupo[3]])
            setAux = listaId | set2
            idGlobal[indice] = list(setAux)
        
    sumaHorasInvalidas = 0
    for dict1 in listaDias:
        lunes = dict1.get(0)
        martes = dict1.get(1)
        miercoles = dict1.get(2)
        jueves = dict1.get(3)
        viernes = dict1.get(4)
        horasLaborales = [8,9,10,11,12,1,16,17,18]     

        if(lunes):
            lunes = list(set(lunes))
            count = 0
            for horaLaboral in horasLaborales:
                if horaLaboral not in lunes:
                    count = count +1
            if count >= 2:
                sumaHorasInvalidas = sumaHorasInvalidas
            else:
                sumaHorasInvalidas = sumaHorasInvalidas + 1
                if idGlobal[listaDias.index(dict1)] not in c8:
                    c8.append(idGlobal[listaDias.index(dict1)])
        if(martes):
            martes = list(set(martes))
            count = 0
            for horaLaboral in horasLaborales:
                if horaLaboral not in martes:
                    count = count +1
            if count >= 2:
                sumaHorasInvalidas = sumaHorasInvalidas
            else:
                sumaHorasInvalidas = sumaHorasInvalidas + 1
                if idGlobal[listaDias.index(dict1)] not in c8:
                    c8.append(idGlobal[listaDias.index(dict1)])
        if(miercoles):
            miercoles = list(set(miercoles))
            count = 0
            for horaLaboral in horasLaborales:
                if horaLaboral not in miercoles:
                    count = count +1
            if count >= 2:
                sumaHorasInvalidas = sumaHorasInvalidas
            else:
                sumaHorasInvalidas = sumaHorasInvalidas + 1
                if idGlobal[listaDias.index(dict1)] not in c8:
                    c8.append(idGlobal[listaDias.index(dict1)])
        if(jueves):
            jueves = list(set(jueves))
            count = 0
            for horaLaboral in horasLaborales:
                if horaLaboral not in jueves:
                    count = count +1
            if count >= 2:
                sumaHorasInvalidas = sumaHorasInvalidas
            else:
                sumaHorasInvalidas = sumaHorasInvalidas + 1
                if idGlobal[listaDias.index(dict1)] not in c8:
                    c8.append(idGlobal[listaDias.index(dict1)])
        if(viernes):
            viernes = list(set(viernes))
            count = 0
            for horaLaboral in horasLaborales:
                if horaLaboral not in viernes:
                    count = count +1
            if count >= 2:
                sumaHorasInvalidas = sumaHorasInvalidas
            else:
                sumaHorasInvalidas = sumaHorasInvalidas + 1
                if idGlobal[listaDias.index(dict1)] not in c8:
                    c8.append(idGlobal[listaDias.index(dict1)])
    return c8,sumaHorasInvalidas

#Factibilidad global 9
#Un espacio solo puede permitir 9 horas al día, ya sea del mismo o diferentes grupos
def espacios(grupos):
    listaEspacios = []
    listaDias = []
    c9 = []
    idGlobal = []
    #juntamos los días y horas de clase de cada grupo
    for grupo in grupos:
        idEspacio = grupo[1]
        dias = grupo[2]
        #Si el espacio aún no está en la lista
        if idEspacio not in listaEspacios:
            listaEspacios.append(idEspacio)
            listaDias.append(dias)
            idGlobal.append(grupo[3])
        else:
            #Buscar la posicion e ingresar los dias en la misma posicion
            dictNueva = {}
            dictAux = {}
            horas = []
            indice = listaEspacios.index(idEspacio)
            dia2 = listaDias[indice]

            #Este for para juntar dos días "iguales"
            #por ejemplo lunes: 8,9 y lunes2 11,12
            #al final dictAux tiene 8,9,11,12
            for dia in dias:
                if dia2.has_key(dia):
                    horas = dias[dia]+dia2[dia]
                    dictAux[dia] = horas
            #Estos for's para los días que no se repiten (no son iguales)
            #por ejemplo el primero tiene lunes y viernes
            #el segundo tiene jueves y viernes
            #entonces los dos fors hacen que lunes y jueves se agreguen al nuevo diccionario
            for dia in dias:
                dictNueva[dia] = dias[dia]
            for dia in dia2:
                dictNueva[dia] = dia2[dia]
            for dia in dictAux:
                dictNueva[dia] = dictAux[dia]
            #Se asigna a la nueva lista la suma de ambos horarios de un mismo espacio
            listaDias[indice] = dictNueva
            
            if type(idGlobal[indice]) is list:
                listaId = set(idGlobal[indice])
            else: 
                listaId = set([idGlobal[indice]])
            if type(grupo[3]) is list:
                set2 = set(grupo[3])
            else: 
                set2 = set([grupo[3]])
            setAux = listaId | set2
            idGlobal[indice] = list(setAux)
    sumaHorasInvalidas = 0
    for dict1 in listaDias:
        lunes = dict1.get(0)
        martes = dict1.get(1)
        miercoles = dict1.get(2)
        jueves = dict1.get(3)
        viernes = dict1.get(4)   
        if(lunes):
            if len(lunes) >= 9:
                sumaHorasInvalidas = sumaHorasInvalidas + 1
                if idGlobal[listaDias.index(dict1)] not in c9:
                    c9.append(idGlobal[listaDias.index(dict1)])
        if(martes):
            if len(martes) >= 9:
                sumaHorasInvalidas = sumaHorasInvalidas + 1
                if idGlobal[listaDias.index(dict1)] not in c9:
                    c9.append(idGlobal[listaDias.index(dict1)])
        if(miercoles):
            if len(miercoles) >= 9:
                sumaHorasInvalidas = sumaHorasInvalidas + 1
                if idGlobal[listaDias.index(dict1)] not in c9:
                    c9.append(idGlobal[listaDias.index(dict1)])
        if(jueves):
            if len(jueves) >= 9:
                sumaHorasInvalidas = sumaHorasInvalidas + 1
                if idGlobal[listaDias.index(dict1)] not in c9:
                    c9.append(idGlobal[listaDias.index(dict1)])
        if(viernes):
            if len(viernes) >= 9:
                sumaHorasInvalidas = sumaHorasInvalidas + 1
                if idGlobal[listaDias.index(dict1)] not in c9:
                    c9.append(idGlobal[listaDias.index(dict1)])
    return c9,sumaHorasInvalidas

#Función que devuelve el valor de la función de factibilidad global(5-9)
def globalFactibilidad(solucion,datos,datosProfesor,datosGrupos):
    c3 = []
    c4 = []
    c42 = []
    c5 = []

    fact3 = fact4 = fact5 = fact6 = fact7 = fact8 = fact9=0
    #3.Un profesor no puede estar asignado a dos lugares(espacios) al mismo tiempo(día y hora)    
    for i in range((len(datosProfesor))-2):
        for j in range (i+1,(len(datosProfesor)-1)):
            pos,tempVal = compararProfesor3(datosProfesor[i],datosProfesor[j],datos)
            fact3 = fact3 + tempVal
            if pos >= 0:
                c3.append(pos)
            
            pos,pos2,tempVal = compararProfesorGrupo4(datosProfesor[i],datosProfesor[j],datosGrupos[i],datosGrupos[j],datos)
            fact4 = fact4 + tempVal
            if pos >= 0:
                c4.append(pos)
            if pos2 >= 0:
                c42.append(pos2)
             
            pos,tempVal = compararGrupos5(datosGrupos[i],datosGrupos[j],datos)
            fact5 = fact5 + tempVal
            if pos >= 0:
                c5.append(pos)
    c6,tempVal = revisarHoraClase(datosProfesor)
    fact6 = fact6 + tempVal
    c6Aux = []
    for m in c6:
        for l in m:
            c6Aux.append(l)
    c6 = c6Aux
    
    mBound = datos["metabounds"]
    posiciones = posicion(mBound)
    c6Aux = []
    
    for i in c6:
        profesorId = i
        lgs = mBound[profesorId]["lgs"] #Se obtiene los lecturers de la asignación n (n = profesorID = posicionMetabounds)
        indice = buscarPosProfesorGrupos(datosProfesor,profesorId)
        profesor = datosProfesor[indice]
        posicionHora = posiciones[profesorId]+lgs[profesor[5]]["hidx"] 
        c6Aux.append(posicionHora)
    c6 = c6Aux
    
    #La factibilidad de recursamiento aún no se toma en cuenta porque no se tienen datos completos
    #fact7 = fact7 + recursamiento(datosGrupos)
    c8,tempVal = horaLibre(datosGrupos)
    fact8 = fact8 + tempVal
    c8Aux = []
    for m in c8:
        for l in m:
            c8Aux.append(l)
    c8 = c8Aux
    
    c8Aux = []
    for i in c8:
        grupoId = i
        lgs = mBound[grupoId]["lgs"] #Se obtiene los lecturers de la asignación n (n = profesorID = posicionMetabounds)
        indice = buscarPosProfesorGrupos(datosGrupos,grupoId)
        grupo = datosGrupos[indice]
        if lgs[grupo[6]]["pidx"] >0:  
            posicionDia = posiciones[grupoId]+lgs[grupo[6]]["pidx"] 
            c8Aux.append(posicionDia)
    c8 = c8Aux
    
    c9,tempVal = espacios(datosGrupos)
    c9Aux = []
    for m in c9:
        for l in m:
            c9Aux.append(l)
    c9 = c9Aux
    
    c9Aux = []
    for i in c9:
        grupoId = i
        lgs = mBound[grupoId]["lgs"] #Se obtiene los lecturers de la asignación n (n = profesorID = posicionMetabounds)
        indice = buscarPosProfesorGrupos(datosGrupos,grupoId)
        grupo = datosGrupos[indice]
        if lgs[grupo[6]]["pidx"] >0:  
            posicionDia = posiciones[grupoId]+lgs[grupo[6]]["pidx"] 
            c9Aux.append(posicionDia)
    c9 = c9Aux
    fact9 = fact9 + tempVal
    return c3,c4,c42,c5,c6,[],c8,c9,fact3,fact4,fact5,fact6,fact7,fact8,fact9
    
############################################################################################################################
############################################################################################################################
    
#función de factibilidad (Hard Constraints)
def seleccionar(solucion,datos):
    mBound = datos["metabounds"] #metabounds
    ctrl = 0 #variable para la posición de datos
    ##################VARIABLES PARA LA SUMATORIA DE LA FUNCIÓN DE FACTIBILIDAD)############
    funcFact = 0 #Función de factibilidad GLOBAL Y TOTAL
    fact1 = 0 # Costo de las restricciones individuales 1,2 y 3 (Hard Constraint)
    #Se le da mas peso porque abarca tres restricciones
    peso1 = 5 #Peso de las resticciones individuales 1,2 y 3 (Se multiplica por el costo)
    fact2 = 0
    peso2 = 5
    fact3 = 0
    peso3 = 5
    fact4 = 0
    #Se le da menos peso porque pueden haber errores de captura y se pasen las horas de clase
    peso4 = 5
    fact5 = 0
    peso5 = 5
    fact6 = 0
    peso6 = 5
    fact7 = 0
    peso7 = 5
    fact8 = 0
    peso8 = 5    
    fact9 = 0
    peso9 = 5
    heu1 = 0
    pesoH1 = 5
    heu2 = 0
    pesoH2 = 5
    listaGlobalProfesorEspacio = []
    listaGlobalGrupoEspacio = []
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    c5 = []
    c6 = []
    c7 = []
    c8 = []
    c9 = []
    h1 = []
    h2 = []
    
    #######################################################################################
    for i in range(len(mBound)):
        idAsignacionGlobal = i
        size = mBound[i]["size"]
        asignaciones = mBound[i]["assignments"]
        recursamientos = mBound[i]["recursamientos"]
        
        dictDias = {} #Para ir guardando horas repetidas de cada dìa, segùn sea el caso
        dictDiasAux = {} #Para ir guardando horas repetidas de cada dìa, segùn sea el caso
        #Los días son del 0-4 (Lunes-Viernes)
        #cada lgs puede tener una,dos o más clases de teoría, y cero,una o más clases de práctica
        lenlgs = len(mBound[i]["lgs"])
        lgs = mBound[i]["lgs"]
        #Solo hacerlo en caso de que haya más de 1 lgs, caso contrario no se debe solapar.
        fueraDeHorariolgs = 0
        colision2 = 0
        teacherList = []
        groupList = []
        specialtyList = []
        listaTemporal = []
        #recursamientosList = []
        if(mBound[i]["mid"]): #multiasignación
            for x in range(len(asignaciones)):
                if (asignaciones[x]["teacher"] not in teacherList):
                    teacherList.append(asignaciones[x]["teacher"])
                if (asignaciones[x]["group"] not in groupList):
                    groupList.append(asignaciones[x]["group"])
                #if (asignaciones[x]["specialty"] not in specialtyList): 
                if(asignaciones[x]["specialty"] == None):
                    specialtyList.append(-1)
                else:
                    specialtyList.append(asignaciones[x]["specialty"])
                #if (asignaciones[x]["recursamientos"] not in groupList):
                #    recursamientosList.append(asignaciones[x]["group"])
        else:
            teacherList.append(asignaciones[0]["teacher"])
            groupList.append(asignaciones[0]["group"])
            if(asignaciones[0]["specialty"] == None):
                specialtyList.append(-1)
            else:
                specialtyList.append(asignaciones[0]["specialty"])
        posicionHORAS = []
        for j in range(lenlgs):
            lect = lgs[j]["lectures"]
                
            if(lgs[j]["hidx"] != -1):
                hora = solucion[ctrl+lgs[j]["hidx"]]
                posicionHORAS.append(ctrl+lgs[j]["hidx"])
            if(lgs[j]["pidx"] != -1):
                diaVect = solucion[ctrl+lgs[j]["pidx"]]
            else:
                diaVect = lgs[j]["days"]            
            
#########################################################
####################################################
            #EN Esta parte se guardan datos globales
            inicial = 0#variable temporal para obtener del array de días los días correctos.
            
            espacio = solucion[ctrl+j]                    
            if len(lect) > 1:
                dictDiasAux = {}
                #por cada lecture
                for m in range(len(lect)):
                    horas = []
                    rango = lect[m]["n"]
                    final = inicial+rango
                    diasChar = diaVect[inicial:final]
                    #Sacar las horas de clase al día a partir de duración y hora
                    for x in range(lect[m]["d"]):
                        horas.append(hora+x)
                    for x in range(len(diasChar)):
                        dictDiasAux[diasChar[x]] = horas
                    inicial = final
                    
                    #En esta parte se hace una lista de profesor,espacio,dia,hora,id_clase
            else:
                horas = []
                #Sacar las horas de clase al día a partir de duración y hora       
                for x in range(lect[0]["d"]):
                    horas.append(hora+x)
                val = 0
                for x in range(lect[0]["n"]):
                    if dictDiasAux.has_key(diaVect[x]) and val == 0:
                        horas.extend(dictDiasAux[diaVect[x]])
                        val = 1
                    dictDiasAux[diaVect[x]] = horas
                    
            for i in range(len(teacherList)):
                listaTemporal.append(teacherList[i])
                listaTemporal.append(espacio)
                listaTemporal.append(dictDiasAux)
                listaTemporal.append(idAsignacionGlobal)
                listaTemporal.append(specialtyList[i])
                listaTemporal.append(j) #Número de lgs o de asignación para obtener posiciones
                listaGlobalProfesorEspacio.append(listaTemporal)
                listaTemporal = []
            for i in range(len(groupList)):
                listaTemporal.append(groupList[i])
                listaTemporal.append(espacio)
                listaTemporal.append(dictDiasAux)
                listaTemporal.append(idAsignacionGlobal)
                listaTemporal.append(specialtyList[i])
                if recursamientos == []:
                    recursamientos = -1
                listaTemporal.append(recursamientos)
                listaTemporal.append(j) #Número de lgs o de asignación para obtener posiciones
                listaGlobalGrupoEspacio.append(listaTemporal)
                listaTemporal = []
            dictDiasAux = {}
########################################################
                
            #Factibilidad Individual (1-5 anterior, ahora 1 y 2)
            #Las restricciones 1 y 2 se consideran en la 3ra
            #porque se cersiora para todas las clases tanto de teoría y práctica.
            #.-Las clases de Teoría no deben ser el mismo día, a la misma hora
            #.-Las clases de Práctica no deben ser el mismo día, a la misma hora
            #1.-Las clases de Teoría y Práctica no deben ser el mismo día, a la misma hora
                
            if(lenlgs > 1):
                #Si hay más de una lecture, verificar los días y horas en que se van a tomar separadamente
                #dependiendo de la hora de inicio tomar las demás horas dentro de la duración.
                inicial = 0#variable temporal para obtener del array de días los días correctos.
                if len(lect) > 1:
                    #por cada lecture
                    for m in range(len(lect)):
                        horas = []
                        rango = lect[m]["n"]
                        final = inicial+rango

                        diasChar = diaVect[inicial:final]
                        #Sacar las horas de clase al día a partir de duración y hora
                        for x in range(lect[m]["d"]):
                            horas.append(hora+x)
                            #EJEMPLO
                            #si la hora es 9 y duración es 2 entonces:
                            #las horas que no pueden repetirse son 9 y 10 (hora de inicio clases asignadas)
                        for x in range(len(diasChar)):
                            dictDias[diasChar[x]] = horas
                        inicial = final
                    #print dictDias
                else:
                    horas = []
                    #Sacar las horas de clase al día a partir de duración y hora       
                    for x in range(lect[0]["d"]):
                        horas.append(hora+x)
                    val = 0
                    for x in range(lect[0]["n"]):
                        if dictDias.has_key(diaVect[x]) and val == 0:
                            horas.extend(dictDias[diaVect[x]])
                            val = 1
                        dictDias[diaVect[x]] = horas
            
            #2.-Las clases no deben impartirse fuera del horario de clase.
            fueraDeHorario = 0 #variable para contabilizar horas fuera de horario
            if len(lect) > 1:
                inicial = 0
                #por cada lecture
                for m in range(len(lect)):
                    rango = lect[m]["n"]
                    final = inicial+rango
                    diasChar = diaVect[inicial:final]
                    #Sacar las horas de clase al día a partir de duración y hora
                    for x in range(lect[m]["d"]):
                        if ((hora+x) >=14 and (hora+x) <16) or ((hora+x) >= 19):
                            fueraDeHorario = fueraDeHorario + 1
                    inicial = final
            else:
                #Sacar las horas de clase al día a partir de duración y hora       
                for x in range(lect[0]["d"]):
                    if ((hora+x) >=14 and (hora+x) <16) or ((hora+x) >= 19):
                        fueraDeHorario = fueraDeHorario + 1
            colision2 = fueraDeHorario
            fueraDeHorariolgs = fueraDeHorariolgs + fueraDeHorario            
        #SE REALIZA LA SUMA DE LOS VALORES REPETIDOS DE LAS RESTRICCIONES 1,2 Y 3               
        sumaRepetidos = 0
        colision1 = 0
                
        for dia in dictDias:
            contador = collections.Counter(dictDias[dia]) 
            for x in contador:
                sumaRepetidos = sumaRepetidos + (contador[x]-1)
                colision1 = colision1 + (contador[x]-1)
        if colision1 > 0:
            c1.append(posicionHORAS)
            
        colision1 = 0
        
        if colision2 > 0:
            c2.append(posicionHORAS)
        colision2 = 0
        #Se le agrega a la función de factibilidad Global el número de 
        fact1 = fact1 + sumaRepetidos
        fact2 = fact2 + fueraDeHorariolgs

        
        ctrl = ctrl + size   #Incrementar posición de control para ir al siguiente MetaBound
    #Restricciones locales
    #Acá se van a sumar todas las restricciones multiplicado por sus pesos
    c1Aux = []
    for m in c1:
        for l in m:
            c1Aux.append(l)
    c1 = c1Aux
    c2Aux = []
    for m in c2:
        for l in m:
            c2Aux.append(l)
    c2 = c2Aux

    #Se manda a llamar otra función que calcula las factibilidades globales
    c3,c4,c42,c5,c6,c7,c8,c9,fact3,fact4,fact5,fact6,fact7,fact8,fact9 = globalFactibilidad(solucion,datos,listaGlobalProfesorEspacio,listaGlobalGrupoEspacio)
    #En esta parte se eliminan elementos repetidos de las posiciones a modificar para que nose modifiquen dos o mas veces,
    #ya que se puede volver a reelegir un valor malo de una asignación.
    c1 = list(set(c1))
    c2 = list(set(c2))
    c3 = list(set(c3))
    c4 = list(set(c4)) #ESPACIO
    c5 = list(set(c5))
    c6 = list(set(c6))
    c8 = list(set(c8))
    c9 = list(set(c9))
    c42 = list(set(c42)) #GRUPO

    #En esta parte se suman las restricciones débiles, multiplicado por sus pesos    
    c10,heu1 = horasContinuasP(listaGlobalProfesorEspacio)
    c11,heu2 = horasContinuasA(listaGlobalGrupoEspacio)
    c10Aux = []
    for m in c10:
        for l in m:
            c10Aux.append(l)
    c10 = c10Aux
    posiciones = posicion(mBound)
    c10Aux = []
    for i in c10:
        profesorId = i
        lgs = mBound[profesorId]["lgs"] #Se obtiene los lecturers de la asignación n (n = profesorID = posicionMetabounds)
        indice = buscarPosProfesorGrupos(listaGlobalProfesorEspacio,profesorId)
        profesor = listaGlobalProfesorEspacio[indice]
        posicionHora = posiciones[profesorId]+lgs[profesor[5]]["hidx"] 
        c10Aux.append(posicionHora)
    c10 = c10Aux
    posiciones = posicion(mBound)
    c11Aux = []
    for i in c11:
        grupoId = i
        lgs = mBound[grupoId]["lgs"] #Se obtiene los lecturers de la asignación n (n = profesorID = posicionMetabounds)
        indice = buscarPosProfesorGrupos(listaGlobalGrupoEspacio,grupoId)
        grupo = listaGlobalGrupoEspacio[indice]
        posicionHora = posiciones[grupoId]+lgs[grupo[6]]["hidx"] 
        c11Aux.append(posicionHora)
    c11 = c11Aux
    c10 = list(set(c10))
    c11 = list(set(c11))
    listaPos = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c42]
    listaFact = [fact1,fact2,fact3,fact4,fact5,fact6,fact7,fact8,fact9,heu1,heu2]
    
    funcFact = funcFact + heu1 + heu2
    return listaPos,listaFact