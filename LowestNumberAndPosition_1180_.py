N = int(input())
lista = list(map(int, input().split()))
menor = min(lista)
indi = lista.index(menor)
print("Menor valor:", menor)
print("Posicao:", indi)