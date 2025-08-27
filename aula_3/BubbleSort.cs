using System;
using System.Collections.Generic;

class Program
{
    static void Bolha(List<int> lista)
    {
        bool houveTroca;
        int tmp;
        int qtdComparacoes = 0, qtdTrocas = 0;

        do
        {
            houveTroca = false;
            for (int i = 0; i < lista.Count - 1; i++)
            {
                qtdComparacoes++;
                if (lista[i] > lista[i + 1])
                {
                    qtdTrocas++;
                    houveTroca = true;

                    tmp = lista[i];
                    lista[i] = lista[i + 1];
                    lista[i + 1] = tmp;
                }
            }
        } while (houveTroca);

        Console.WriteLine("Comparações: " + qtdComparacoes);
        Console.WriteLine("Trocas: " + qtdTrocas);
    }

    static void Main()
    {
        List<int> numeros = new List<int>() { 5, 3, 8, 4, 2 };
        Bolha(numeros);

        Console.WriteLine("Lista ordenada:");
        foreach (var n in numeros)
        {
            Console.Write(n + " ");
        }
    }
}
