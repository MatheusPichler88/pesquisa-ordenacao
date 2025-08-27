package aula_2;

import java.util.List;
import java.util.Random;

public class Utilidades {
    /**
     * Método de classe que popula uma lista com números aleatóriios e de forma sequencial dentro de uma faixa
     *
     * @param lista
     * @param quantidadeNumeros
     * @param inicio
     * @param fim
     * @param aleatorio         - se true, os números devem ser aleatórios
     */
    public static void popularLista(List<Integer> lista, long quantidadeNumeros, int inicio, int fim, boolean aleatorio) {
        Random gerador = new Random();

        if (aleatorio) {
            for (long i = 0; i < quantidadeNumeros; i++) {
                lista.add(gerador.nextInt(inicio, fim));
            }
        }
        if (!aleatorio) {
            for (long i = inicio; i < fim; i++) {
                lista.add((int) i);
            }
        }
    }

    /**
     * Método de classe que exibe o conteúdo de uma lista de inteiros
     *
     * @param lista
     * @param frase - para exibir no início do método
     */
    public static void exibirLista(List<Integer> lista, String frase) {
        System.out.println(frase);
        for (Integer item : lista) {
            System.out.print(item);
        }
        System.out.println("--------------");
        System.out.println("Total de registros: " + lista.size());
    }
}
