import time
import random

class Util:
    @staticmethod
    def popular_lista_aleatoria(lista, quantidade, minimo, maximo):
        """Preenche uma lista com números aleatórios"""
        lista.clear()
        for _ in range(quantidade):
            lista.append(random.randint(minimo, maximo))

class Ordenacao:
    @staticmethod
    def bolha(lista):
        """Implementação do algoritmo Bubble Sort"""
        houve_troca = True
        qtd_comparacoes = 0  # Contador de comparações
        qtd_trocas = 0       # Contador de trocas
        while (houve_troca):    
            houve_troca = False
            for i in range (len(lista) - 1):
                qtd_comparacoes += 1  # Conta cada comparação
                if (lista[i] > lista[i+1]):
                    qtd_trocas += 1   # Conta cada troca
                    houve_troca = True
                    # Faz a troca de posição
                    tmp = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = tmp
        return qtd_comparacoes, qtd_trocas
    
    @staticmethod
    def selecao(lista):
        """Implementação do algoritmo Selection Sort"""
        qtd_comparacoes = 0  # Contador de comparações
        qtd_trocas = 0       # Contador de trocas
        for i in range(len(lista) - 1):
            posMenor = i  # Assume que o menor está na posição i
            for j in range(i+1, len(lista)):
                qtd_comparacoes += 1  # Conta cada comparação
                if (lista[j] < lista[posMenor]):
                    posMenor = j  # Encontrou um elemento menor
            if (i != posMenor):
                qtd_trocas += 1   # Conta cada troca
                # Faz a troca de posição
                tmp = lista[i]
                lista[i] = lista[posMenor]
                lista[posMenor] = tmp
        return qtd_comparacoes, qtd_trocas

# Cria três listas vazias para os testes
lista_bolha = []        # Para testar algoritmo Bubble Sort
lista_normal = []       # Para testar método .sort() nativo do Python  
lista_selecao = []      # Para testar algoritmo Selection Sort

# Preenche as 3 listas com os MESMOS números aleatórios (5000 números entre 100 e 20000)
Util.popular_lista_aleatoria(lista_bolha, 5000, 100, 20000)
Util.popular_lista_aleatoria(lista_normal, 5000, 100, 20000)
Util.popular_lista_aleatoria(lista_selecao, 5000, 100, 20000)

# Teste 1: Mede tempo do método nativo do Python (o mais rápido)
tempoInicio = time.time()
lista_normal.sort()  # Usa algoritmo otimizado do Python
tempoFim = time.time()
print("Tempo da rotina ordenar por sort nativo: ", (tempoFim - tempoInicio) , "s")        

# Teste 2: Mede tempo do Bubble Sort (implementação manual)
tempoInicio = time.time()
qtd_comparacoes, qtd_trocas = Ordenacao.bolha(lista_bolha)  # Algoritmo Bubble Sort
tempoFim = time.time()
print("Tempo da rotina ordenar por bolha: ", (tempoFim - tempoInicio) , "s")      
print('Comparacoes:', qtd_comparacoes)  # Mostra quantas comparações foram feitas
print('Trocas:', qtd_trocas)            # Mostra quantas trocas foram feitas

# Teste 3: Mede tempo do Selection Sort (implementação manual)
tempoInicio = time.time()
qtd_comparacoes, qtd_trocas = Ordenacao.selecao(lista_selecao)  # Algoritmo Selection Sort
tempoFim = time.time()
print("Tempo da rotina ordenar por selecao: ", (tempoFim - tempoInicio) , "s")      
print('Comparacoes:', qtd_comparacoes)  # Mostra quantas comparações foram feitas
print('Trocas:', qtd_trocas)            # Mostra quantas trocas foram feitas