package aula_1;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> listaNumeros = new ArrayList<>();
        ArrayList<Integer> lista2Numeros = new ArrayList<>();


        ArrayList<String> listaPalavras = new ArrayList<>();

        util.popularAleatorioNumeros(listaNumeros, 10, 100, 500);
        util.exibirListaNumeros(listaNumeros);

        lista2Numeros.addAll(listaNumeros);

        // Exibe a lista2Numeros para evitar o aviso de variável não utilizada
        util.exibirListaNumeros(lista2Numeros);

        util.popularAleatorioPalavras(listaPalavras, 10, 6);
        util.exibirListaPalavras(listaPalavras);



    }
}
