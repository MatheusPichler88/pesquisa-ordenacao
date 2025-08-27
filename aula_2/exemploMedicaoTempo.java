package aula_2;
import java.util.ArrayList;
import java.util.List;

public class exemploMedicaoTempo {
    public static void main(String[] args) {
        long tempoInicio, tempoFim; 
        List<Integer> listaAleatoria = new ArrayList<>(); 
        List<Integer> listaSequencial = new ArrayList<>();
    
        tempoInicio = System.nanoTime();
        // rotina1 - popular uma lista com 100000 aleatorios na faixa 100 a 100000
        Utilidades.popularLista(listaAleatoria, 100000, 100, 100000, true);
        //Utilidades.exibirLista(listaAleatoria, "Lista aleatória");
        tempoFim = System.nanoTime();
        System.out.println("Tempo (ms) rotina 1: " + (tempoFim - tempoInicio)/1000000);
 
        tempoInicio = System.nanoTime();
        // rotina2 - popular uma lista com 100000 de forma crescente 0 na posição 0, 1 na posição 1, e assim por diante
        Utilidades.popularLista(listaSequencial, 100000, 100, 100000, false);
        //Utilidades.exibirLista(listaAleatoria, "Lista sequencial");
        tempoFim = System.nanoTime();
        System.out.println("Tempo (ms) rotina 2: " + (tempoFim - tempoInicio)/1000000);
    }
}
 
 