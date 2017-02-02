from threading import Thread
import os

t1 = Thread(target=os.system('python prueba_cliente.py --host localhost --ruta_directorio /home/kevin/Documentos/Proyecto_Distribuidos/dataset/ --ruta_guarda /home/kevin/Documentos/Proyecto_Distribuidos/Resultados/cliente_5_1.txt --total_cache 2 --puerto 8585'))
t2 = Thread(target=os.system('python prueba_cliente.py --host localhost --ruta_directorio /home/kevin/Documentos/Proyecto_Distribuidos/dataset/ --ruta_guarda /home/kevin/Documentos/Proyecto_Distribuidos/Resultados/cliente_5_2.txt --total_cache 2 --puerto 8585'))
t3 = Thread(target=os.system('python prueba_cliente.py --host localhost --ruta_directorio /home/kevin/Documentos/Proyecto_Distribuidos/dataset/ --ruta_guarda /home/kevin/Documentos/Proyecto_Distribuidos/Resultados/cliente_5_3.txt --total_cache 2 --puerto 8585'))
t4 = Thread(target=os.system('python prueba_cliente.py --host localhost --ruta_directorio /home/kevin/Documentos/Proyecto_Distribuidos/dataset/ --ruta_guarda /home/kevin/Documentos/Proyecto_Distribuidos/Resultados/cliente_5_4.txt --total_cache 2 --puerto 8585'))
t5 = Thread(target=os.system('python prueba_cliente.py --host localhost --ruta_directorio /home/kevin/Documentos/Proyecto_Distribuidos/dataset/ --ruta_guarda /home/kevin/Documentos/Proyecto_Distribuidos/Resultados/cliente_5_5.txt --total_cache 2 --puerto 8585'))


t1.start(); t2.start(); t3.start(); t4.start(); t5.start();