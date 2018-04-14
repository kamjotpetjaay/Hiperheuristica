# -*- coding: utf-8 -*-

""" 
Funciones de lectura de archivo y obtencion de datos principales
Autor: Lluvia Morales
Fecha: Enero de 2017
"""

import json

def readingFile(fname):
	data_file 	=  open(fname,"r")
	jdata 		=  json.load(data_file)
	data_file.close()
	return jdata

def obtainingData(jdata):
	metabounds 	=  jdata["metabounds"]
	bounds		=  jdata["bounds"]

def indivOutput(fname, n, p, t, f, s):
	#En teoria deberia de guardarse
	#	- El algoritmo, nombre
	#	- La combinacion de parametros
	#	- El tiempo de ejecucion
	#	- La funcion de Factibilidad
	#	- La solucion
	try:
		data_file	=	open(fname,"w")
		data_file.read()
	except IOError:
		data_file = open(fname, "w")

		
	data_file.write(n + '\n')
	data_file.write("Combinacion de parametros: " + p + '\n')
	data_file.write("Tiempo de ejecucion: " + t + '\n')
	data_file.write("Funcion de factibilidad: " + f + '\n')
	data_file.write("Mejor solucion: " + s + '\n' + '\n')
	data_file.close()




#def genOutput():
	#En teoria deberia de guardarse:
	#	- El algoritmo
	#	- La combinacion de parametros
	#	- El menor, mayor y promedio de tiempo de ejecucion
	#	- La menor, mayor y promedio de funcion de factibilidad
	#	- La mejor solucion de las 50 ejecuciones del algoritmo 
