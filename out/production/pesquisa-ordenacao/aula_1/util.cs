
namespace ordenacao;
{   
    internal class util
{
        /// <summary>
        /// método de classe que popula uma lista de numeros inteiros aleatórios
        /// </summary>
        /// <param name="lista">Estrutura de armazenamento dos números</param>  
        /// <param name="quantidade">Quantidade de números a serem gerados</param>
        /// <param name="inicio">Valor inicial da extensão do número gerado</param>
        /// <param name="fim">Valor final da extensão do número gerado</param>
    }
    public static void popularAleatorioNumeros(List<int> lista, int quantidade, int inicio, int fim)
    {
        Random random = new Random();
        for (; quantidade > 0; quantidade--)
        {
            lista.add(random.Next(inicio, fim));

        }
    }

    /// <summary>
    /// Método de classe que exibe os números inteiros contidos na lista
    /// </summary>
    /// <param name="lista">Estrutura de armazenamento dos números</param>
    public static void exibirListaNumeros(List<int> lista) {
        foreach (int numero in lista)
        {
            Console.WriteLine(item);
        }
    }

    public static void popularAleatorioPalavras(List<String> lista, long quantidade, int tamanhoPalavra){
        String letras = "abcdefghijklmnopqrstuvwxyz";
        Random gerador = new Random();

        for (; quantidade >0; quantidade--){
            string palavraGerada = "";
            char letraSorteada;
            for (int i = 0; i< tamanho; i++){
                letraSorteada = letras[gerador.Next(letras.Length)];
                palavraGerada = palavraGerada + letraSorteada;
            }
            lista.add(palavraGerada);
        }
    }
}