import networkx as nx
import sys

grafo = nx.Graph()
grafos_disp = []

def logica_prim(grafo_utilizado):

    return 


# ======= Lógica de Leitura do Aquivo gragos.txt ======= #

with open('grafos.txt', 'r') as arquivo:

    for linha in arquivo:

        linha_simples = linha.strip()

        if linha_simples.startswith('[') and linha_simples.endswith(']'):
            
            grafos_disp.append(linha_simples)


if len(grafos_disp) == 0:
    sys.exit('Não há grafos disponíveis no arquivo "grafos.txt"')


# ======= Lógica de Escolha do grafo ======= #


print('Grafos disponíveis no arquivo "grafos.txt":')

for indice, nome in enumerate(grafos_disp):
    print(f'{indice + 1}. {nome}')


while True:

    try:

        grafo_escolhido = int(input('Digite o número do grafo desejado: ')) -1

        if grafo_escolhido < 0 or grafo_escolhido >= len(grafos_disp):
            print('Opção Inválida')

        else:
            break;

    except ValueError:
        print('Opção Inválida')


# ======= Lógica de Leitura do Grafo Escolhido ======= #    

lendo_alvo = False

with open('grafos.txt', 'r') as arquivo:

    for linha in arquivo:

        linha_simples = linha.strip()

        if not linha_simples:
            continue

        if linha_simples.startswith('[') and linha_simples.endswith(']'):

            if linha_simples == grafos_disp[grafo_escolhido]:
                lendo_alvo = True

            else:
                lendo_alvo = False
                continue

        if lendo_alvo:

            origem, destino, peso = linha.split()
            grafo.add_edge(origem, destino, peso = int(peso))


