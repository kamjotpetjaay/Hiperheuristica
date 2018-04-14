# -*- coding: utf-8 -*-
"""
Created on Thu Mar 02 09:03:42 2017
by P@b
"""

import data
#from Tabu import busquedaTabu
#from Recocido import recocidoSimulado
#from Genetico import algoritmoGenetico
#from Armonica import busquedaArmonica
from Hiperheuristica import hiperheuristica

#################################################################################
#############################################################################################    
    
def main():
    datos = data.readingFile("metabounds-7.json")
    
    #[tiempo,final,vecMin,Sinicial] = busquedaTabu(datos,150,10,90,20)

    #[tiempo,final,vecMin,Sinicial] = busquedaArmonica(datos,150,20,60,60,25)

    #[tiempo,final,vecMin,Sinicial] = recocidoSimulado(datos,100,25,0.00001,50,20,0.9)
	
    #[tiempo,final,vecMin,Sinicial] = algoritmoGenetico(datos,150,50,60,40,10,60)

    #TIEMPO,FACTIBILIDAD,SOLUCION = hiperheuristica(datos,150,10,90,20)

    tiempo,fmin,sbest = hiperheuristica(datos,3,10,90,20)

main()
