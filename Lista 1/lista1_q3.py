import turtle

# Função para desenhar um polígono qualquer
def sum_to(n):
    """
    Retorna a soma de todos os inteiros positivos de 0 até n (n incluso)
    Retorna -1 se o input for incorreto (numero negativo ou não inteiro)
    """    
    if n < 0 or type(n) != int:
        return -1
    total = 0
    for i in range(n+1):
        total += i
    return total

n = int(input("Escreva um número natural: "))
print("A soma dos números inteiros de 0 até {} é {}".format(n, sum_to(n)))