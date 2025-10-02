"""Desafio:
    - Método que recebe uma lista de inteiros e retorna:
        - True se a lista está em Heap Máximo
        - False se a lista não está em Heap Máximo """

class Ordenacao:
    
    @staticmethod
    def em_heap_maximo(lista):
        i = 0
        while i < len(lista):
            fe = 2 * i + 1
            fd = 2 * i + 2
            if fe < len(lista) and (lista[i] < lista[fe]):
                return False
            
            if fd < len(lista):
                if(lista[i] < lista[fd]):
                    return False
            i += 1
        return True

def main():
    lista = [8,3,6,1,2,4,5]
    print ('Lista original:' , lista)
    if(Ordenacao.em_heap_maximo(lista)):
        print ('Está em Heap Máximo? ', Ordenacao.em_heap_maximo(lista))
    else:
        print (' Não está em Heap Máximo! ')
