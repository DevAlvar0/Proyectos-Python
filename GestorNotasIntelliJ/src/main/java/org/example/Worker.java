package org.example;

import java.io.*;
import java.net.Socket;

public class Worker implements Runnable {

    private final Socket socket;
    // Credenciales
    private static final String USUARIO_VALIDO = "pepe";
    private static final String PASS_VALIDO = "1234";
    // Archivo
    private static final String ARCHIVO_NOTAS = "notas.txt";
    // Objeto estático para sincronizar la escritura entre distintos hilos Worker
    private static final Object lock = new Object();

    public Worker(Socket socket) {
        this.socket = socket;
    }

    @Override
    public void run() {
        try (
                BufferedReader entrada = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter salida = new PrintWriter(socket.getOutputStream(), true)
        ) {
            // --- FASE 1: LOGIN ---
            boolean autenticado = false;
            int intentos = 0;

            while (intentos < 3 && !autenticado) {
                String usuario = entrada.readLine();
                String pass = entrada.readLine();

                if (USUARIO_VALIDO.equals(usuario) && PASS_VALIDO.equals(pass)) {
                    salida.println("LOGIN_OK");
                    autenticado = true;
                } else {
                    intentos++;
                    if (intentos == 3) {
                        salida.println("LOGIN_FALLIDO");
                    } else {
                        salida.println("REINTENTAR");
                    }
                }
            }

            if (!autenticado) {
                System.out.println("Cliente " + socket.getInetAddress() + " desconectado por fallos de login.");
                socket.close();
                return;
            }

            // --- FASE 2: GESTIÓN DE NOTAS ---
            String comando;
            boolean continuar = true;

            while (continuar && (comando = entrada.readLine()) != null) {

                if (comando.startsWith("ADD")) {
                    String textoNota = comando.substring(4); // Quitar "ADD "
                    guardarNotaEnFichero(textoNota);
                    salida.println("NOTA_GUARDADA");
                    System.out.println("Nota guardada para cliente " + socket.getInetAddress());

                } else if (comando.equals("LIST")) {
                    enviarListaNotas(salida);

                } else if (comando.equals("QUIT")) {
                    continuar = false;
                }
            }

        } catch (IOException e) {
            System.err.println("Error en la comunicación con cliente: " + e.getMessage());
        } finally {
            try {
                if (socket != null && !socket.isClosed()) {
                    socket.close();
                }
                System.out.println("Conexión cerrada con cliente.");
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    /**
     * Guarda la nota en el archivo.
     * Importante: Usa un bloque 'synchronized(lock)' estático.
     * Al ser 'Worker' instanciado múltiples veces, 'synchronized(this)' no serviría.
     */
    private void guardarNotaEnFichero(String nota) {
        synchronized (lock) {
            try (PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter(ARCHIVO_NOTAS, true)))) {
                pw.println(nota);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    private void enviarListaNotas(PrintWriter salida) {
        // Para leer no es estrictamente necesario bloquear, aunque recomendable si la escritura es muy frecuente.
        // Aquí permitiremos lectura concurrente sin bloqueo estricto para mayor velocidad.
        File archivo = new File(ARCHIVO_NOTAS);

        if (!archivo.exists() || archivo.length() == 0) {
            salida.println("SIN_NOTAS");
            return;
        }

        try (BufferedReader br = new BufferedReader(new FileReader(archivo))) {
            salida.println("LISTA_INICIO");
            String linea;
            while ((linea = br.readLine()) != null) {
                salida.println(linea);
            }
            salida.println("LISTA_FIN");
        } catch (IOException e) {
            salida.println("SIN_NOTAS");
        }
    }
}