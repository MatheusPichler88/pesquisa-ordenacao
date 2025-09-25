class Ordenacao:
    @staticmethod
    def bolha(lista):
        houve_troca = True
        qtd_comparacoes = 0
        qtd_trocas = 0
        while (houve_troca):    
            houve_troca = False
            for i in range (len(lista) - 1):
                qtd_comparacoes+=1
                if (lista[i] > lista[i+1]):
                    qtd_trocas+=1
                    houve_troca = True
                    tmp = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = tmp
                    
        return qtd_comparacoes, qtd_trocas #medem a complexidade do algoritmo
    
    @staticmethod
    def selecao(lista):
        qtd_comparacoes = 0
        qtd_trocas = 0
        for i in range(len(lista) - 1):
            posMenor = i
            for j in range(i+1, len(lista)):
                qtd_comparacoes+=1
                if (lista[j] < lista[posMenor]):
                    posMenor = j
            if (i != posMenor):
                qtd_trocas+=1
                tmp = lista[i]
                lista[i] = lista[posMenor]
                lista[posMenor] = tmp
                
        return qtd_comparacoes, qtd_trocas
    
    
    @staticmethod
    def insercao(lista):
        qtd_comparacoes = 0
        qtd_trocas = 0

        for i in range(1, len(lista)):
            tmp = lista[i]
            for j in range(i - 1, -2, -1):
                qtd_comparacoes+=1
                if (tmp < lista[j]):
                    lista[j + 1] = lista[j]
                    qtd_trocas+=1
                else:
                    break

            lista[j + 1] = tmp
            qtd_trocas+=1
            
        return qtd_comparacoes, qtd_trocas
    
    @staticmethod
    def agitacao(lista):
        qtd_comparacoes = 0
        qtd_trocas = 0
        ini = 0
        fim = len(lista) - 1
        houve_troca = True

        while houve_troca:
            houve_troca = False
            for i in range(ini, fim):
                qtd_comparacoes += 1
                if lista[i] > lista[i + 1]:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    qtd_trocas += 1
                    houve_troca = True
            if not houve_troca:
                break
            fim -= 1

            houve_troca = False
            for i in range(fim, ini, -1):
                qtd_comparacoes += 1
                if lista[i] < lista[i - 1]:
                    lista[i], lista[i - 1] = lista[i - 1], lista[i]
                    qtd_trocas += 1
                    houve_troca = True
            ini += 1

        return qtd_comparacoes, qtd_trocas
    
    
    @staticmethod
    def pente(lista):
        houve_troca = True
        distancia = len(lista)
        qtd_comparacoes = 0
        qtd_trocas = 0
     

        while houve_troca or distancia > 1:
            distancia = int(distancia / 1.3)
            if distancia < 1:
                distancia = 1
            houve_troca = False
            i = 0
            for i in range(i - distancia) < len(lista):
                qtd_comparacoes += 1
                if lista[i] > lista[i + distancia]:
                    qtd_trocas += 1 
                    houve_troca = True
                    tmp = lista[i]
                    lista[i] = lista[i + distancia]
                    lista[i + distancia] = tmp
        return qtd_comparacoes, qtd_trocas
        
        
    @staticmethod
    def shell(lista):
        qtd_comparacoes = 0
    '''python

void shell(Lista<> lista) {
    int i, j;
    int tmp;
    int qtdComparacoes = 0, qtdTrocas = 0;
    int distancia = 1;

    int referenciaTamanho = 3;

    do {
        distancia = referenciaTamanho * distancia + 1;
    } while (distancia < n);
    

    do {
        distancia = (int)distancia / referenciaTamanho;
        
        for (i = distancia; i < n; i++) {
            tmp = vetor[i];
            for (j = i - distancia; j >= 0; j = j - distancia) {
                qtdComparacoes++;
                if (tmp < vetor[j]) {
                    vetor[j + distancia] = vetor[j];
                    qtdTrocas++;
                } else break;
            }
            vetor[j + distancia] = tmp;
            qtdTrocas++;
        }
    } while (distancia > 1);
}
'''