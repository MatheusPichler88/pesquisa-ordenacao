#Faça um método na sua linguagem de preferência que retorne true/True se a lista enviada como parâmetro está ordenada, o false/False caso contrário

def lista_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


 #Da a sequência de valores na estrutura abaixo, contabilize quantas comparações e quantas trocas há para os métodos:
        #- bolha
        #- pente
        #- seleção

        #0   1   2   3   4   5   6   7   8
        #30  90  10  20  80  10  20  40  10

    #- Na sua linguagem de preferência, implemente (sem consulta) seu método escolhido para saber.

lista_dada = [30, 90, 10, 20, 80, 10, 20, 40, 10]

print("Implementação do método de ordenação bolha:")    
def bubble_sort(lista_dada):
    n = len(lista_dada)
    comparacoes = 0
    trocas = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparacoes += 1
            if lista_dada[j] > lista_dada[j+1]:
                lista_dada[j], lista_dada[j+1] = lista_dada[j+1], lista_dada[j]
                trocas += 1
    return lista_dada, comparacoes, trocas

sorted_lista, total_comparacoes, total_trocas = bubble_sort(lista_dada)
print("Lista ordenada:", sorted_lista)
print("Total de comparações:", total_comparacoes)   
