import networkx as nx

grafo = nx.DiGraph()

with open('grafos.txt', 'r') as arquivo:

    for linha in arquivo:

        origem, destino, peso = linha.split()

        grafo.add_edge(int(origem), int(destino), weight = int(peso))


vertice_analisado = int(input('Qual vértice gostaria de ser analisado? '))

dicio_distancia = {}
dicio_rotas = {}

for vertice in grafo.nodes:

    dicio_rotas[vertice] = None
    
    if vertice == vertice_analisado:

        dicio_distancia[vertice] = 0
    
    else:

        dicio_distancia[vertice] = float('inf')


nao_visitados = list(grafo.nodes)

while len(nao_visitados) > 0:

    vertice_atual = None
    menor_distancia = float('inf')

    for vertice in nao_visitados:

        if dicio_distancia[vertice] < menor_distancia:

            menor_distancia = dicio_distancia[vertice]
            vertice_atual = vertice

    nao_visitados.remove(vertice_atual)

    for vizinho in grafo.neighbors(vertice_atual):

        distancia = grafo[vertice_atual][vizinho]['weight']

        if dicio_distancia[vizinho] > dicio_distancia[vertice_atual] + distancia:

            dicio_distancia[vizinho] = dicio_distancia[vertice_atual] + distancia
            dicio_rotas[vizinho] = vertice_atual


print('\n----- RESULTADOS -----\n')

for destino in grafo.nodes:

    print(f'Informações do vértice {destino}:')
    print(f'Menor distância: {dicio_distancia[destino]}')
    print('Rota: ', end='')
    caminho = destino
    rota = []

    while caminho != vertice_analisado:

        rota.append(caminho)
        caminho = dicio_rotas[caminho]

    rota.append(vertice_analisado)
    rota.reverse()

    for resultado in rota:

        if resultado == destino:

            print(f'{resultado}\n')

        else:

            print(f'{resultado} -> ',end='')
