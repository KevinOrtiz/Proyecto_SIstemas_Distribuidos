/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ejemplo1;


import java.util.logging.Level;
import java.util.logging.Logger;
import org.apache.thrift.server.TServer;
import org.apache.thrift.server.TThreadPoolServer;
import org.apache.thrift.transport.TServerSocket;
import org.apache.thrift.transport.TTransportException;

/**
 *
 * @author kevin
 */
public class Ejemplo1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        try {
            // TODO code application logic here
            TServerSocket serverTransport = new TServerSocket(9191);
            pruebaSuma.Processor processor = new pruebaSuma.Processor(new pruebaOperacion());
            TServer server = new TThreadPoolServer(new TThreadPoolServer.Args(serverTransport).processor(processor));
            System.out.println("iniciando servidor en el puerto 9191");
            server.serve();
        
        } catch (TTransportException ex) {
            ex.printStackTrace();
        }
        
        
    }
    
}
