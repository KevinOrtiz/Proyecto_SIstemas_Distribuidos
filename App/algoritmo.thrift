namespace java algoritmos
namespace py   algoritmos

service servicioPartioningMemory{
	double hillClimbingSimple(1:list<double> listMiss, 2:list<double> listCache, 3:double frequency, 4:double sizeCacheMemory, 5:double iMemoryValue, 6:double sizeAcumulateMemory, 7:double bd, 8:double cd);
	double hillClimbingRandom(1:list<double> listMIss, 2:list<double> listCache, 3:double frequency, 4:double sizeCacheMemory, 5:double iMemoryValue, 6:double sizeAcumulateMemory, 7:double bd, 8:double cd, 9:i32 randomSaltos);
}