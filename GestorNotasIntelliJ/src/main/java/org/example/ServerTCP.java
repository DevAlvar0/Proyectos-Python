package org.example;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class ServerTCP {
    private static final int PUERTO = 6000;

    public static void main(String[] args) {
        System.out.println("--- Servidor de Notas (Multihilo) Iniciado en puerto " + PUERTO + " ---");

        try (ServerSocket serverSocket = new ServerSocket(PUERTO)) {
            while (true) {
                // 1. Aceptar conexión
                Socket socketCliente = serverSocket.accept();
                System.out.println("Cliente conectado: " + socketCliente.getInetAddress());

                // 2. Crear instancia de Worker (Runnable)
                Worker worker = new Worker(socketCliente);

                // 3. Crear el hilo pasando el Runnable y arrancarlo
                Thread hilo = new Thread(worker);
                hilo.start();
            }
        } catch (IOException e) {
            System.err.println("Error en el servidor: " + e.getMessage());
        }
    }
}