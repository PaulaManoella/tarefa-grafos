import numpy as np
import time
import os
import networkx as nx
import matplotlib.pyplot as plt

def carregando():
    for i in "Carregando arquivo...":
        print(i, end=' ', flush=True)
        time.sleep(0.2)
carregando()
os.system('cls')
print('Arquivo carregado!\n\nComo deseja representar o grafo?\n(1) Matriz de Adjacência\n(2) Lista de Adjacência')
op = input()
os.system('cls')

def imprime_matriz(num_v, matriz):
    for i in range(num_v):
        for j in range(num_v):
            print(matriz[i,j], end=' ')
        print()

def carrega_matriz():
    arquivo = open('grafo.txt', 'r')
    linhas_arquivo = arquivo.readlines()

    for i in range(len(linhas_arquivo)):
        linha = linhas_arquivo[i].split()
        if i == 0:
            num_v = int(linha[0])
            matriz = np.zeros((num_v, num_v), dtype=np.int64)
        else:
            matriz[int(linha[0]), int(linha[1])] = 1
            matriz[int(linha[1]), int(linha[0])] = 1
    arquivo.close()
    imprime_matriz(num_v, matriz)

def imprime_lista(num_v, lista):
    for i in range(num_v):
        print(f'Vértice {i+1} : {lista[i]}')

lista = []
def carrega_lista_adj():
    arquivo = open('grafo.txt', 'r')
    linhas_arquivo = arquivo.readlines()
    for i in range(len(linhas_arquivo)):
        linha = linhas_arquivo[i].split()
        if i == 0:
            num_v = int(linha[0])
            lista_adj = [[] for _ in range(num_v)]
        else:
            lista_adj[int(linha[0])].append(int(linha[1])+1)
            lista_adj[int(linha[1])].append(int(linha[0])+1)

            par = (int(linha[0])+1, int(linha[1])+1)
            lista.append(par)
    arquivo.close()
    imprime_lista(num_v, lista_adj)

    return lista
lista_pares = carrega_lista_adj()

match op:
    case '1':
        print('Você escolheu Matriz de Adjacência!\n')
        carrega_matriz()
    case '2':
        print('Você escolheu Lista de Adjacência!\n')
        carrega_lista_adj()

op = input('Deseja ver a representação visual do grafo? ')
if op.lower() == 'sim':
    G = nx.Graph()
    G.add_edges_from(lista_pares)
    nx.draw(G, with_labels=True)
    plt.show()