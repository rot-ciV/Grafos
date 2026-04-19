import networkx as nx
import sys

grafo = nx.DiGraph()

def logica_pert(grafo_utilizado):

    tempo_cedo = {}
    grau_de_entrada = {}
    fila_cedo = []
    fila_tarde = []

    for vertice_atual in grafo_utilizado.nodes:

        tempo_cedo[vertice_atual] = 0
        grau_de_entrada[vertice_atual] = grafo_utilizado.in_degree[vertice_atual]

        if grau_de_entrada[vertice_atual] == 0:
            fila_cedo.append(vertice_atual)

    while len(fila_cedo) > 0:

        vertice_processado = fila_cedo.pop(0)
        fila_tarde.append(vertice_processado)

        for vizinho in grafo_utilizado.neighbors(vertice_processado):

            tempo_gasto = grafo_utilizado[vertice_processado][vizinho]['tempo'] + tempo_cedo[vertice_processado]

            if tempo_gasto > tempo_cedo[vizinho]:

                tempo_cedo[vizinho] = tempo_gasto

            grau_de_entrada[vizinho] = grau_de_entrada[vizinho] - 1

            if grau_de_entrada[vizinho] == 0:

                fila_cedo.append(vizinho)

    fila_tarde.reverse()
    tempo_max = max(tempo_cedo.values())
    tempo_tarde = {}

    for vertice_atual in grafo_utilizado.nodes:

        if grafo_utilizado.out_degree[vertice_atual] == 0:
            tempo_tarde[vertice_atual] = tempo_max

        else:
            tempo_tarde[vertice_atual] = float('inf')

    while(len(fila_tarde) > 0):
        
        vertice_processado = fila_tarde.pop(0)

        for predecessor in grafo_utilizado.predecessors(vertice_processado):

            tempo_folga = tempo_tarde[vertice_processado] - grafo_utilizado[predecessor][vertice_processado]['tempo'] 

            if tempo_folga < tempo_tarde[predecessor]:

                tempo_tarde[predecessor] = tempo_folga

    return tempo_cedo, tempo_tarde


# ======= Lógica de Leitura do Arquivo grafos.txt ======= #

grafos_disp = []

with open('grafos.txt', 'r') as arquivo:

    for linha in arquivo:

        linha_simples = linha.strip()

        if linha_simples.startswith('[') and linha_simples.endswith(']'):

            grafos_disp.append(linha_simples)

if len(grafos_disp) == 0:
    sys.exit('\nNenhum grafo foi encontrado.')


# ======= Lógica de Escolha do Grafo ======= #


print('\nLista de Grafos disponiveis no arquivo grafos.txt:')

for indice, nome in enumerate(grafos_disp):

    print(f'{indice + 1}. {nome}')

while True:

    try:

        grafo_escolhido = int(input('\nDigite o número do grafo desejado: ')) - 1

        if grafo_escolhido < 0 or grafo_escolhido >= len(grafos_disp):
            print('Opção Inválida')

        else:
            break


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
            origem, destino, duracao = linha.split() 
            grafo.add_edge(origem, destino, tempo = int(duracao))


# ======= Lógica de Impressão de Resultados ======= #


tempo_cedo, tempo_tarde = logica_pert(grafo)

max_tempo = max(tempo_cedo.values())
caminho_crit = []
tam = len(caminho_crit)

print('\n=== Resultados ===')
print(f'\nTempo máximo: {max_tempo}\n')

for vertice in grafo.nodes:
    
    print(f'Vertice: {vertice}')
    print(f'Tempo Cedo: {tempo_cedo[vertice]}')
    print(f'Tempo Tarde: {tempo_tarde[vertice]}\n')

    if tempo_cedo[vertice] - tempo_tarde[vertice] == 0:
        caminho_crit.append(vertice)

print('Caminho crítico:')

for vertice in caminho_crit:
    
    if caminho_crit[tam - 1] == vertice:
        print(f'{vertice}\n')

    else:
        print(f'{vertice} -> ', end='')


