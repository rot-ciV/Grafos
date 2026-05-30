import networkx as nx
import sys

caminho_arquivo = "sjdr.gml"
Grafo = nx.read_gml(caminho_arquivo)

total_esquinas = Grafo.number_of_nodes()
esquinas_sem_saida = set()
cameras = 0

for esquina_atual in Grafo.nodes:

    if Grafo.degree[esquina_atual] == 1:
        esquinas_sem_saida.add(esquina_atual)

    
for esquina_atual in esquinas_sem_saida:
    
    esquina_com_camera = esquina_atual.neigneighbors()[0]






