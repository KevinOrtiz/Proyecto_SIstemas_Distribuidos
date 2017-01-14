/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ejemplo1;

import org.apache.thrift.TException;

/**
 *
 * @author kevin
 */
public class pruebaOperacion implements pruebaSuma.Iface {

    @Override
    public void restar(int number1, int number2) throws TException {
        System.out.println("Operacion de restar......efectuandoce");
        int resultado = number1-number2;
        System.out.println("Resultado:"+resultado);
    }

    @Override
    public void sumar(int number1, int number2) throws TException {
        System.out.println("Operacion de sumar......efectuando suma");
        int resultado = number1+number2;
        System.out.println("Resultado:"+resultado);

        
    }
    
}
