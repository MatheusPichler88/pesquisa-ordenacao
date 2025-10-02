## Semana 10

# Desafio: 
"""Fazer um programa que:
    - Armazene milhoes de numeros inteiros ou poucos repetidos (desordenados)
    - localize o menor número gerado
    - retorne o número
    - temporize esse processamento
    - contabilize o número de comparações
    
- Pesquisa sequencial e pesqiuisa binária
- Pesquisa digital
"""

class Desafio:

    @staticmethod
    def armazenar_numeros(n):
        import random
        lista = random.sample(range(1, n*10), n)
        return lista

    @staticmethod
    def localizar_menor(lista):
        menor = lista[0]
        comparacoes = 0
        for numero in lista:
            comparacoes += 1
            if numero < menor:
                menor = numero
        return menor, comparacoes
    @staticmethod
    def temporizar_processamento(func, *args):
        import time
        inicio = time.time()
        resultado = func(*args)
        fim = time.time()
        tempo = fim - inicio
        return resultado, tempo
    
    @staticmethod
    def main():
        n = 500000
        lista = Desafio.armazenar_numeros(n)
        (menor, comparacoes), tempo = Desafio.temporizar_processamento(Desafio.localizar_menor, lista)
        print(f"Menor número: {menor}")
        print(f"Número de comparações: {comparacoes}")
        print(f"Tempo de processamento: {tempo:.6f} segundos")
        print(f"Lista original: {lista[:10]}") 
        
if __name__ == "__main__":
        Desafio.main()