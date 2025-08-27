#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;

void insercao(int *vetor, long long int n) {
    long long int i, j;
    int tmp;
    long long int qtdComparacoes = 0, qtdTrocas = 0;

    for (i = 1; i < n; i++) {
        tmp = vetor[i];
        for (j = i - 1; j >= 0; j--) {
            qtdComparacoes++;
            if (tmp < vetor[j]) {
                vetor[j + 1] = vetor[j];
                qtdTrocas++;
            } else break;
        }
        vetor[j + 1] = tmp;
        qtdTrocas++;
    }
    cout << "Quantidade comparacoes: " << qtdComparacoes << endl;
    cout << "Quantidade trocas: " << qtdTrocas << endl << endl;
}

void popularVetorAleatorio(int *vetor, long long int n, int min, int max) {
    srand(time(0));
    for (long long int i = 0; i < n; i++) {
        vetor[i] = rand() % (max - min + 1) + min;
    }
}

void popularVetorOrdenado(int *vetor, long long int n) {
    for (long long int i = 0; i < n; i++) {
        vetor[i] = i;
    }
}

void copiarVetor(int *origem, int *destino, long long int n) {
    for (long long int i = 0; i < n; i++) {
        destino[i] = origem[i];
    }
}

void exibirVetor(int *vetor, long long int n, string frase) {
    cout << frase << endl;
    for (long long int i = 0; i < n; i++) {
        cout << vetor[i] << " ";
        if ((i + 1) % 10 == 0) cout << endl;
    }
    cout << endl << endl;
}

int main() {
    const long long int TAMANHO = 10000;
    int *vetorOriginal = new int[TAMANHO];
    int *vetorInsertion = new int[TAMANHO];
    
    // Popula vetor com números aleatórios
    popularVetorAleatorio(vetorOriginal, TAMANHO, 100, 20000);
    
    // Copia para o vetor que será ordenado
    copiarVetor(vetorOriginal, vetorInsertion, TAMANHO);
    
    // Exibe os primeiros 20 elementos (opcional)
    // exibirVetor(vetorInsertion, 20, "Vetor antes da ordenacao:");
    
    // Executa e mede o tempo do Insertion Sort
    clock_t inicio = clock();
    insercao(vetorInsertion, TAMANHO);
    clock_t fim = clock();
    
    double tempo = double(fim - inicio) / CLOCKS_PER_SEC;
    cout << "Tempo do Insertion Sort: " << tempo << " segundos" << endl;
    
    // Exibe os primeiros 20 elementos ordenados (opcional)
    // exibirVetor(vetorInsertion, 20, "Vetor apos a ordenacao:");
    
    // Limpa a memória
    delete[] vetorOriginal;
    delete[] vetorInsertion;
    
    return 0;
}