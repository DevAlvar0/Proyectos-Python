package org.example;

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class ClientTCP {
    private static final String HOST = "localhost";
    private static final int PUERTO = 6000;

    public static void main(String[] args) {
        System.out.println("--- Cliente Conectando al Servidor ---");

        try (Socket socket = new Socket(HOST, PUERTO);
             PrintWriter salida = new PrintWriter(socket.getOutputStream(), true);
             BufferedReader entrada = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             Scanner sc = new Scanner(System.in)) {

            // --- LOGIN ---
            boolean logueado = false;
            while (!logueado) {
                System.out.print("Usuario: ");
                String user = sc.nextLine();
                System.out.print("Password: ");
                String pass = sc.nextLine();

                salida.println(user);
                salida.println(pass);

                String respuesta = entrada.readLine();
                if ("LOGIN_OK".equals(respuesta)) {
                    System.out.println(">> Acceso concedido.");
                    logueado = true;
                } else if ("LOGIN_FALLIDO".equals(respuesta)) {
                    System.out.println(">> Acceso denegado. Cerrando.");
                    return;
                } else {
                    System.out.println(">> Credenciales erróneas. Inténtalo de nuevo.");
                }
            }

            // --- MENÚ ---
            boolean salir = false;
            while (!salir) {
                System.out.println("\n1. Añadir nota | 2. Listar notas | 3. Salir");
                System.out.print("> ");
                String op = sc.nextLine();

                switch (op) {
                    case "1":
                        System.out.print("Escribe la nota: ");
                        String nota = sc.nextLine();
                        salida.println("ADD " + nota);
                        System.out.println("Servidor: " + entrada.readLine());
                        break;
                    case "2":
                        salida.println("LIST");
                        String linea;
                        // Leemos la primera línea para ver si hay notas
                        String cabecera = entrada.readLine();
                        if ("SIN_NOTAS".equals(cabecera)) {
                            System.out.println(">> No hay notas en el servidor.");
                        } else if ("LISTA_INICIO".equals(cabecera)) {
                            System.out.println("--- LISTA DE NOTAS ---");
                            while (!(linea = entrada.readLine()).equals("LISTA_FIN")) {
                                System.out.println(linea);
                            }
                            System.out.println("----------------------");
                        }
                        break;
                    case "3":
                        salida.println("QUIT");
                        salir = true;
                        break;
                    default:
                        System.out.println("Opción incorrecta.");
                }
            }

        } catch (IOException e) {
            System.err.println("Error en cliente: " + e.getMessage());
        }
    }
}