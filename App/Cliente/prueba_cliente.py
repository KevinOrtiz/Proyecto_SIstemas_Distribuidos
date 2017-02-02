
import pandas as pd
import numpy as np
import os
import argparse
import time
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
	file = open(args["ruta_guarda"],"w+")
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

		print(frecuencia,tiempo_hits,tiempo_miss,pesos_workload,args["host"],float(args["total_cache"]),args["puerto"])

		transport = TSocket.TSocket(args['host'],int(args['puerto']))

		transportBuffering = TTransport.TBufferedTransport(transport)

		protocolBinary = TBinaryProtocol.TBinaryProtocol(transportBuffering)

		client = servicioPartioningMemory.Client(protocolBinary)

		transportBuffering.open()

		listFile = getFileCollection(args["ruta_directorio"])
		if (listFile != False):
				iMemoryValue = 0
				sizeAcumulateMemory = 0
				sizeAcumulateMemory1 = 0
				iMemoryValue1 = 0
				i = 1
				j = 1
				for x in listFile:
					## aqui va la funcion que manda dos listas ,lista de hit , lista de miss, parametros bd,cd, frecuencia
					listMiss = x['miss'].tolist()
					listCache = x['cache'].tolist()
					startLatency_simple = time.time()
					valueMemory = client.hillClimbingSimple(listMiss,listCache,frecuencia,float(args['total_cache']),iMemoryValue,sizeAcumulateMemory,tiempo_hits,tiempo_miss)
					endLatency_simple = time.time()
					if valueMemory == 0:
						valueMemory = float(args['total_cache']) - sizeAcumulateMemory
					iMemoryValue = valueMemory
					sizeAcumulateMemory = sizeAcumulateMemory + valueMemory
					valueTimeHillClimbingSimple = -startLatency_simple + endLatency_simple
					print("*******************HILL CLIMBING SIMPLE **************************** \n")
				 	print("workload_"+ str(i) + "----> valueMemory:" + str(valueMemory))
				 	print("\n")
				 	print("size_Acumulate_Memory--->" + str(sizeAcumulateMemory))
			 		print("\n")
			 		print("Tiempo de Hill climbing Simple = " + str(valueTimeHillClimbingSimple))
			 		print("************************************************* \n")
			 		file.write(" " +  str(valueTimeHillClimbingSimple) + "  " + "hs" + "\n")
			 		i = i + 1
				randomSaltos = 5
				for y in listFile:	 		
			 		listMiss1 = y['miss'].tolist()
			 		listCache1 = y['cache'].tolist()
			 		startLatency_random = time.time()
			 		valueMemory1 = client.hillClimbingRandom(listMiss1,listCache1,frecuencia,float(args['total_cache']),iMemoryValue1,sizeAcumulateMemory1,tiempo_hits,tiempo_miss,int(randomSaltos))
			 		endLatency_random = time.time()
			 		if valueMemory1== 0:
			 			valueMemory1 = float(args['total_cache'])-sizeAcumulateMemory1
			 		iMemoryValue1 = valueMemory1
			 		sizeAcumulateMemory1 = sizeAcumulateMemory1 + valueMemory1
			 		valueTimeHillClimbingRandom = -startLatency_random + endLatency_random
				 	print("********************HILL CLIMBING RANDOM ********************** \n")
				 	print("workload_"+ str(j) + "----> valueMemory:" + str(valueMemory1))
				 	print("\n")
				 	print("size_Acumulate_Memory--->" + str(sizeAcumulateMemory1))
			 		print("\n")
			 		print("Tiempo de Hill Climbing Random = " + str(valueTimeHillClimbingRandom))
			 		print("************************************************* \n")
			 		file.write(" " +  str(valueTimeHillClimbingRandom) + "  " + "hR" + "\n")
			 		
			 		j = j + 1
				print "Servicio Finalizado"
				transportBuffering.close()


	except Thrift.TException, tx:
		print '%s' % (tx.message)