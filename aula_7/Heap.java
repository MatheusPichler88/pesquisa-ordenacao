import java.util.ArrayList;
import java.util.List;

class Ordenacao {
    public static boolean emHeapMaximo(ArrayList<Integer> lista){
        int n = lista.size();
        for (int i = 0; i <= (n - 2) / 2; i++) {
            int filhoEsquerdo = 2 * i + 1;
            int filhoDireito = 2 * i + 2;

            if (filhoEsquerdo < n && lista.get(i) < lista.get(filhoEsquerdo)) {
                return false;
            }
            if (filhoDireito < n && lista.get(i) < lista.get(filhoDireito)) {
                return false;
            }
        }
        return true;
    }
}

public class Heap {
    public static void main(String[] args) {
        ArrayList<Integer> lista = new ArrayList<>(List.of(10, 9, 8, 7, 6, 5, 4, 3, 2, 1));

        System.out.println("Lista original: " + lista);

        if(Ordenacao.emHeapMaximo(lista)){
            System.out.println("A lista está em heap máximo.");
        } else {
            System.out.println("A lista não está em heap máximo.");
        }
    }
}