import networkx as nx

grafo = nx.DiGraph()

with open('grafo.txt', 'r') as arquivo:

    for linha in arquivo:

        origem, destino, duracao = linha.split()

        grafo.add_edge(origem, destino, tempo = int(duracao))


for vert_atual in grafo.nodes:

    # if vertice atual tiver mais que 1 vizinho, tenho que dividir a  analise
    # caso contrario só continuo somando 