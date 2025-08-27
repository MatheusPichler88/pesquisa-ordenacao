package aula_2;

import java.util.List;
import java.util.Random;
import java.util.ArrayList;

public class Rotina1 {
    public static void main(String[] args) {
        Random gerador = new Random();
        List listaNumeros = new ArrayList<>();
        int min = 100;
        int max = 100000;
        int numero = 0;
        //Começa a contar o tempo
        long tempoInicio = System.nanoTime();
        // TODO:popular uma lista com 100000 aleatorios na faixa 100 a 100000
        //Lista com intervalos de 100 até 100000.
        for (int i = 0; i < 100000; i++) {
            numero = gerador.nextInt((max - min) + 1) + min;
            listaNumeros.add(numero);
        }
        //Termina de contar o tempo.
        long tempoFim = System.nanoTime();
        System.out.println("Tempo (ms) rotina 1: " + (tempoFim - tempoInicio)/1000000);
    }
}