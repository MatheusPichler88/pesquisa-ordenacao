import java.util.List;
public class SelectionSort {
    public static void selectionSort(List<Integer> lista) {
        int tmp;
        int posMenor;
        int qtd_comparacoes = 0, qtd_trocas = 0;

        for (int i = 0; i < lista.size() - 1; i++) {
            posMenor = i;
            for (int j = i + 1; j < lista.size(); j++) {
                qtd_comparacoes++;
                if (lista.get(j) < lista.get(posMenor)) {
                    posMenor = j;
                }
            }
            if (i != posMenor) {
                qtd_trocas++;
                tmp = lista.get(i);
                lista.set(i, lista.get(posMenor));
                lista.set(posMenor, tmp);
            }
        }

        System.out.println("Comparações: " + qtd_comparacoes);
        System.out.println("Trocas: " + qtd_trocas);
    }
}


