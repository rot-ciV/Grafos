import networkx as nx
import sys

grafo = nx.DiGraph()
grafos_disp = []

#Abre o arquivo grafos.txt em modo leitura e cria a variavel arquivo
with open('grafos.txt', 'r') as arquivo:

    for linha in arquivo:

        #transforma a String "linha" em uma nova sem quebra de linha e depois atribuí a linha_simples
        linha_simples = linha.strip()
        
        #Se a linha começar com "[" e termina com "] adiciona ela em grafos_disp 
        if linha_simples.startswith('[') and linha_simples.endswith(']'):

            grafos_disp.append(linha_simples)
            

# Caso não haja nenhum grafo para analisar, o programa fecha
if len(grafos_disp) == 0:

    sys.exit(('Nenhum grafo foi encontrado.'))


print('Grafos disponíveis no arquivo "grafos.txt":')

# O enumerate pega a lista de grafos e retorna o indice e o nome do grafo
for indice, nome in enumerate(grafos_disp):
    
    print(f'{indice + 1}. {nome}')    

while True:
    
    try:
        num_grafo = int(input('Digite o número do grafo desejado: '))

        if num_grafo <= 0 or num_grafo > len(grafos_disp):
            print('Opção inválida')
    
        else:
            break

    except ValueError:
        print('Opção inválida')

grafo_escolhido = grafos_disp[num_grafo - 1]
lendo_alvo = False

with open('grafos.txt', 'r') as arquivo:

    for linha in arquivo:

        linha_simples = linha.strip()
        
        if not linha_simples:
            continue

        if linha_simples.startswith('[') and linha_simples.endswith(']'):

            if linha_simples == grafo_escolhido:
                lendo_alvo = True
                continue

            else:
                lendo_alvo = False
                continue

        if lendo_alvo:

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

    if vertice_atual == None:
        break

    nao_visitados.remove(vertice_atual)

    for vizinho in grafo.neighbors(vertice_atual):

        distancia = grafo[vertice_atual][vizinho]['weight']

        if dicio_distancia[vizinho] > dicio_distancia[vertice_atual] + distancia:

            dicio_distancia[vizinho] = dicio_distancia[vertice_atual] + distancia
            dicio_rotas[vizinho] = vertice_atual


print('\n----- RESULTADOS -----\n')

for destino in grafo.nodes:

    print(f'Informações do vértice {destino}:')

    if dicio_distancia[destino] == float('inf'):
        print('Vértice inalcançável a partir da origem.\n')
        continue

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
