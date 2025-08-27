def elecao(lista):
    qtd_comparacoes = 0
    qtd_trocas = 0

    for i in range(len(lista) - 1):
        posMenor = i
        for j in range(i + 1, len(lista)):
            qtd_comparacoes += 1
            if lista[j] < lista[posMenor]:
                posMenor = j

        if i != posMenor:
            qtd_trocas += 1
            tmp = lista[i]
            lista[i] = lista[posMenor]
            lista[posMenor] = tmp

    return qtd_comparacoes, qtd_trocas

# --------------------------
# Código principal
# --------------------------
import random
import time
# Criar lista aleatória de 10.000 elementos entre 100 e 20.000
lista = [random.randint(100, 20000) for _ in range(10000)]

print("Primeiros 20 elementos antes da ordenação:", lista[:20])

# Medir tempo
inicio = time.time()
comparacoes, trocas = elecao(lista)
fim = time.time()

print("Primeiros 20 elementos após a ordenação:", lista[:20])
print("Comparações:", comparacoes)
print("Trocas:", trocas)
print("Tempo de execução: {:.4f} segundos".format(fim - inicio))