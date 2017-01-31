#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import logging
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def hillClimbingSimple(self, listMiss, frequency, sizeCacheMemory, iMemoryValue, sizeAcumulateMemory, bd, cd):
    """
    Parameters:
     - listMiss
     - frequency
     - sizeCacheMemory
     - iMemoryValue
     - sizeAcumulateMemory
     - bd
     - cd
    """
    pass

  def hillClimbingRandom(self, listMIss, frequency, sizeCacheMemory, iMemoryValue, sizeAcumulateMemory, bd, cd, randomSaltos):
    """
    Parameters:
     - listMIss
     - frequency
     - sizeCacheMemory
     - iMemoryValue
     - sizeAcumulateMemory
     - bd
     - cd
     - randomSaltos
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def hillClimbingSimple(self, listMiss, frequency, sizeCacheMemory, iMemoryValue, sizeAcumulateMemory, bd, cd):
    """
    Parameters:
     - listMiss
     - frequency
     - sizeCacheMemory
     - iMemoryValue
     - sizeAcumulateMemory
     - bd
     - cd
    """
    self.send_hillClimbingSimple(listMiss, frequency, sizeCacheMemory, iMemoryValue, sizeAcumulateMemory, bd, cd)
    return self.recv_hillClimbingSimple()

  def send_hillClimbingSimple(self, listMiss, frequency, sizeCacheMemory, iMemoryValue, sizeAcumulateMemory, bd, cd):
    self._oprot.writeMessageBegin('hillClimbingSimple', TMessageType.CALL, self._seqid)
    args = hillClimbingSimple_args()
    args.listMiss = listMiss
    args.frequency = frequency
    args.sizeCacheMemory = sizeCacheMemory
    args.iMemoryValue = iMemoryValue
    args.sizeAcumulateMemory = sizeAcumulateMemory
    args.bd = bd
    args.cd = cd
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_hillClimbingSimple(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = hillClimbingSimple_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "hillClimbingSimple failed: unknown result")

  def hillClimbingRandom(self, listMIss, frequency, sizeCacheMemory, iMemoryValue, sizeAcumulateMemory, bd, cd, randomSaltos):
    """
    Parameters:
     - listMIss
     - frequency
     - sizeCacheMemory
     - iMemoryValue
     - sizeAcumulateMemory
     - bd
     - cd
     - randomSaltos
    """
    self.send_hillClimbingRandom(listMIss, frequency, sizeCacheMemory, iMemoryValue, sizeAcumulateMemory, bd, cd, randomSaltos)
    return self.recv_hillClimbingRandom()

  def send_hillClimbingRandom(self, listMIss, frequency, sizeCacheMemory, iMemoryValue, sizeAcumulateMemory, bd, cd, randomSaltos):
    self._oprot.writeMessageBegin('hillClimbingRandom', TMessageType.CALL, self._seqid)
    args = hillClimbingRandom_args()
    args.listMIss = listMIss
    args.frequency = frequency
    args.sizeCacheMemory = sizeCacheMemory
    args.iMemoryValue = iMemoryValue
    args.sizeAcumulateMemory = sizeAcumulateMemory
    args.bd = bd
    args.cd = cd
    args.randomSaltos = randomSaltos
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_hillClimbingRandom(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = hillClimbingRandom_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "hillClimbingRandom failed: unknown result")


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["hillClimbingSimple"] = Processor.process_hillClimbingSimple
    self._processMap["hillClimbingRandom"] = Processor.process_hillClimbingRandom

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_hillClimbingSimple(self, seqid, iprot, oprot):
    args = hillClimbingSimple_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = hillClimbingSimple_result()
    try:
      result.success = self._handler.hillClimbingSimple(args.listMiss, args.frequency, args.sizeCacheMemory, args.iMemoryValue, args.sizeAcumulateMemory, args.bd, args.cd)
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("hillClimbingSimple", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_hillClimbingRandom(self, seqid, iprot, oprot):
    args = hillClimbingRandom_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = hillClimbingRandom_result()
    try:
      result.success = self._handler.hillClimbingRandom(args.listMIss, args.frequency, args.sizeCacheMemory, args.iMemoryValue, args.sizeAcumulateMemory, args.bd, args.cd, args.randomSaltos)
      msg_type = TMessageType.REPLY
    except (TTransport.TTransportException, KeyboardInterrupt, SystemExit):
      raise
    except Exception as ex:
      msg_type = TMessageType.EXCEPTION
      logging.exception(ex)
      result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
    oprot.writeMessageBegin("hillClimbingRandom", msg_type, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class hillClimbingSimple_args:
  """
  Attributes:
   - listMiss
   - frequency
   - sizeCacheMemory
   - iMemoryValue
   - sizeAcumulateMemory
   - bd
   - cd
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'listMiss', (TType.DOUBLE,None), None, ), # 1
    (2, TType.DOUBLE, 'frequency', None, None, ), # 2
    (3, TType.DOUBLE, 'sizeCacheMemory', None, None, ), # 3
    (4, TType.DOUBLE, 'iMemoryValue', None, None, ), # 4
    (5, TType.DOUBLE, 'sizeAcumulateMemory', None, None, ), # 5
    (6, TType.DOUBLE, 'bd', None, None, ), # 6
    (7, TType.DOUBLE, 'cd', None, None, ), # 7
  )

  def __init__(self, listMiss=None, frequency=None, sizeCacheMemory=None, iMemoryValue=None, sizeAcumulateMemory=None, bd=None, cd=None,):
    self.listMiss = listMiss
    self.frequency = frequency
    self.sizeCacheMemory = sizeCacheMemory
    self.iMemoryValue = iMemoryValue
    self.sizeAcumulateMemory = sizeAcumulateMemory
    self.bd = bd
    self.cd = cd

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.listMiss = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readDouble()
            self.listMiss.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.DOUBLE:
          self.frequency = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.DOUBLE:
          self.sizeCacheMemory = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.DOUBLE:
          self.iMemoryValue = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.DOUBLE:
          self.sizeAcumulateMemory = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.DOUBLE:
          self.bd = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.DOUBLE:
          self.cd = iprot.readDouble()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('hillClimbingSimple_args')
    if self.listMiss is not None:
      oprot.writeFieldBegin('listMiss', TType.LIST, 1)
      oprot.writeListBegin(TType.DOUBLE, len(self.listMiss))
      for iter6 in self.listMiss:
        oprot.writeDouble(iter6)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.frequency is not None:
      oprot.writeFieldBegin('frequency', TType.DOUBLE, 2)
      oprot.writeDouble(self.frequency)
      oprot.writeFieldEnd()
    if self.sizeCacheMemory is not None:
      oprot.writeFieldBegin('sizeCacheMemory', TType.DOUBLE, 3)
      oprot.writeDouble(self.sizeCacheMemory)
      oprot.writeFieldEnd()
    if self.iMemoryValue is not None:
      oprot.writeFieldBegin('iMemoryValue', TType.DOUBLE, 4)
      oprot.writeDouble(self.iMemoryValue)
      oprot.writeFieldEnd()
    if self.sizeAcumulateMemory is not None:
      oprot.writeFieldBegin('sizeAcumulateMemory', TType.DOUBLE, 5)
      oprot.writeDouble(self.sizeAcumulateMemory)
      oprot.writeFieldEnd()
    if self.bd is not None:
      oprot.writeFieldBegin('bd', TType.DOUBLE, 6)
      oprot.writeDouble(self.bd)
      oprot.writeFieldEnd()
    if self.cd is not None:
      oprot.writeFieldBegin('cd', TType.DOUBLE, 7)
      oprot.writeDouble(self.cd)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.listMiss)
    value = (value * 31) ^ hash(self.frequency)
    value = (value * 31) ^ hash(self.sizeCacheMemory)
    value = (value * 31) ^ hash(self.iMemoryValue)
    value = (value * 31) ^ hash(self.sizeAcumulateMemory)
    value = (value * 31) ^ hash(self.bd)
    value = (value * 31) ^ hash(self.cd)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class hillClimbingSimple_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.DOUBLE, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.DOUBLE:
          self.success = iprot.readDouble()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('hillClimbingSimple_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.DOUBLE, 0)
      oprot.writeDouble(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class hillClimbingRandom_args:
  """
  Attributes:
   - listMIss
   - frequency
   - sizeCacheMemory
   - iMemoryValue
   - sizeAcumulateMemory
   - bd
   - cd
   - randomSaltos
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'listMIss', (TType.DOUBLE,None), None, ), # 1
    (2, TType.DOUBLE, 'frequency', None, None, ), # 2
    (3, TType.DOUBLE, 'sizeCacheMemory', None, None, ), # 3
    (4, TType.DOUBLE, 'iMemoryValue', None, None, ), # 4
    (5, TType.DOUBLE, 'sizeAcumulateMemory', None, None, ), # 5
    (6, TType.DOUBLE, 'bd', None, None, ), # 6
    (7, TType.DOUBLE, 'cd', None, None, ), # 7
    (8, TType.I32, 'randomSaltos', None, None, ), # 8
  )

  def __init__(self, listMIss=None, frequency=None, sizeCacheMemory=None, iMemoryValue=None, sizeAcumulateMemory=None, bd=None, cd=None, randomSaltos=None,):
    self.listMIss = listMIss
    self.frequency = frequency
    self.sizeCacheMemory = sizeCacheMemory
    self.iMemoryValue = iMemoryValue
    self.sizeAcumulateMemory = sizeAcumulateMemory
    self.bd = bd
    self.cd = cd
    self.randomSaltos = randomSaltos

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.listMIss = []
          (_etype10, _size7) = iprot.readListBegin()
          for _i11 in xrange(_size7):
            _elem12 = iprot.readDouble()
            self.listMIss.append(_elem12)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.DOUBLE:
          self.frequency = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.DOUBLE:
          self.sizeCacheMemory = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.DOUBLE:
          self.iMemoryValue = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.DOUBLE:
          self.sizeAcumulateMemory = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.DOUBLE:
          self.bd = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.DOUBLE:
          self.cd = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I32:
          self.randomSaltos = iprot.readI32()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('hillClimbingRandom_args')
    if self.listMIss is not None:
      oprot.writeFieldBegin('listMIss', TType.LIST, 1)
      oprot.writeListBegin(TType.DOUBLE, len(self.listMIss))
      for iter13 in self.listMIss:
        oprot.writeDouble(iter13)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.frequency is not None:
      oprot.writeFieldBegin('frequency', TType.DOUBLE, 2)
      oprot.writeDouble(self.frequency)
      oprot.writeFieldEnd()
    if self.sizeCacheMemory is not None:
      oprot.writeFieldBegin('sizeCacheMemory', TType.DOUBLE, 3)
      oprot.writeDouble(self.sizeCacheMemory)
      oprot.writeFieldEnd()
    if self.iMemoryValue is not None:
      oprot.writeFieldBegin('iMemoryValue', TType.DOUBLE, 4)
      oprot.writeDouble(self.iMemoryValue)
      oprot.writeFieldEnd()
    if self.sizeAcumulateMemory is not None:
      oprot.writeFieldBegin('sizeAcumulateMemory', TType.DOUBLE, 5)
      oprot.writeDouble(self.sizeAcumulateMemory)
      oprot.writeFieldEnd()
    if self.bd is not None:
      oprot.writeFieldBegin('bd', TType.DOUBLE, 6)
      oprot.writeDouble(self.bd)
      oprot.writeFieldEnd()
    if self.cd is not None:
      oprot.writeFieldBegin('cd', TType.DOUBLE, 7)
      oprot.writeDouble(self.cd)
      oprot.writeFieldEnd()
    if self.randomSaltos is not None:
      oprot.writeFieldBegin('randomSaltos', TType.I32, 8)
      oprot.writeI32(self.randomSaltos)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.listMIss)
    value = (value * 31) ^ hash(self.frequency)
    value = (value * 31) ^ hash(self.sizeCacheMemory)
    value = (value * 31) ^ hash(self.iMemoryValue)
    value = (value * 31) ^ hash(self.sizeAcumulateMemory)
    value = (value * 31) ^ hash(self.bd)
    value = (value * 31) ^ hash(self.cd)
    value = (value * 31) ^ hash(self.randomSaltos)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class hillClimbingRandom_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.DOUBLE, 'success', None, None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.DOUBLE:
          self.success = iprot.readDouble()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('hillClimbingRandom_result')
    if self.success is not None:
      oprot.writeFieldBegin('success', TType.DOUBLE, 0)
      oprot.writeDouble(self.success)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
