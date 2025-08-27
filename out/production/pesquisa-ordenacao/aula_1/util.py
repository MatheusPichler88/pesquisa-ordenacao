import random

class util:
    """
    Classe responsável por métodos de gestão de listas de numeros inteiros e lista de palavras.
    """
    
    @staticmethod
    def popular_aleatorio_numeros(lista, quantidade, inicio, fim):
        """_summary_
        Popular uma lista com números aleatórios.
        Args:
            lista (int): estrutura de armazenamento de números inteiros.
            quantidade (int): quantidade de números a serem gerados.
            inicio (int): valor mínimo do intervalo.
            fim (int): valor máximo do intervalo.
        """
        for _ in range(quantidade):
            lista.append(random.randrange(inicio, fim))
            
    @staticmethod
    def exibir_lista_numeros(lista):
        """
        Exibir os números contidos na lista.

        Args:
            lista (int): contém os números inteiros a serem exibidos.
        """
        for item in lista:
                    print(item)
            
    @staticmethod
    def popular_lista_palavras(lista, quantidade, tamanho):
                letras = 'abcdefghijklmnopqrstuvwxyz'
                for _ in range(quantidade):
                    palavra_gerada = ""
                    letra_gerada = ""
                    for _ in range(tamanho):
                        letra_gerada = letras[random.randrange(len(letras))]
                        palavra_gerada += letra_gerada
                    lista.append(palavra_gerada)