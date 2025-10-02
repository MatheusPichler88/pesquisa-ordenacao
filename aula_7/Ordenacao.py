class Pessoal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f"{self.nome} ({self.idade})"    
    
def bolha(pessoas, chave):
    n = len(pessoas)
    for i in range(n):
        for j in range(0, n-i-1):
            if chave(pessoas[j]) > chave(pessoas[j+1]):
                pessoas[j], pessoas[j+1] = pessoas[j+1], pessoas[j]
    return pessoas

def pente(pessoas, chave):
    n = len(pessoas)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = pessoas[i]
            j = i
            while j >= gap and chave(pessoas[j - gap]) > chave(temp):
                pessoas[j] = pessoas[j - gap]
                j -= gap
            pessoas[j] = temp
        gap //= 2
    return pessoas

def ordena_por_idade(pessoas):
    return bolha(pessoas, chave=lambda pessoa: pessoa.idade)

def ordena_por_nome2(pessoas):
    return bolha(pessoas, chave=lambda pessoa: pessoa.nome)
def ordena_por_nome(pessoas):
    return pente(pessoas, chave=lambda pessoa: pessoa.nome)

def ordena_por_idade2(pessoas):
    return pente(pessoas, chave=lambda pessoa: pessoa.idade)

def main(): 
    pessoas = [
        Pessoal("Luiza", 19),
        Pessoal("Ricardo", 50),
        Pessoal("Matheus", 22),
        Pessoal("Kamila", 27),
        Pessoal("Ana", 23),
        Pessoal("Beatriz", 38)
    ]

    print("Original:", pessoas)
    print("================================")
    print("Ordenado por idade (Bolha):", ordena_por_idade(pessoas.copy()))
    print("Ordenado por nome (Bolha):", ordena_por_nome2(pessoas.copy()))
    print("Tempo de ordenação:")
    print("================================")
    print("Ordenado por idade (Pente):", ordena_por_idade2(pessoas.copy()))
    print("Ordenado por nome (Pente):", ordena_por_nome(pessoas.copy()))
   
    
if __name__ == "__main__":
    main()
   
    