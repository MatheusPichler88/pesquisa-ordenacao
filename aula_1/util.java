package aula_1;

import java.util.ArrayList;
import java.util.Random;

public class util {
    /***
     * metodo para popular uma lista de numeros aleatorios entre inicio (inclusivo) e fim (exclusivo)
     * @param lista estrutura de armazenamento dos numeros
     * @param quantidade de numeros a serem gerados
     * @param inicio valor inicial da extensao do número gerado (inclusivo)
     * @param fim valor final da extensao do número gerado (exclusivo)
     */
    public static void popularAleatorioNumeros(ArrayList<Integer> lista, long quantidade, int inicio, int fim) {
        Random gerador = new Random();
        for (; quantidade > 0; quantidade--) {
            lista.add(gerador.nextInt(inicio, fim));
        }
    }

    /***
     * métoddo estatico que gera palavras aleatórias
     * @param lista armazena palavras geradas
     * @param quantidade de palavras a serem geradas
     * @param tamanhoPalavra das palavras a serem geradas
     */

    public static void popularAleatorioPalavras(ArrayList<String> lista, long quantidade, int tamanhoPalavra){
        String letras = "abcdefghijklmnopqrstuvwxyz";
        Random gerador = new Random();

        for (; quantidade >0; quantidade--){
            String palavraGerada = "";
            char letraSorteada;
            for (int i = 0; i< tamanhoPalavra; i++){
                letraSorteada = letras.charAt(gerador.nextInt(letras.length()));
                palavraGerada = palavraGerada + letraSorteada;
            }
            lista.add(palavraGerada);
        }
    }
    /***
     * metodo para exibir uma lista de numeros
     * @param lista estrutura de armazenamento dos numeros
     */
    public static void exibirListaNumeros(ArrayList<Integer> lista){
        for (Integer item : lista){
            System.out.println(item);
        }
    }

    /***
     * metodo para exibir uma lista de palavras
     * @param lista estrutura de armazenamento das palavras
     */
    public static void exibirListaPalavras(ArrayList<String> lista){
        for (String item : lista){
            System.out.println(item);
        }
    }
}
