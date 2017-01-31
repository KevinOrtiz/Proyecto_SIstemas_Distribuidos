
import pandas as pd
import numpy as np
import os
import argparse
import sys, glob
sys.path.append('gen-py')
from algoritmos import servicioPartioningMemory
from algoritmos.ttypes import *
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def loadCsv(namefile):
	try:
		file = pd.read_csv(namefile,sep=",")
		return file
	except Exception as e:
		type(e)
		return "error en la carga de los csv"

def getFileCollection(namedirectory):
	try:
		lista = []
		for filename in os.listdir(namedirectory):
			print(filename)
			if filename.endswith("csv"):
				lista.append(loadCsv(namedirectory+filename))
		return lista
	except Exception as e:
		print(type(e))
		return False
	
	

def saveData(directorio,workloadname,dataFrame):
	try:
		dataFrame.to_csv(workloadname + '.csv')
		print("se guardo correctamente el workload:" + workloadname)
		return True
	except Exception as e:
		print(e)
		return False

def createDataFrame(listWorkload,Memory,Latency):
	dicResult = {}
	for x in listWorkload:
		dicResult[x]= pd.Series([Memory,Latency],index=["Memoria","Latencia"])
	df = pd.DataFrame(dicResult)
	return df

if __name__ == '__main__':
	ap = argparse.ArgumentParser()
	ap.add_argument("-host","--host",required=True,help="Direccion ip del servidor")
	ap.add_argument("-ruta","--ruta_directorio", required=True,help="ruta donde se encuentra localizado los workloads")
	ap.add_argument("-save","--ruta_guarda", required=False,help="ruta donde se guardaran los workloads")
	ap.add_argument("-frecuencia","--frecuencia",required=False,help="valor en frecuencia de cada workload")
	ap.add_argument("-bd","--tiempo_hits",required=False,help="Tiempo de los hit en microsegundos")
	ap.add_argument("-cd","--tiempo_miss",required=False,help="Tiempo de los miss en microsegundos")
	ap.add_argument("-w","--pesos_workload",required=False,help="Pesos que se asignan a los workloads")
	ap.add_argument("-M","--total_cache",required=True,help="Tamano total de la cache en GB")
	ap.add_argument("-P","--puerto",required=True,help="puerto donde se encuentra activo el servidor")

	args = vars(ap.parse_args())
	Salir = 1
	try:
		
		if (args["frecuencia"] is None ):
			frecuencia = 0.12221

		else:
			frecuencia = int(args["frecuencia"])

		if (args["tiempo_hits"] is None):
			tiempo_hits = 0.12234

		else:
			tiempo_hits = float(args["tiempo_hits"])

		if (args["tiempo_miss"] is None):
			tiempo_miss = 0.23334
		else:
			tiempo_miss = float(args["tiempo_miss"])

		if (args["pesos_workload"] is None):
			pesos_workload = 21

		else:
			pesos_workload = args["pesos_workload"]

		iMemoryValue = 0
		i = 1

		sizeAcumulateMemory = 0

		print(frecuencia,tiempo_hits,tiempo_miss,pesos_workload,args["host"],int(args["total_cache"]),args["puerto"])

		transport = TSocket.TSocket(args['host'],int(args['puerto']))

		transportBuffering = TTransport.TBufferedTransport(transport)

		protocolBinary = TBinaryProtocol.TBinaryProtocol(transportBuffering)

		client = servicioPartioningMemory.Client(protocolBinary)

		transportBuffering.open()

		listFile = getFileCollection(args["ruta_directorio"])
		if (listFile != False):
			while(Salir != 0):
				print "Usted podra probar dos algoritmos"
				print "1.-Hill climbing simple"
				print "2.-Hill climbing de reinicio aleatorio"
				print "3.-Salir"
				opcionAlgoritmo = raw_input("ingrese las opcion(debe ser numerica)")
				if (opcionAlgoritmo == '1'):
					i = 1
					for x in listFile:
					## aqui va la funcion que manda dos listas ,lista de hit , lista de miss, parametros bd,cd, frecuencia
						listMiss = x['miss'].tolist()
						listCache = x['cache'].tolist()
						valueMemory = client.hillClimbingSimple(listMiss,listCache,frecuencia,int(args['total_cache']),iMemoryValue,sizeAcumulateMemory,tiempo_hits,tiempo_miss)
						iMemoryValue = valueMemory
						sizeAcumulateMemory = sizeAcumulateMemory + valueMemory
						print("********************************************** \n")
						print("workload_" + str(i) + "---> valueMemory:" + str(valueMemory))
						print("\n")
						print("size_Acumulate_Memory------>:" + str(sizeAcumulateMemory))
						print("\n")
						print("*********************************************** \n")	
						i = i + 1		
					'''
					En esta parte de declara el metodo remoto que sera la funcion Hill climbing 
					que tendra como parametro frecuencia,cd,bd,M,m,listaHit,listMiss 
					y retorna el valor de asignacion en memoria cache m{i,1,2,3,4}
					'''

				elif (opcionAlgoritmo == '2'):
					sizeAcumulateMemory = 0
					iMemoryValue = 0
					i = 1
					randomSaltos = raw_input("Ingrese el numero de saltos que desea que realice el algoritmo")
					for x in listFile:
				 		## aqui va la funcion que manda dos listas ,lista de hit , lista de miss, parametros bd,cd, frecuencia
				 		listMiss = x['miss'].tolist()
				 		listCache = x['cache'].tolist()
				 		valueMemory = client.hillClimbingRandom(listMiss,listCache,frecuencia,int(args['total_cache']),iMemoryValue,sizeAcumulateMemory,tiempo_hits,tiempo_miss,int(randomSaltos))
				 		iMemoryValue = valueMemory
				 		sizeAcumulateMemory = sizeAcumulateMemory + valueMemory
					 	print("************************************************ \n")
					 	print("workload_"+ str(i) + "----> valueMemory:" + str(valueMemory))
					 	print("\n")
					 	print("size_Acumulate_Memory--->" + str(sizeAcumulateMemory))
				 		print("\n")
				 		print("************************************************* \n")
				 		i = i + 1

				elif (opcionAlgoritmo == '3'):
					print "Servicio Finalizado"
					Salir = 0
					transportBuffering.close()

				else:
					print "Ingrese una opcion correcta!"
	

	except Thrift.TException, tx:
		print '%s' % (tx.message)