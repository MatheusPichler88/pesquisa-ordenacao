package aula_2;

import java.util.ArrayList;
import java.util.List;

public class Rotina2 {
    public static void main(String[] args) {

        long tempoInicio = System.nanoTime();
        //Criação de lista com 100.000 números pelo índice.
        List<Integer> listaNumeros = new ArrayList<>();
        for(int i = 0; i < 100000; i++){
            listaNumeros.add(i);
        }
        long tempoFim = System.nanoTime();
        System.out.println("Tempo (ms) rotina 2: " + (tempoFim - tempoInicio)/1000000);
    }
}
