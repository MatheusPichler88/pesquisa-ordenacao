import random
import time

class Util:
    @staticmethod
    def popular_lista_aleatoria(lista, quantidade, inicio, fim):
        for _ in range(quantidade):
            lista.append(random.randint(inicio, fim))
            
    @staticmethod
    def exibir_lista(lista, frase):
        print(frase)
        for item in lista:
            print(item)
 
class Ordenacao:
    @staticmethod
    def bolha(lista):
        houve_troca = True
        qtd_comparacoes = 0
        qtd_trocas = 0
        while houve_troca:    
            houve_troca = False
            for i in range(len(lista) - 1):
                qtd_comparacoes += 1
                if lista[i] > lista[i+1]:
                    qtd_trocas += 1
                    houve_troca = True
                    tmp = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = tmp
        return qtd_comparacoes, qtd_trocas

# -----------------------------
# Código principal
# -----------------------------
lista_bolha = []
lista_normal = []

Util.popular_lista_aleatoria(lista_bolha, 10000, 100, 20000)
Util.popular_lista_aleatoria(lista_normal, 10000, 100, 20000)
 
tempoInicio = time.time()
lista_normal.sort()
tempoFim = time.time()
print("Tempo da rotina ordenar por sort nativo: ", (tempoFim - tempoInicio), "s")        
 
tempoInicio = time.time()
qtd_comparacoes, qtd_trocas = Ordenacao.bolha(lista_bolha)
tempoFim = time.time()
print("Tempo da rotina ordenar por bolha: ", (tempoFim - tempoInicio), "s")      
print('Comparacoes:', qtd_comparacoes)
print('Trocas:', qtd_trocas)
