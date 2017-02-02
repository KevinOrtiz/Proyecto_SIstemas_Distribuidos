/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package servidor;

import algoritmos.servicioPartioningMemory;
import java.util.List;
import org.apache.thrift.TException;

/**
 *
 * @author kevin
 */
public class Algorithm implements servicioPartioningMemory.Iface {

    @Override
    public double hillClimbingSimple(List<Double> listMiss, List<Double> listCache, double frequency, double sizeCacheMemory, double iMemoryValue, double sizeAcumulateMemory, double bd, double cd){
        double valueEAT;
        int indexCacheValue = 0;
        double actualValueMemory;
        double pastValueMemory=0;
        double candidateValueMemory;
        for(int i= 0; i < listMiss.size();i++){
            valueEAT = EAT(listMiss.get(i),bd,cd);
            actualValueMemory = -frequency * valueEAT;
         
            if (actualValueMemory < pastValueMemory) {
                candidateValueMemory = listCache.get(indexCacheValue);
                if ((sizeAcumulateMemory+candidateValueMemory)<= sizeCacheMemory) {
                    /*
                    hear return the value optimal 
                    */
                    return candidateValueMemory;
                    
                }      
           }
            
            indexCacheValue = i;
        }
        
        return (0);
        
       
    }

    @Override
    public double hillClimbingRandom(List<Double> listMIss, List<Double> listCache, double frequency, double sizeCacheMemory, double iMemoryValue, double sizeAcumulateMemory, double bd, double cd, int randomSaltos){
        int saltos = 0;
        int contadorColina = 0;
        double actualValueMemory;
        double pastValueMemory=0;
        double valueEAT;
        double candidateValueMemory=0;
        double valueMemory = 0;
        int sizeListHist = listMIss.size();
        int indexCacheValue = 0;
        for(int i=0; i < randomSaltos;i++){
        
            for (int j = saltos; j < listMIss.size(); j++) {
                contadorColina = j;
                valueEAT = EAT(listMIss.get(j),bd,cd);
                actualValueMemory = -frequency * valueEAT;
   
                    if (actualValueMemory < pastValueMemory && (listCache.get(indexCacheValue)+sizeAcumulateMemory) <= sizeCacheMemory) {
                        valueMemory=listCache.get(indexCacheValue);
                        break;
                        
                    }
                pastValueMemory = actualValueMemory;
                indexCacheValue = j;
                
            }
            
           saltos = (int) (contadorColina +(Math.random() * (sizeListHist - contadorColina)));     
        
        }
        
        if (valueMemory == 0) {
            return 0;
        }
        
        else  {
        
            return valueMemory;
        
        }
        
       
    
    }
    
     
    double EAT(double missValue,double bd, double cd){
       double valueEAT = (missValue*cd)+((1-missValue)*bd);
       return valueEAT;
    }
    
    
    
}
