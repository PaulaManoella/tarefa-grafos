import networkx as nx
import matplotlib.pyplot as plt

def obter_grafo(numero):
    print(f'Grafo {numero}\n' + '='*45)
    
    v = int(input(f'Informe o número de vértices do grafo {numero}: '))
    lista_v = [i + 1 for i in range(v)]

    lista_e = []
    while True:
        op = input('Deseja adicionar uma nova aresta? ')
        if op  == "nao":
            break
        else:   
            arestas = input("Informe as arestas separadas por espaço.\nExemplo: 1 2\n")
            separado = arestas.split()
            e = [int(i) for i in separado]
            tupla = (e[0], e[1])
            lista_e.append(tupla)
    
    return lista_v, lista_e

v1, e1 = obter_grafo(1)
v2, e2 = obter_grafo(2)

produto_cartesiano = [(v1[i], v2[j]) for i in range(len(v1)) for j in range(len(v2))]

print(produto_cartesiano)

arestas_produto = []

for i, (v1_a, v2_a) in enumerate(produto_cartesiano):
    for j, (v1_b, v2_b) in enumerate(produto_cartesiano):
        if i != j:
            #compara o primeiro elemento do par
            if v1_a == v1_b and (v2_a, v2_b) in e2:
                arestas_produto.append(((v1_a, v2_a), (v1_b, v2_b)))
            #compara o segundo elemento do par
            if v2_a == v2_b and (v1_a, v1_b) in e1:
                arestas_produto.append(((v1_a, v2_a), (v1_b, v2_b)))

G = nx.Graph()
G.add_edges_from(arestas_produto)
nx.draw(G, with_labels=True)
plt.show()