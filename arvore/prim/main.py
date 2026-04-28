import networkx as nx
import sys

grafo = nx.Graph()
grafos_disp = []

def logica_prim(grafo_utilizado):

    prim = nx.Graph()
    custo = 0
    vertice_visitados = set()
    vertice_visitados.add(list(grafo_utilizado.nodes)[0])

    while(len(vertice_visitados) < len(grafo_utilizado.nodes)):

        menor_vizinho = None
        vertice_do_vizinho = None
        menor_peso = float('inf')

        for vertice in vertice_visitados:

            for vizinho in grafo_utilizado.neighbors(vertice):

                if vizinho in vertice_visitados:
                    continue

                if grafo_utilizado[vertice][vizinho]['peso'] < menor_peso:
                    menor_peso = grafo_utilizado[vertice][vizinho]['peso']
                    menor_vizinho = vizinho
                    vertice_do_vizinho = vertice

        
        vertice_visitados.add(menor_vizinho)
        prim.add_edge(vertice_do_vizinho, menor_vizinho, peso = int(menor_peso))
        custo = custo + menor_peso

    return prim, custo


# ======= Lógica de Leitura do Aquivo gragos.txt ======= #


with open('grafos.txt', 'r') as arquivo:

    for linha in arquivo:

        linha_simples = linha.strip()

        if linha_simples.startswith('[') and linha_simples.endswith(']'):
            
            grafos_disp.append(linha_simples)


if len(grafos_disp) == 0:
    sys.exit('\nNão há grafos disponíveis no arquivo "grafos.txt"')


# ======= Lógica de Escolha do grafo ======= #


print('\nGrafos disponíveis no arquivo "grafos.txt":')

for indice, nome in enumerate(grafos_disp):
    print(f'{indice + 1}. {nome}')


while True:

    try:

        grafo_escolhido = int(input('\nDigite o número do grafo desejado: ')) -1

        if grafo_escolhido < 0 or grafo_escolhido >= len(grafos_disp):
            print('Opção Inválida')

        else:
            break;

    except ValueError:
        print('Opção Inválida')


# ======= Lógica de Leitura do Grafo Escolhido ======= #    


with open('grafos.txt', 'r') as arquivo:

    lendo_alvo = False

    for linha in arquivo:

        linha_simples = linha.strip()

        if not linha_simples:
            continue

        if linha_simples.startswith('[') and linha_simples.endswith(']'):

            if linha_simples == grafos_disp[grafo_escolhido]:
                lendo_alvo = True
                continue

            else:
                lendo_alvo = False
                continue

        if lendo_alvo:

            origem, destino, peso = linha.split()
            grafo.add_edge(origem, destino, peso = int(peso))


# ======= Lógica de Impressão do Prim ======= #  

prim, custo = logica_prim(grafo) 

print('\n----- RESULTADOS -----\n')
print(f'Custo total: {custo}')
print('-' * 23)

for origem, destino, informacao in prim.edges(data=True):

    print(f'{origem} <----> {destino} | Custo: {informacao["peso"]}')

print('-' * 23  + '\n')