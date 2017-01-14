import sys, glob
sys.path.append('gen-py')
##sys.path.insert(0, glob.glob('/home/kevin/Descarga/thrift-0.9.3/lib/py/build/lib.*')[0])

from tutorial import pruebaSuma
from tutorial.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


try:
	# Make socket
  transport = TSocket.TSocket('localhost', 9191)

  # Buffering is critical. Raw sockets are very slow
  transportBuffering = TTransport.TBufferedTransport(transport)

  # Wrap in a protocol
  protocolBinnary = TBinaryProtocol.TBinaryProtocol(transportBuffering)

  # Create a client to use the protocol encoder
  client = pruebaSuma.Client(protocolBinnary)

  # Connect!
  transportBuffering.open()

  print "Conectado cliente con exito"

  suma = client.sumar(1,2)

  print(suma)

  resta = client.restar(10,5)

  print(resta)

  transportBuffering.close()

	
except Thrift.TException, tx:
	print '%s' % (tx.message)
	