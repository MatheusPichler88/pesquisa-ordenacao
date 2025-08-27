import java.util.List;

public class BubbleSort {
    
    public static void bolha(List<Integer> lista) {
        boolean houveTroca;
        int tmp;
        int qtdComparacoes = 0, qtdTrocas = 0;
     
        do {
            houveTroca = false;
            for (int i = 0; i < lista.size()-1; i++){
                qtdComparacoes++;
                if (lista.get(i) > lista.get(i+1)) {
                    qtdTrocas++;
                    houveTroca = true;
                    tmp = lista.get(i);
                    lista.set(i, lista.get(i+1));
                    lista.set(i+1, tmp);
                }
            }
        } while (houveTroca);
        
        // Exibe as estatísticas
        System.out.println("Comparações: " + qtdComparacoes);
        System.out.println("Trocas: " + qtdTrocas);
    }
    
    // Método main para testar
    public static void main(String[] args) {
        // Exemplo de uso
        java.util.List<Integer> numeros = new java.util.ArrayList<>();
        numeros.add(5);
        numeros.add(2);
        numeros.add(8);
        numeros.add(1);
        numeros.add(3);
        
        System.out.println("Lista antes: " + numeros);
        bolha(numeros);
        System.out.println("Lista depois: " + numeros);
    }
}