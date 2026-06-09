import networkx as nx

caminho_arquivo = "Tabuleiro_com_incompatibilidades.gml"
Grafo = nx.read_gml(caminho_arquivo)

pos_rainha = list()
flag = 1
posicoes = list(Grafo.nodes)
indice = 0
    
while(indice < len(posicoes)):
    
    flag = 1
    quadradin = posicoes[indice]

    for pos_atual in pos_rainha:

        if Grafo.has_edge(pos_atual, quadradin):
            flag = 0
            break

    if flag:
        pos_rainha.append(quadradin)
        indice = ((indice // 8) * 8) + 8

    else:

        indice  += 1

        while indice % 8 == 0:

            indice = posicoes.index(pos_rainha[-1]) + 1
            pos_rainha.pop()
            

# ===== Impressao dos Resultados ===== #

print('\n=========== RESULTADO ===========\n')

num_resultados = len(pos_rainha) // 8

for linha in range (8):

    desenho_linha = ""

    for coluna in range(8):

        indice = (linha * 8) + coluna
        quadradin = posicoes[indice]

        if quadradin in pos_rainha:
            desenho_linha += '[♛] '

        else:
            desenho_linha += '[ ] '

    print(desenho_linha)
print()