/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package servidor;

import algoritmos.servicioPartioningMemory;
import org.apache.thrift.server.TServer;
import org.apache.thrift.server.TThreadPoolServer;
import org.apache.thrift.transport.TServerSocket;
import org.apache.thrift.transport.TTransportException;

/**
 *
 * @author kevin
 */
public class Servidor {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
         try {
            // TODO code application logic here
            TServerSocket serverTransport = new TServerSocket(8585);
            servicioPartioningMemory.Processor processor = new servicioPartioningMemory.Processor(new Algorithm());
            TServer server = new TThreadPoolServer(new TThreadPoolServer.Args(serverTransport).processor(processor));
            System.out.println("iniciando servidor en el puerto 8585");
            server.serve();
        
        } catch (TTransportException ex) {
            ex.printStackTrace();
        }
    }
    
}
