# Importa a biblioteca de tempo
import time

#Criando a lista
listas = [
    [5, 3, 6, 2, 10, 1, 4, 9, 8, 7],
]
# Marca o momento que começa
tempoInicio = time.time()

# Ordena a primeira lista (isso é o que queremos medir)
listas[0].sort()

# Marca o momento que termina  
tempoFim = time.time()

# Calcula e mostra quanto tempo levou
print("Tempo de processamento do sort do Python: ", (tempoFim - tempoInicio) , "s")